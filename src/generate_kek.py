from cryptography.fernet import Fernet

kek = Fernet.generate_key()

with open("kek_v1.key", "wb") as f:
    f.write(kek)

print("KEK berhasil dibuat")