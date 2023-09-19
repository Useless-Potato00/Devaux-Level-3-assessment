import tkinter as tk
from tkinter import simpledialog
from tkinter.simpledialog import askstring 
class clas:
    
    def __init__(self): #this is what runs when the class is called and makes the window and background.
        self.window = tk.Tk()
        self.window.geometry("400x300")
        
        self.background = tk.Frame(self.window, height=300, width=400, bg="")
        self.background.place(relx=0.5, rely=0.5, anchor="center")

        self.wind = tk.Label(self.window, text="Welcome!")
        self.wind.pack()

        self.bt1 = tk.Button(self.window, text="Set Username", command = self.definition) #Button to call second def.
        self.bt1.pack()

        self.bt2 = tk.Button(self.window, text="Start", command = clas2)
        self.bt2.pack() #Calls the second class to create new window.

        self.window.title("First windo")

        self.window.mainloop()

    def definition(self): #This is the second def and is only run when you call it (Name input).
        
        self.yeet = askstring("Input name", "Input name")
        lisit = [self.yeet] #List that holds the username
        print(lisit)
        
class clas2: 
    def __init__(self): #When Clas2 is called it will run this definiton (Window 2), This will show a directory for what times tables the User wants to practice.

        self.window = tk.Tk()
        self.window.geometry("400x300")

        self.fretdf.label(text="Times table: ")
        self.fretdf.
        self.fegh()

    def fegh(self):
        global entry
        self.fing = entry.get()
        self.entry.config(text = int)
clas()