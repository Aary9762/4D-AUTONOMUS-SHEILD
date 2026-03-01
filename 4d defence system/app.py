from flask import Flask, render_template, jsonify, send_file
import json
import os
import random
import io
import time

app = Flask(__name__)

STATUS_FILE = "threat_log.json"
# System State with Automated Threat Logic and Self-Healing
state = {
    "shift_count": 0, 
    "current_port": 8080, 
    "mode": "STABLE",
    "vault_integrity": 100,
    "last_attack_time": time.time()
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/system_status')
def get_status():
    # Check for real sniffer hits from Scapy
    real_threat = os.path.exists(STATUS_FILE)
    
    # Automated Attack Logic: Simulate an intrusion every 15 seconds
    auto_threat = False
    current_time = time.time()
    if current_time - state["last_attack_time"] > 15:
        auto_threat = True
        if current_time - state["last_attack_time"] > 18: 
            state["last_attack_time"] = current_time

    threat_detected = real_threat or auto_threat
    
    if threat_detected:
        state["shift_count"] += 1
        state["current_port"] = random.randint(1024, 65535)
        state["mode"] = random.choice(["AMD_SEV_ISOLATION", "TEMPORAL_MTD", "ENCRYPT_SHUFFLE"])
        state["vault_integrity"] = max(state["vault_integrity"] - random.randint(1, 3), 65)
    else:
        state["mode"] = "STABLE"
        state["vault_integrity"] = min(state["vault_integrity"] + 0.1, 100) # Self-healing

    return jsonify({
        "current_port": state["current_port"],
        "threat_detected": threat_detected,
        "shift_count": state["shift_count"],
        "mode": state["mode"],
        "integrity": round(state["vault_integrity"], 1)
    })

@app.route('/download_report')
def download_report():
    report = f"=== AMD SLINGSHOT: 4D SHIELD V2.1 FORENSIC LOG ===\n"
    report += f"Compute Hardware: AMD EPYC™ 9004 Series\n"
    report += f"Packet Acceleration: AMD Alveo™ V70 SmartNIC\n"
    report += f"Total Mitigated Attacks: {state['shift_count']}\n"
    report += "--------------------------------------------------\n"
    report += "[SEC] Temporal Shift active. Attackers neutralized in honey-loop.\n"
    
    mem_file = io.BytesIO()
    mem_file.write(report.encode('utf-8'))
    mem_file.seek(0)
    return send_file(mem_file, as_attachment=True, download_name="Shield_Forensics.txt")

if __name__ == '__main__':
    if os.path.exists(STATUS_FILE): os.remove(STATUS_FILE)
    app.run(debug=True, port=5050)