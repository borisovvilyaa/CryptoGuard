from src.encrypt import encrypter
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

class decrypter (encrypter):
    def __init__(self, file) -> None:
        self.file = file
        self.key =  b'\xfbkL\x83mpq\xf9\x90\xe6\x89\xfc\x82\xa3T\x00'

    def decrypt(self):
        cipher = AES.new(self.key, AES.MODE_ECB)
        decrypted_text = cipher.decrypt(self.file.generate_bytes())
        return decrypted_text
