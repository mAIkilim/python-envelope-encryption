from cryptography.fernet import Fernet

with open("dek_recovered.key", "rb") as f:
    dek = f.read()

cipher = Fernet(dek)

with open("data.enc", "rb") as f:
    ciphertext = f.read()

plaintext = cipher.decrypt(ciphertext)

print(plaintext.decode())