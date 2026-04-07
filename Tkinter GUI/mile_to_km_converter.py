from tkinter import *
from tkinter import Label

# Set up the main window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(250, 100)
window.config(padx = 10, pady = 10)

# Set up the Entry
input = Entry(width=10)
input.grid(row=0, column=1)

# Set up the Text
## 1. Miles
label_1 = Label(text = 'Miles', font= ('Arial', 12))
label_1.grid(row=0, column=2)

## 2. is equal to
label_2 = Label(text = 'is equal to', font= ('Arial', 12))
label_2.grid(row=1, column=0)

## 3. Converted km value
def convert():
    miles = input.get()
    try:
        miles = float(miles)
    except:
        miles = 0
    km = miles * 1.60934
    label_3.config(text=f'{km}')

label_3 = Label(text = '0', font= ('Arial', 12))
label_3.grid(row=1, column=1)

## 4. Km
label_4 = Label(text = 'Km', font= ('Arial', 12))
label_4.grid(row=1, column=2)

# Set up the Button
button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)

window.mainloop()
