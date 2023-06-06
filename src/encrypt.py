"""
Module: encrypt.py
Description: File encryption utility using AES encryption algorithm.
Author: Borusov Illia
"""

import os
import hashlib
from src.AES import AESCipher


class encrypter:
    def __init__(self, file_name):
        """
        Initializes the encrypter object with the given file name and sets the source and destination paths.
        Also generates a password and encrypts the file using AES encryption.
        
        @param file_name: Name of the file to encrypt.
        """

        self.file_name = file_name
        self.src = "files/" + self.file_name
        self.dest = "encrypt/" + self.file_name
        self.password = self.generate_password()
        self.aes = self.generate_bytes()

    def generate_password(self):
        """
        Generates a password by applying the RIPEMD-160 hash function to the contents of the file.
        
        @return: Generated password.
        """

        return self.ripemd160(self.read_file())

    def ripemd160(self, s):
        """
        Applies the RIPEMD-160 hash function to the given string.
        
        @param s: Input string.
        @return: Hashed string.
        """

        h = hashlib.new("ripemd160")
        h.update(s.encode("utf-8"))
        return h.hexdigest()

    def generate_bytes(self):
        """
        Generates the encrypted bytes of the file using AES encryption.
        
        @return: Encrypted bytes.
        """

        cipher = AESCipher()
        encrypted_text = cipher.encrypt(self.read_file().encode("utf-8"))
        return encrypted_text

    def return_data_aes(self):
        """
        Returns the encrypted bytes.
        
        @return: Encrypted bytes.
        """

        return self.aes

    def return_name(self):
        """
        Returns the file name.
        
        @return: File name.
        """

        return self.file_name

    def return_password(self):
        """
        Returns the generated password.
        
        @return: Generated password.
        """

        return self.password

    def return_src(self):
        """
        Returns the source path of the file.
        
        @return: Source path.
        """

        return self.src

    def return_dest(self):
        """
        Returns the destination path of the file.
        
        @return: Destination path.
        """

        return self.dest

    def get_password(self):
        """
        Returns the generated password.
        
        @return: Generated password.
        """

        return self.password

    def replace(self):
        """
        Replaces the original file with the encrypted file.
        """

        os.replace(self.src, self.dest)

    def undo_replace(self):
        """
        Reverts the file replacement by moving the encrypted file back to the original location.
        """

        os.replace(self.dest, self.src)

    def read_file(self):
        """
        Reads the contents of the file and returns it as a string.
        
        @return: Contents of the file.
        """

        file_item = ""
        with open(self.src) as f:
            file_item += f.read() + "\n"
        return file_item

    def read_file_utf8(self):
        """
        Reads the contents of the encrypted file in UTF-8 encoding and returns it as bytes.
        
        @return: Contents of the encrypted file as bytes.
        """

        with open(f"encrypt/{self.file_name.split('.')[0]}.gf", "rb") as file:
            bytes_data = file.read()
        return bytes_data

    def encrypt(self):
        """
        Encrypts the file by writing the password and encrypted bytes to the encrypted file.
        
        @return: True if encryption is successful, False otherwise.
        """

        try:
            with open(f"encrypt/{self.file_name.split('.')[0]}.gf", "wb") as file:
                file.write(bytes(self.ripemd160(self.password), "utf-8"))
                file.write(self.aes)
            return True
        except Exception as e:
            print(f"Encryption failed: {str(e)}")
            return False
