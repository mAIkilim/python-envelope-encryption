from cryptography.fernet import Fernet

with open("kek_v1.key", "rb") as f:
    old_kek = f.read()

old_cipher = Fernet(old_kek)

with open("encrypted_dek.bin", "rb") as f:
    encrypted_dek = f.read()

dek = old_cipher.decrypt(encrypted_dek)

with open("kek_v2.key", "rb") as f:
    new_kek = f.read()

new_cipher = Fernet(new_kek)

encrypted_dek_v2 = new_cipher.encrypt(dek)

with open("encrypted_dek_v2.bin", "wb") as f:
    f.write(encrypted_dek_v2)

print("Rotasi KEK berhasil")