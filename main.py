"""
Module: main.py
Description: A GUI application for file encryption and decryption using the CryptoGuard library.
Author: Borusov Illia
Version: 0.1-alpha
"""

from src.encrypt import encrypter
# from src.render import *
# from src.decrypt import decrypter

import os
import shutil

import customtkinter as ctk
from tkinter import filedialog
from PIL import ImageTk, Image
from src.interface.ReadfileEncrypt import Readfile


class App:
    def __init__(self):
        """
        Initializes the application window and sets up the GUI elements.
        """

        ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

        self.window = ctk.CTk()
        self.window.geometry("420x320")
        self.window.title("CryptoGuard v0.1-alpha | Borusov Illia")

        self.logo_path = "logo.png"
        self.logo_image = Image.open(self.logo_path)
        self.logo_image_tk = ImageTk.PhotoImage(self.logo_image)

        self.logo = ctk.CTkLabel(self.window)
        self.logo.configure(image=self.logo_image_tk, text="")
        self.logo.pack(pady=10)

        self.encrypt_button = ctk.CTkButton(self.window, text="Encrypt", command=self.encrypt_action)
        self.encrypt_button.pack(pady=10)

        self.decrypt_button = ctk.CTkButton(self.window, text="Decrypt", command=self.decrypt_action)
        self.decrypt_button.pack(pady=10)

        self.generate_password_button = ctk.CTkButton(self.window, text="Generate password SHA-3", command=self.generate_password)
        self.generate_password_button.pack(pady=10)

        self.window.iconbitmap("logo.ico")

    def encrypt_action(self):
        """
        Callback function for the encrypt button.
        Prompts the user to select a text file to encrypt, moves it to the 'files' folder,
        and performs encryption using the 'encrypter' module.
        """

        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

        # Determine the path to the 'files' folder in the root project directory
        root_folder = os.path.dirname(os.path.abspath(__file__))
        files_folder = os.path.join(root_folder, "files")

        # Create the 'files' folder if it doesn't exist
        if not os.path.exists(files_folder):
            os.makedirs(files_folder)

        # Get the file name from the full path
        file_name = os.path.basename(file_path)

        # Define the new path to move the file to the 'files' folder
        new_file_path = os.path.join(files_folder, file_name)

        # Move the file to the 'files' folder
        shutil.move(file_path, new_file_path)

        file = encrypter(file_name)
        readfile = Readfile(file.read_file(), file_name)
        readfile.run()

    def decrypt_action(self):
        """
        Callback function for the decrypt button.
        Prompts the user to select an encrypted file, moves it to the 'encrypt' folder,
        and performs decryption using the 'decrypter' module.
        """

        file_path = filedialog.askopenfilename(filetypes=[("Encrypt file", "*.gf")])
        root_folder = os.path.dirname(os.path.abspath(__file__))
        files_folder = os.path.join(root_folder, "encrypt")

        # Create the 'encrypt' folder if it doesn't exist
        if not os.path.exists(files_folder):
            os.makedirs(files_folder)

        # Get the file name from the full path
        file_name = os.path.basename(file_path)

        # Define the new path to move the file to the 'encrypt' folder
        new_file_path = os.path.join(files_folder, file_name)

        # Move the file to the 'encrypt' folder
        shutil.move(file_path, new_file_path)

    def generate_password(self):
        """
        Callback function for the generate password button.
        Generates a password using the SHA-3 algorithm.
        """

        pass

    def run(self):
        """
        Runs the application main loop.
        """

        self.window.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
