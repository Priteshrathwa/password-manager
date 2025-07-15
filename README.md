# 🔐 Password Manager (Terminal-Based, Python)

A simple terminal-based password manager built with Python.  
It uses strong AES encryption, master password protection, and clipboard copy functionality.

---

## 🚀 Features

- ✅ Save encrypted passwords by service & username  
- ✅ Retrieve passwords with clipboard copy  
- ✅ Master password authentication (bcrypt hashed)  
- ✅ AES encryption with `cryptography` module  

---

## 📦 Requirements

Install dependencies:
```bash
pip install -r requirements.txt
🛠 Setup
1. Generate Encryption Key (run once)
python
Copy
Edit
from cryptography.fernet import Fernet
with open("key.key", "wb") as f:
    f.write(Fernet.generate_key())
2. Create Master Password Hash (run once)
python
Copy
Edit
import bcrypt
password = input("Set your master password: ").encode()
hash = bcrypt.hashpw(password, bcrypt.gensalt())
with open("master.hash", "wb") as f:
    f.write(hash)
🧪 How to Use
Run the app:

bash
Copy
Edit
python main.py
Then follow the on-screen menu:

pgsql
Copy
Edit
1. Save Password
2. Get Password
3. Exit
📁 File Structure
main.py — Main logic (encryption, password storage)

key.key — AES encryption key (for demo only)

master.hash — Master password hash

requirements.txt — All dependencies

README.md — You’re reading it!

⚠️ Security Note
This is a practice/demo project.
In real use, do NOT upload:

key.key

master.hash

Use .gitignore to protect them.

👨‍💻 Author
Made with 💻 + 🔒 by Pritesh Rathwa
