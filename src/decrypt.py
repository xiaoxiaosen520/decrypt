import hashlib
import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import getpass
import csv

def get_password():
    return getpass.getpass(prompt='enter your password: ')

def encrypt_file(input_file_path, output_file_path):
    with open(input_file_path, 'rb') as f:
        plaintext = f.read()
    password = get_password().encode()
    
    password_pre = get_password().encode()
    
    if password not in password_pre:
        return

    key = hashlib.sha256(password).digest()

    iv = os.urandom(16)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    with open(output_file_path, 'wb') as f:
        f.write(iv)
        f.write(ciphertext)

def decrypt_file(input_file_path):
    with open(input_file_path, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()

    password = get_password().encode()

    key = hashlib.sha256(password).digest()
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_data) + unpadder.finalize()
    return plaintext

def convert_to_dict_list(decrypted_data):
    data_lines = decrypted_data.decode().split('\n')
    reader = csv.DictReader(data_lines)
    dict_list = [row for row in reader]

    return dict_list

input_file_path = r'path'
output_file_path = r'path'

# encrypt_file(input_file_path, output_file_path)

# decrypted_data = decrypt_file(input_file_path)
# print(decrypted_data.decode())
# dict_list = convert_to_dict_list(decrypted_data)
# for row in dict_list:
#     print(row['phrase'])

# encrypt_file(r'path', r'path')

