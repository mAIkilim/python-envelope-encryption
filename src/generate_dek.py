from cryptography.fernet import Fernet

dek = Fernet.generate_key()

with open("dek.key", "wb") as f:
    f.write(dek)

print("DEK berhasil dibuat")