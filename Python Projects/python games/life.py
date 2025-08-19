import tkinter as tk

# Intro
intro = [
    "Damn!",
    "You wake up from a nightmare, but your vision is pitch black",
    '"Hello?"',
    "A sudden shhh comes into the corner of my hearing senses"
]
current_line = 0
# def to proceed to the next line
def next_line(event=None):
    global current_line
    if current_line < len(intro):
        # new line every enter
        new_label = tk.Label(frame, text=intro[current_line], fg="white", bg="black", anchor="w")
        new_label.pack()
        new_label = tk.label(frame, text=intro[current_line])
     label.config(text=intro[current_line])
      current_line += 1
    else:
        label.config(text="(End of Dialogue)")



# create window
gui = tk.Tk()
gui.title("Hello World")
gui.geometry("1280x800")
gui.config(background='black')



# bind enter key
gui.bind("<Return>", next_line)


gui.bind("<Key>")
# GUI run
gui.mainloop()
