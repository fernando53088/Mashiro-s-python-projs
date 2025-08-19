import random 
import tkinter 

def show_choice():
   result = random.choice(['yes', 'no'])
   label.config(text=result)

root = tkinter.Tk() # opening root
root.title("Yes or No Game")
root.geometry("300x300")

label = tkinter.Label(root, text="", font=("Arial", 24))
label.pack(pady=20)

button = tkinter.Button(root, text="Choose!", command=show_choice, font=("Arial, 18"))
button.pack(pady=10)

root.mainloop() # closing root