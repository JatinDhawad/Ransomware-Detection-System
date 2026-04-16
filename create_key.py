from cryptography.fernet import Fernet
import os


def create_key():
    if os.path.exists("key.key"):
        print("⚠️ Key already exists. Existing key preserved.")
        return

    key = Fernet.generate_key()

    with open("key.key", "wb") as file:
        file.write(key)

    print("✅ Key created successfully!")


create_key()