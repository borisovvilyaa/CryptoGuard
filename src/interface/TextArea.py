"""
Module: TextArea.py
Description: A GUI application for displaying and editing text.
Author: Borusov Illia
"""

from config import VERSION
import customtkinter as ctk

class TextArea(ctk.CTk):
    def __init__(self, text):
        """
        Initialize the TextArea class.

        @param text: The initial text to be displayed in the text area.
        """
        self.text_encrypt = text

        ctk.set_default_color_theme("dark-blue")
        self.window = ctk.CTk()
        self.window.geometry("800x600")
        self.window.title(f"CryptoGuard Editor {VERSION} | Borusov Illia")

        self.textbox = ctk.CTkTextbox(master=self.window, width=800, height=600, corner_radius=0)
        self.textbox.pack(fill="both", expand=True)
        self.textbox.insert("1.0", self.text_encrypt)
        self.textbox.configure(font=("Monospace", 12))

        self.window.iconbitmap("logo.ico")

    def run(self):
        """
        Run the application main loop.
        """
        self.window.mainloop()

if __name__ == "__main__":
    app = TextArea("text")
    app.run()
