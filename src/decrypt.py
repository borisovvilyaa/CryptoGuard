"""
Module: decrypter.py
Description: Decrypts an encrypted file using AES encryption.
Author: Borusov Illia
"""

from src.encrypt import encrypter
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad


class decrypter(encrypter):
    def __init__(self, file, password) -> None:
        """
        Initializes the decrypter object with the encrypted file and password.
        
        @param file: Name of the encrypted file.
        @param password: Password for decryption.
        """
        self.file = file
        self.key = b'\xfbkL\x83mpq\xf9\x90\xe6\x89\xfc\x82\xa3T\x00'
        self.password = password
    
    def verify(self) -> bool:
        """
        Verifies if the password is correct by comparing the stored password hash with the decrypted hash from the file.
        
        @return: True if the password is correct, False otherwise.
        """
        if self.ripemd160(self.password).encode("utf-8") == self.decrypt_from_file()[:40]:
            return True
        else:
            return False
    
    def decrypt(self):
        """
        Decrypts the encrypted file using AES encryption.
        
        @return: Decrypted text if the password is correct, an error message otherwise.
        """
        if self.verify():
            cipher = AES.new(self.key, AES.MODE_ECB)
            decrypted_text = cipher.decrypt(self.decrypt_from_file()[40:])
            return decrypted_text.decode('utf-8')
        else:
            return "Wrong password!"
    
    def decrypt_from_file(self) -> bytes:
        """
        Reads the encrypted file and returns the file content as bytes.
        
        @return: Encrypted file content as bytes.
        """
        with open(f'encrypt/{self.file}', 'rb') as file:
            bytes_data = file.read()
        return bytes_data
