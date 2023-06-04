import os
import hashlib
from src.AES import AESCipher
class encrypter:
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self.src = "files/"+self.file_name
        self.dest = 'encrypt/'+self.file_name
        self.password = self.generate_password()
        self.aes = self.generate_bytes()
        
    def generate_password(self):
        h = hashlib.new('ripemd160')
        h.update(self.read_file().encode('utf-8'))
        return h.hexdigest()
    
    def generate_bytes(self):
        cipher = AESCipher()
        encrypted_text = cipher.encrypt(self.read_file().encode('utf-8'))
        return encrypted_text
    
    def return_data_aes(self) -> bytes:
        return self.aes
    def return_name(self) -> str:
        return self.file_name
    def return_password(self) -> str:
        return self.password
    def return_src(self) -> str:
        return self.src
    
    def return_dest(self) -> str:
        return self.dest
    def get_password(self) -> str:
        return self.password
    
    def replace(self) -> None:
        os.replace(self.src, self.dest)
    
    def undo_replace(self) -> None:
        os.replace(self.dest, self.src)
        
    
    def read_file(self) -> str:
        file_item = ""
        with open(self.src) as f:
            file_item += f.read() + "\n"
        return file_item
    def read_file_utf8(self) -> str:
        with open(f"encrypt/{self.file_name.split('.')[0]}.bin", 'rb') as file:
            bytes_data = file.read()
        return bytes_data
    
    def encrypt(self):
        with open(f"encrypt/{self.file_name.split('.')[0]}.bin", "wb") as file:
            file.write(bytes(self.password, 'utf-8'))
            file.write(self.aes)
            

