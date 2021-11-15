import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

source_file = 'fiddling/artifacts/apple.png'
encrypted_file = 'fiddling/artifacts/encrypted-apple'
decrypted_file = 'fiddling/artifacts/decrypted-apple.png'

password = b"password"
salt = os.urandom(16)

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
)

key = base64.urlsafe_b64encode(kdf.derive(password))
f = Fernet(key)

with open(source_file, 'rb') as file:
    original = file.read()

encrypted = f.encrypt(original)
with open(encrypted_file, 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

decrypted = f.decrypt(encrypted)
with open(decrypted_file, 'wb') as decrypted_file:
    decrypted_file.write(decrypted)