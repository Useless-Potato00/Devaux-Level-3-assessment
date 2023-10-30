import tkinter as tk
from tkinter import simpledialog
from tkinter.simpledialog import askstring
import random

class MyClass: # The main class, the games menu.
    def __init__(self): # This is the intial defintion to start everything. It holds the window in which everything is shown.
        self.username = "None"
        self.score = 0
        self.window = tk.Tk()
        self.window.geometry("400x300")
        self.window.title("Main Window")
    
        self.background = tk.Frame(self.window, height=300, width=400, bg="green") 
        self.background.place(relx=0.5, rely=0.5, anchor="center") #This purely for asthetics. It makes the background of the window green.
    
        self.fra1 = tk.Frame(self.window, background="green")
        self.lab1 = tk.Label(self.fra1, text="Welcome!")
        self.lab1.pack()#Greet the user.
    
        self.bt1 = tk.Button(self.fra1, text="Set Username", command=self.name)
        self.lab2 = tk.Label(self.fra1, text="Username: None")
        self.lab2.pack()
        self.bt1.pack()#This button is used to set the username.

        self.bt3 = tk.Button(self.fra1, text="Load Save", command=self.load_save)
        self.bt3.pack()
    
        self.bt2 = tk.Button(self.fra1, text="Enter", command=self.times_table)
        self.bt2.pack()#This button is used to enter the times table game.
    
        self.fra1.pack()#packing for the frame
    
        self.window.mainloop()#this keeps the main window open

    def save_game(self):
        self.save_file = open("save.txt", "w")
        self.save_file.writelines("{}\n{}".format(self.username, self.score))
        self.save_file.close()
        simpledialog.messagebox.showinfo("Game Saved" , "Your game has been saved.")
    
    def load_save(self): #load save
        self.save_file = open("save.txt", "r")
        self.username = self.save_file.readline().strip()
        self.score = self.save_file.readline().strip()
        self.save_file.close()
        self.lab2.config(text="Username: {}".format(self.username)) #  For some reason this doesn't work.
        simpledialog.messagebox.showinfo("Save Loaded", "Your save has been loaded")
    
    def name(self): #Sets a username for the user.
        self.astr1 = askstring("Input name", "Input name")
        if self.astr1 == "":
            self.username = "None"
        else:
            self.username = self.astr1

        self.lab2.config(text="Username: {}".format(self.username))
    
    def times_table(self): #the defintion for the times table
        
        try:
            self.fra3.destroy()
        except:
            self.fra1.destroy()
            
        
        self.fra2 = tk.Frame(self.window, background="green")

        randy = random.randint(1, 10)
        randy2 = random.randint(1, 10)
        self.question = "{}, What is {} + {}?".format(self.username, randy, randy2)
        self.answer = randy + randy2
        print(self.question, self.answer)
        self.lab3 = tk.Label(self.fra2, text=self.question)
        self.lab3.pack()
        self.ent1 = tk.Entry(self.fra2)
        self.ent1.pack()
        self.bt3 = tk.Button(self.fra2, text="Enter", command=self.cheaking_answer)
        self.bt3.pack()
        
        self.fra2.pack()

    def cheaking_answer(self): #This cheaks is the player was correct or wrong.
        try:
            self.player_answer = int(self.ent1.get())
            if self.player_answer == self.answer:
                self.score += 1
                self.fra2.destroy()
                self.fra3 = tk.Frame(self.window, background="green")
                self.fra3.pack()
                self.lab4 = tk.Label(self.fra3, text="Congradulation {}! You got the answer correct!".format(self.username))
                self.lab4.pack()
                self.lab5 = tk.Label(self.fra3, text="Your score is {}".format(self.score))
                self.lab5.pack()
                self.bt4 = tk.Button(self.fra3, text="Save Game", command=self.save_game)
                self.bt4.pack()
                self.bt5 = tk.Button(self.fra3, text="Next Question", command=self.times_table)
                self.bt5.pack()

            else:
                self.fra2.destroy()
                self.fra3 = tk.Frame(self.window, background="green")
                self.fra3.pack()
                self.lab4 = tk.Label(self.fra3, text="Sorry {}, you got the wrong answer!".format(self.username))
                self.lab4.pack()
                self.lab5 = tk.Label(self.fra3, text="Your score is {}".format(self.score))
                self.bt5 = tk.Button(self.fra3, text="Next Question", command=self.times_table)
                self.bt5.pack()
                
        except ValueError:
            simpledialog.messagebox.showerror("Error", "Please enter a number")
    
obj = MyClass()#Calls the main class
obj.obj.mainloop()#starts