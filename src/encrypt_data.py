from cryptography.fernet import Fernet

with open("dek.key", "rb") as f:
    dek = f.read()

cipher = Fernet(dek)

with open("data.txt", "rb") as f:
    plaintext = f.read()

ciphertext = cipher.encrypt(plaintext)

with open("data.enc", "wb") as f:
    f.write(ciphertext)

print("Data berhasil dienkripsi")