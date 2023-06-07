import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from src.decrypt import decrypter
from src.interface.TextArea import TextArea

class ReadfileDecryption(ctk.CTk):
    def __init__(self, file):
        """
        Initialize the ReadfileDecryption class.

        @param file: The file to be decrypted.
        """
        self.file = file

        ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
        self.window = ctk.CTk()
        self.window.geometry("320x120")
        self.window.title("CryptoGuard Editor v0.1-alpha | Borusov Illia")
        self.window.resizable(False, False)
        self.password_label = ctk.CTkLabel(self.window, text="Password:")
        self.password_label.pack()

        self.password_entry = ctk.CTkEntry(self.window, show="*")
        self.password_entry.pack()

        self.submit_button = ctk.CTkButton(self.window, text="Submit", command=self.submit_password)
        self.submit_button.pack()

    def submit_password(self):
        """
        Handle the submit button click event.
        """
        password = self.password_entry.get()
        dec = decrypter(self.file, password)
        # Add code here to handle the entered password
        if dec.verify():
            self.window.destroy()

            CTkMessagebox(title="Success", message="Passwords were successfully")
            TextArea(dec.decrypt()).run()
        else:
            CTkMessagebox(title="Error", message="Passwords were not valid")

    def run(self):
        """
        Run the application main loop.
        """
        self.window.mainloop()

if __name__ == "__main__":
    app = ReadfileDecryption("example.txt")
    app.run()
