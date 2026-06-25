from cryptography.fernet import Fernet

new_kek = Fernet.generate_key()

with open("kek_v2.key", "wb") as f:
    f.write(new_kek)

print("KEK baru berhasil dibuat")