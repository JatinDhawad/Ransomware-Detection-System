from cryptography.fernet import Fernet, InvalidToken
import os


def decrypt_files(folder, user_key):
    try:
        cipher = Fernet(user_key.encode())

    except Exception:
        return -1

    count = 0

    try:
        files = os.listdir(folder)

    except Exception as e:
        print(f"[DECRYPT ERROR] Unable to access folder: {e}")
        return 0

    for filename in files:

        if not filename.endswith(".locked"):
            continue

        path = os.path.join(folder, filename)

        try:
            with open(path, 'rb') as file:
                data = file.read()

            decrypted_data = cipher.decrypt(data)

            original_name = filename.replace(".locked", "")
            new_path = os.path.join(folder, original_name)

            with open(new_path, 'wb') as file:
                file.write(decrypted_data)

            os.remove(path)

            count += 1

            print(f"[DECRYPTED] {original_name}")

        except InvalidToken:
            return -2

        except Exception as e:
            print(f"[DECRYPT ERROR] Failed on {filename}: {e}")

    return count