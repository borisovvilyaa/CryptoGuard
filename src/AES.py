from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

class AESCipher:
    def __init__(self):
        self.key =  b'\xfbkL\x83mpq\xf9\x90\xe6\x89\xfc\x82\xa3T\x00'

    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_ECB)
        padded_data = pad(data, AES.block_size)
        cipher_text = cipher.encrypt(padded_data)
        return cipher_text

    def decrypt(self, cipher_text):
        decipher = AES.new(self.key, AES.MODE_ECB)
        decrypted_data = decipher.decrypt(cipher_text)
        unpadded_data = unpad(decrypted_data, AES.block_size)
        return unpadded_data

