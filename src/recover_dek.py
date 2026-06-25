from cryptography.fernet import Fernet

with open("kek_v1.key", "rb") as f:
    kek = f.read()

cipher = Fernet(kek)

with open("encrypted_dek.bin", "rb") as f:
    encrypted_dek = f.read()

dek = cipher.decrypt(encrypted_dek)

with open("dek_recovered.key", "wb") as f:
    f.write(dek)

print("DEK berhasil dipulihkan")