from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)

# Label
my_label = Label(text="I AM a Label", font= ('Arial', 24, 'bold'))
my_label.pack()     # pack the label into the window
my_label['text'] = "My Text"
my_label.place(x=100, y=100)

# Button
i=0
def button_clicked():
    txt = input.get()
    my_label.config(text=txt)

button = Button(text = 'Click me', command = button_clicked)
button.pack()

# Entry
input = Entry(width = 10)
input.pack()
print(input.get())

# Spinbox/Scale/Checkbutton/Radiobutton/Listbox


window.mainloop()