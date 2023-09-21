import tkinter as tk
from tkinter import simpledialog
from tkinter.simpledialog import askstring 
class clas:
    
    def __init__(self): #this is what runs when the class is called and makes the window and background.
        self.window = tk.Tk()
        self.window.geometry("400x300")
        
        self.background = tk.Frame(self.window, height=300, width=400, bg="")
        self.background.place(relx=0.5, rely=0.5, anchor="center")#Purely for decoration

        self.fr = tk.Frame(self.window)
        self.wind = tk.Label(self.fr, text="Welcome!")
        self.wind.pack()
        self.bt1 = tk.Button(self.fr, text="Set Username", command = self.definition) #Button to call the 'definition' def.
        self.bt1.pack()
        self.bt2 = tk.Button(self.fr, text="Set Username", command = 
        self.thing) #Button to call the 'thng' def.
        self.bt2.pack()
        self.fr.pack()

        self.window.title("Main Window")#Title of window

        self.window.mainloop()

    def definition(self): #This is the second def and is only run when you call it (Name input).
        
        self.yeet = askstring("Input name", "Input name")
        lisit = [self.yeet] #List that holds the username
        print(lisit)
        
    def game(self):

        self.fr.destroy()

        self.fretdf.label(selftext="Times table: ")
        self.fretdf.pack()
        self.fegh()

    def thing(self):

        self.fr.destroy()
        
        global entry
        self.fing = entry.get()
        self.entry.config(text = int)
        self.print(self.fing)
clas()