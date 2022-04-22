from tkinter import *


# Function
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


# Window
window = Tk()
window.title("My First Gooey Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label

my_label = Label(text="I Don't Believe in Labels.", font=("Arial", 24, "bold"))
my_label.config(text="Click that Shit")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="Why am I here?")
button.grid(column=3, row=0)
# Entry

input = Entry(width=10)
print(input.get)
input.grid(column=2, row=2)

window.mainloop()
