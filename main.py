import tkinter as tk
from tkinter import simpledialog
from tkinter.simpledialog import askstring 
class clas:
    
    def __init__(self): #this is what runs when the class is called and makes the window and background
        self.window = tk.Tk()
        self.window.geometry("400x300")
        
        self.background =tk.Frame(self.window, height=300, width=400)
        self.background.place(relx=0.5, rely=0.5, anchor="center")

        self.definition() #this runs the second def in this class
        self.window.mainloop()

    def definition(self): # This is the second def and is only run when you call it. This sets the labels and buttons
        
        self.neww = tk.Label(self.window, text="Your first window!")
        self.neww.pack()
        
        self.bt1 = tk.Button(self.window, text="New", command=clas2) #New window button
        self.bt1.pack()

        self.bt2 = tk.Button(self.window, text="set username", command=clas3)
        self.bt2.pack()

class clas2: 
    def __init__(self): #When Clas2 is called it will run this definiton (Window 2)
        
        self.window = tk.Tk()
        self.window.geometry("400x300")
    
        self.window2 = tk.Label(self.window, text="Second Window")
        self.window2.pack()

class clas3:
    def __init__(self):

        self.yeet = askstring("Input name", "Input name")
        lisit = [self.yeet]
        print(lisit)
clas()