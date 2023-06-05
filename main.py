from src.encrypt import encrypter
# from src.render import *
from src.decrypt import decrypter

import customtkinter as ctk
from tkinter import filedialog
from PIL import ImageTk, Image

class App:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("420x320")
        self.window.title("CryptoGuard v0.1-alpha | Borusov Illia")
        
        self.logo_path = "logo.jpg"
        self.logo_image = Image.open(self.logo_path)
        self.logo_image.thumbnail((100, 100))  # Изменение размера изображения до 100x100
        
        self.logo_image_tk = ImageTk.PhotoImage(self.logo_image)
        
        self.logo = ctk.CTkLabel(self.window)
        self.logo.configure(image=self.logo_image_tk, text="")
        self.logo.pack(pady=10)
        
        self.encrypt_button = ctk.CTkButton(self.window, text="Encrypt", command=self.encrypt_action)
        self.encrypt_button.pack(pady=10)
        
        self.decrypt_button = ctk.CTkButton(self.window, text="Decrypt", command=self.decrypt_action)
        self.decrypt_button.pack(pady=10)
        
        
        self.decrypt_button = ctk.CTkButton(self.window, text="Generate password SHA-3", command=self.generate_passowrd)
        self.decrypt_button.pack(pady=10)
        
        self.window.iconbitmap("logo.ico")  # Установка иконки окна

    def encrypt_action(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        print("Encrypt file:", file_path)
    
    def decrypt_action(self):
        file_path = filedialog.askopenfilename(filetypes=[("Encrypt file", "*.gf")])
        print("Decrypt file:", file_path)
    def generate_passowrd(self):
        pass
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()




# print("--------------------------------Begin--------------------------------")

# # Make test demo output file

# file = encrypter("file.txt")
# print("Password for this file is", file.get_password())
# file.encrypt()

# # print(file.read_file_utf8())

# file_decrypter = decrypter("file.gf", "38e8606c44c0cc3c06cf790f7892c12136912258")
# print(file_decrypter.decrypt())

# print("--------------------------------End--------------------------------")

