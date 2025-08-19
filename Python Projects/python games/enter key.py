import tkinter as tk

# gui window
gui=tk.Tk()
gui.geometry('1280x800')
gui.configure(background='black')
gui.title("enter key")

# enter press
def on_enter(event):
    label.config("Enter pressed") # !!!!! To display text on tkinter use label.config. !!!!!

label = tk.Label(gui, text="Press Enter", font=("Arial", 19))
label.pack(pady=20)

# binding enter
gui.bind('<Return>', on_enter)

# gui loop
gui.mainloop()