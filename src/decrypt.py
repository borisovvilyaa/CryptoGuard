from src.encrypt import encrypter
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

class decrypter (encrypter):
    def __init__(self, file, password) -> None:
        self.file = file
        self.key =  b'\xfbkL\x83mpq\xf9\x90\xe6\x89\xfc\x82\xa3T\x00'
        self.password = password
    def verify(self) -> bool:
        if self.password == self.decrypt_from_file()[:40]:
            return True
        else:
            return False
    def decrypt(self):
        # print(self.verify())
        if self.verify(): 
            cipher = AES.new(self.key, AES.MODE_ECB)
            decrypted_text = cipher.decrypt(self.decrypt_from_file()[40:])
            return decrypted_text.decode('utf-8')
        else:
            return "Password not wrong! Fuck u bith"
    def decrypt_from_file(self) -> bytes:
        with open(f'encrypt/{self.file}', 'rb') as file:
            bytes_data = file.read()
        return bytes_data
            