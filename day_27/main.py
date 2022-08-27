from tkinter import *

window = tkinter.TK()

window.mainloop()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=2)
my_label.config(padx=100, pady=200)

# Button

def button_clicked():
    new_text = my_input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me!", command=button_clicked)
button.grid(column=2, row=0)

# Entry

my_input = Entry()
my_input.grid(column=3, row=2)

