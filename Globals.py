import tkinter as tk
from tkinter import ttk


class Global:
    window = tk.Tk()
    window.title("Crypt")

    window.geometry("500x500")

    frame = tk.Frame(window, padx=10, pady=10)
    frame.pack(expand=True)

    func = tk.Label(frame, text="Choose command(code or decode)")
    func.grid(row=3, column=1)

    func_in = tk.Entry(frame)
    func_in.grid(row=4, column=1)

    crypt = tk.Label(
        frame, text="Choose type of cryptographer (Cesar, Vigenere, Vernam)"
    )
    crypt.grid(row=5, column=1)

    crypt_in = tk.Entry(frame)
    crypt_in.grid(row=6, column=1)

    txt = tk.Label(frame, text="Write your text")
    txt.grid(row=7, column=1)

    txt_in = tk.Entry(frame, width="50")
    txt_in.grid(row=8, column=1)

    keyword = tk.Label(frame, text="Write keyword")
    keyword.grid(row=9, column=1)

    keyword_in = tk.Entry(frame)
    keyword_in.grid(row=10, column=1)

    txt_hack = tk.Label(frame, text="If you want hack cipher, enter path to txt file")
    txt_hack.grid(row=13, column=1)

    txt_hack_in = tk.Entry(
        frame, text="If you want hack cipher, enter path to txt file"
    )
    txt_hack_in.grid(row=14, column=1)

    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    label = ttk.Label(frame)
    label.grid(row=12, column=1)

    label2 = ttk.Label(frame)
    label2.grid(row=16, column=1)

    def __init__(self, t="", k="", c="", cr=""):
        self.text = t
        self.key = k
        self.command = c
        self.cryp = cr
