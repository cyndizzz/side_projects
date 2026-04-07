from tkinter import *
import random
import string

FONT_NAME = ("Arial", 10)
EMAIL = 'def@gmail.com'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pwd = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
    password_entry.insert(0, pwd)
    print(pwd)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    with open('password.txt', 'a') as file:
        file.write(f'{website} | {username} | {password}\n')

    # Clear up the fields
    website_entry.delete(0, END)
    website_entry.focus()
    username_entry.delete(0, END)
    username_entry.insert(0, EMAIL)
    password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50, bg = 'white')

# Image
canvas = Canvas(window, width = 200, height = 200, bg = "white", highlightthickness = 0)
canvas_img = PhotoImage(file = 'logo.png')
canvas.create_image(100, 100, image = canvas_img)
canvas.grid(row = 0, column = 1)

# Labels
website_label = Label(text = "Website:", font = FONT_NAME, bg = "white")
website_label.grid(row = 1, column = 0)
username_label = Label(text = "Email/Username:", font = FONT_NAME, bg = "white")
username_label.grid(row = 2, column = 0)
password_label = Label(text = "Password:", font = FONT_NAME, bg = "white")
password_label.grid(row = 3, column = 0)

# Entries
website_entry = Entry(width = 38, highlightbackground="white")
website_entry.grid(row = 1, column = 1, columnspan=2)
website_entry.focus()
username_entry = Entry(width = 38, highlightbackground="white")
username_entry.grid(row = 2, column = 1, columnspan=2)
username_entry.insert(0,EMAIL)
password_entry = Entry(width = 21, highlightbackground="white")
password_entry.grid(row = 3, column = 1)

# Buttons
generate_button = Button(text = 'Generate Password', command=generate_password, highlightbackground="white")
generate_button.grid(row = 3, column = 2)
save_button = Button(text = 'Add', width= 36, highlightbackground="white", command = save)
save_button.grid(row = 4, column = 1,columnspan=2)

# Dialog Boxes and Pop-Ups





window.mainloop()