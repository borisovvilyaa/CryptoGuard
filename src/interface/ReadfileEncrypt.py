"""
Module: Readfile.py
Description: GUI interface for displaying and encrypting file contents.
Author: Borusov Illia
"""

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from src.encrypt import encrypter


class Readfile(ctk.CTk):
    def __init__(self, text, file):
        """
        Initializes the Readfile object with the given text content and file name.
        
        @param text: Text content to display in the GUI.
        @param file: Name of the file.
        """
        
        self.text_encrypt = text
        self.file = file

        ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
        self.window = ctk.CTk()
        self.window.geometry("420x320")
        self.window.title("CryptoGuard Editor v0.1-alpha | Borusov Illia")


        self.textbox = ctk.CTkTextbox(master=self.window, width=400, corner_radius=0)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textbox.insert("1.0", self.text_encrypt)

        self.window.grid_rowconfigure(0, weight=0)  # Make row 0 fill available vertical space
        self.window.grid_columnconfigure(0, weight=1)  # Make column 0 fill available horizontal space
    
        self.encrypt_button = ctk.CTkButton(master=self.window, text="Encrypt and Save", corner_radius=0, command=self.save)
        self.encrypt_button.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        
      


        self.window.grid_rowconfigure(0, weight=0)  # Make row 0 fill available vertical space
        self.window.grid_columnconfigure(0, weight=1)  # Make column 0 fill available horizontal space

        self.window.iconbitmap("logo.ico")  # Set window icon
    
    def show_message(self, password):
        """
        Displays a success message box with the encrypted file information.
        
        @param password: Generated password for the encrypted file.
        """
        CTkMessagebox(title="Success", message=f"File successfully encrypted!\nFile moved to folder: encrypt/{self.file.split('.')[0]}.gf\nPassword: {password}")

    def save(self):
        """
        Encrypts the file and displays the success message box with the generated password.
        """
        file = encrypter(self.file)
        if file.encrypt():
            self.show_message(file.get_password())
            print("Password for this file is", file.get_password())

    def run(self):
        """
        Runs the GUI application.
        """
        self.window.mainloop()


if __name__ == "__main__":
    app = Readfile("Hello", "example.txt")
    app.run()
