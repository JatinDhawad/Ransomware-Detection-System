import encryptor
import decryptor
import monitor
import detector
import os
import threading

FOLDER = "test_data"


def detect():
    stop_flag = {"stop": False}
    result = {"changes": 0, "files": 0}

    locked_files = [f for f in os.listdir(FOLDER) if f.endswith(".locked")]

    if locked_files:
        print("⚠️ Recovery required before starting new attack.")
        return "recovery_required", 0

    def monitor_thread():
        result["changes"] = monitor.monitor_activity(FOLDER, stop_flag)

    t1 = threading.Thread(target=monitor_thread)
    t1.start()

    print("[+] Monitoring during attack...")

    result["files"] = encryptor.encrypt_files(FOLDER, stop_flag)

    t1.join()

    print(f"[+] Files affected: {result['files']}")
    print(f"[+] Changes detected: {result['changes']}")

    if detector.detect_ransomware(result["changes"]):
        print("🚨 RANSOMWARE DETECTED!")
        return True, result["files"]

    elif result["files"] > 0:
        print("⚠️ Attack Executed But Threshold Not Reached")
        return False, result["files"]

    else:
        print("✅ No Threat Detected")
        return False, 0


def recover(user_key):
    return decryptor.decrypt_files(FOLDER, user_key)