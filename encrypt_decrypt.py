#!/usr/bin/env python3
# coding: utf-8
#
### Modules import
from cryptography.fernet import Fernet

### Variables initialization
key = Fernet.generate_key()
f = Fernet(key)

### Code
print(key.decode())
encrypted_data = f.encrypt(b"Hello World")
print("After encryption : ", encrypted_data)
decrypted_data = f.decrypt(encrypted_data)
print("After decryption : ", decrypted_data.decode())

### End
