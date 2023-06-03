import os
import hashlib
class encrypter:
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self.src = "files/"+self.file_name
        self.dest = 'encrypt/'+self.file_name
        self.password = self.generate_password()
        
    def generate_password(self):
        h = hashlib.new('ripemd160')
        h.update(self.read_file().encode('utf-8'))
        return h.hexdigest()
    
    def return_name(self) -> str:
        return self.file_name
    
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
    

