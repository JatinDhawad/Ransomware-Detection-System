# Autonomous Ransomware Detection and Recovery System

A Python-based cybersecurity mini project that simulates ransomware behavior, detects suspicious encryption activity using behavioral analysis, stops the attack in real time, and provides secure file recovery using a decryption key.

---

## Project Overview

This project demonstrates the complete ransomware security lifecycle:

1. **Attack Simulation** – Encrypts files and renames them with `.locked`
2. **Behavior Monitoring** – Monitors suspicious encrypted file creation
3. **Real-Time Detection** – Detects ransomware using threshold-based behavioral analysis
4. **Attack Prevention** – Stops encryption mid-execution
5. **Recovery System** – Restores files using correct decryption key

---

## Features

- AES-based file encryption using Fernet
- Real-time behavioral ransomware detection
- Automatic attack interruption
- File recovery with decryption key verification
- Simulated ransomware popup and countdown
- GUI dashboard using Tkinter
- Activity logging and file impact reporting

---

## Tech Stack

- **Language:** Python
- **GUI:** Tkinter
- **Encryption:** Cryptography (Fernet / AES-based)
- **Concepts Used:** Behavioral Analysis, Symmetric Encryption, Intrusion Prevention

---

## Project Structure

```text
ransomware-detection-system/
│
├── gui.py
├── main.py
├── encryptor.py
├── decryptor.py
├── monitor.py
├── detector.py
├── create_key.py
├── test_data/
└── README.md
```

How It Works
1. Start Attack
 - Simulates ransomware attack
 - Encrypts files in test_data/
 - Renames them to .locked
2. Monitor Activity
 - Tracks newly created .locked files
 - Counts suspicious file encryption events
3. Detect Threat
 - If encrypted file count exceeds threshold:
 - Flags ransomware
 - Stops attack immediately
4. Recover Files
 - User enters decryption key
 - Files restored to original state

Setup Instructions
Install Dependencies
```
pip install cryptography
```
Generate Encryption Key
```
python create_key.py
```
Run Application
```
python gui.py
```
Detection Logic

The system uses behavior-based detection:

If the number of encrypted .locked files created in a short time exceeds a predefined threshold, the system classifies the activity as ransomware.

Limitations
 - Monitors only specified folder (test_data)
 - Threshold-based detection may cause false positives
 - Educational simulation only (not production security software)
Educational Purpose

This project is built for academic demonstration of:

 - Malware Simulation
 - Ransomware Behavior
 - Behavioral Threat Detection
 - Real-Time Attack Prevention
 - Incident Recovery Mechanisms

Author

Developed as part of Cyber Security Mini Project.


---

# Optional Suggestion

After adding README:
- GitHub repo will look much more professional
- Helps faculty/recruiters understand project instantly

---

If you want, I can help you refine it further (badges, screenshots, demo GIF, architecture diagram, etc.) or assist with any other project materials.
