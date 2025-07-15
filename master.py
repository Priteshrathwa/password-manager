import bcrypt

master_password = "".encode()
hashed = bcrypt.hashpw(master_password, bcrypt.gensalt())

with open("master.hash", "wb") as f:
    f.write(hashed)
