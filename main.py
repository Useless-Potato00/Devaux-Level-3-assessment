import tkinter as tk
from tkinter import simpledialog
from tkinter.simpledialog import askstring
import random

class MyClass:
    def __init__(self):
        
        self.window = tk.Tk()
        self.window.geometry("400x300")
        self.window.title("Main Window")
    
        self.background = tk.Frame(self.window, height=300, width=400, bg="green")
        self.background.place(relx=0.5, rely=0.5, anchor="center")
    
        self.fra1 = tk.Frame(self.window)
        self.lab1 = tk.Label(self.fra1, text="Welcome!")
        self.lab1.pack()
    
        self.bt1 = tk.Button(self.fra1, text="Set Username", command=self.name)
        self.bt1.pack()
    
        self.bt2 = tk.Button(self.fra1, text="Enter", command=self.times_table)
        self.bt2.pack()
    
        self.fra1.pack()
    
        self.window.mainloop()
    
    def name(self):
        self.yeet = askstring("Input name", "Input name")
        if self.yeet:
            self.username = self.yeet
    
    def times_table(self):
        
        self.fra1.destroy()
        
        self.fra2 = tk.Frame(self.window)
        
        self.ask1 = tk.Entry(self.fra2)
        self.ask1.focus_set()
        self.ask1.pack()
        
        self.lab2 = tk.Label(self.fra2, text="")
        self.lab2.pack()
        
        self.bt3 = tk.Button(self.fra2, text="enter", command=self.update_label)
        self.bt3.pack()
        
        self.fra2.pack()
        
    def update_label(self): #I couldn't understand how '.get' worked so I used Chat Gpt to help me work that out, this being the result.
        
        entered_text = self.ask1.get()# A variable named 'entered_text' is created to store the user input received from 'self.ask1'.
        self.lab2.config(text=entered_text)#This takes the input from entered_text and changes the 'lab2' label to that text.

        if entered_text == "abc":  
             print("hello")
            
obj = MyClass()
obj.start()
MyClass()