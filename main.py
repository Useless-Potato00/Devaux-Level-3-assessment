import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("400x300")

ro = tk.Label(text="Python Rocks!")
ro.pack()

ret = tk.Label(width="300", height="300")
ret.pack()

h=ttk.Button(text="Python")
h.pack()

window.mainloop()