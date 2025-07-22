import bcrypt
import getpass
from cryptography.fernet import Fernet
import pyperclip


def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as file:
        file.write(key)


def load_key():
    return open("key.key", "rb").read()

def encrypt_password(password):
    key = load_key()
    fernet = Fernet(key)
    return fernet.encrypt(password.encode())

def decrypt_password(encrypted_password):
    key = load_key()
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_password).decode()


import json
import os

def save_password(service, username, password):
    encrypted = encrypt_password(password)
    data = {}

    if os.path.exists("data.json") and os.path.getsize("data.json") > 0:
        with open("data.json", "r") as file:
            data = json.load(file)
    else:
        data = {}


    # Initialize list if not present
    if service not in data:
        data[service] = []

    # Append new username-password pair
    data[service].append({
        "username": username,
        "password": encrypted.decode()
    })

    with open("data.json", "w") as file:
        json.dump(data, file, indent=2)


def get_password(service, username):
    if not os.path.exists("data.json") or os.path.getsize("data.json") == 0:
        return None

    with open("data.json", "r") as file:
        data = json.load(file)

    if service in data:
        for entry in data[service]:
            if entry["username"] == username:
                decrypted = decrypt_password(entry["password"].encode())
                return decrypted
    return None




def main():
    with open("master.hash", "rb") as f:
        stored_hash = f.read()

    master = getpass.getpass("Enter master password to unlock: ").encode()

    if not bcrypt.checkpw(master, stored_hash):
        print("❌ Access denied.")
        return
    else:
        print("✅ Access granted.\n")
    

    while True:
        print("\n1. Save Password")
        print("2. Get Password")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            service = input("Service Name: ")
            username = input("Username: ")
            password = input("Password: ")
            save_password(service, username, password)
            print("✅ Password saved!")
        elif choice == "2":
            service = input("Service Name: ")
            username = input("Username: ")
            password = get_password(service, username)
            if password:
                pyperclip.copy(password)
                print(f"\n🔐 Password for {username}: {password}")
            else:
                print("❌ No record found for that service and username.")

        elif choice == "3":
            print("Bye! 🔒")
            break
        else:
            print("❗ Invalid choice")

main()


