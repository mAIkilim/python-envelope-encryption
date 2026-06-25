from cryptography.fernet import Fernet

with open("kek_v1.key", "rb") as f:
    kek = f.read()

cipher = Fernet(kek)

with open("dek.key", "rb") as f:
    dek = f.read()

encrypted_dek = cipher.encrypt(dek)

with open("encrypted_dek.bin", "wb") as f:
    f.write(encrypted_dek)

print("DEK berhasil dilindungi")