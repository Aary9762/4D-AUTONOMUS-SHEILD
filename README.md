# 4D-AUTONOMUS-SHEILD
The core philosophy of this project is to move from Static Defense (walls that stay in one place) to Active, Polymorphic Defense (a system that changes shape over time to confuse and trap attackers).
The 4D Autonomous Shield shifts the paradigm from static defense to an active, polymorphic battlefield. Traditional firewalls are "static walls" that attackers have the luxury of time to map and bypass. Our system uses Time as the 4th Dimension, constantly rotating entry points and network signatures to create a moving target.


Key Innovation: The 3-Pillar Defense
The Shield (MTD): Automated socket logic that randomly rotates server port numbers every 15–30 seconds.
The Trap (TCP Tarpit): A "Honey-Maze" that deceives unauthorized connections by feeding them 1-byte messages, infinitely wasting attacker computational resources.
The Brain (AI Adaptation): An LLM-driven engine that monitors connection patterns and increases "temporal entropy" (rotation speed) during active threats.


Tech Stack & Hardware:
Core Logic: Python (Socket, Scapy, L3RawSocket) 
UI/Frontend: HTML5 Canvas (Particle Swarm Rendering) & Flask 

AMD Integration (Proposed):
AMD EPYC™: High-performance local AI inference for the "Neural Brain." 
AMD Alveo™ V70: Hardware-accelerated L4-L7 packet filtering for sub-millisecond response. 
AMD Infinity Guard (SEV-SNP): Hardware-isolated sandboxing for the core Data Vault. 

4D Visual Dashboard
The UI features a real-time Particle Swarm:
Blue Particles: Represent the active, jumping Shield protecting the central "Data Vault." 
Red Particles: Represent detected attacker probes being trapped in the "Honey-Maze." 
Neural Console: Displays real-time AI behavioral analysis and shift coordinates. 

Installation & Usage
1. Prerequisites
Python 3.10+

Npcap (Installed in WinPcap compatibility mode)

Administrative Privileges (for Scapy raw packet sniffing)

2. Setup
git clone https://github.com/[Aary9762]/4d-autonomous-shield.git
cd 4d-autonomous-shield
pip install -r requirements.txt

3. Run the Shield
Terminal 1 (The Core):
python app.py

Terminal 2 (The Hardware Sniffer - Admin):
python shield_core.py

usiness Potential
This solution addresses a critical gap for small-to-medium enterprises that lack access to enterprise-grade MTD. By leveraging open-source logic and AMD edge hardware, we provide a cost-effective, post-quantum ready defense that actively drains attacker resources.
+2

The EquiNova Team:
Arvind Singh Manhas - Team Leader , Core Developer(Aary9762)
Animesh Pandey - Core Developer(Akkun77)
