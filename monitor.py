import os
import time
import detector


def monitor_activity(folder, stop_flag):
    threshold = detector.THRESHOLD
    changes = 0
    detected_locked = set()

    start_time = time.time()
    timeout = 20

    while not stop_flag["stop"]:

        try:
            current_files = os.listdir(folder)

        except Exception as e:
            print(f"[MONITOR ERROR] {e}")
            return changes

        for file in current_files:

            if file.endswith(".locked") and file not in detected_locked:
                detected_locked.add(file)
                changes += 1

                print(f"[MONITOR] Suspicious encrypted file detected: {file}")

                if changes >= threshold:
                    print("🚨 Ransomware Detected! Stopping attack...")
                    stop_flag["stop"] = True
                    return changes

        if time.time() - start_time > timeout:
            print("[MONITOR] Monitoring timeout reached.")
            return changes

        time.sleep(0.2)

    return changes