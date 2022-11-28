import tkinter as tk
import Globals as glob
import Functions as fn

on_btn = tk.Button(glob.Global.frame, text="perform", command=fn.ShowText)
on_btn.grid(row=11, column=1)


hacker_btn = tk.Button(glob.Global.frame, text="hack", command=fn.CallHack)
hacker_btn.grid(row=15, column=1)


glob.Global.window.mainloop()
