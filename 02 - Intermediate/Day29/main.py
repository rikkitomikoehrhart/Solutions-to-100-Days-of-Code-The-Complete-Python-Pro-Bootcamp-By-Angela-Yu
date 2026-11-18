import os
from tkinter import *
from tkinter import messagebox
import characters
from random import choice, randint, shuffle
import pyperclip

GRAY = "#2e2e2e"
WHITE = "#ffffff"

# ------------------------ PASSWORD GENERATOR --------------------------- #
def generate_password():
    password_entry.delete(0, END)
    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(characters.letters) for _ in range(nr_letters)]
    password_symbols = [choice(characters.symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(characters.numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    new_password = "".join(password_list)

    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)



# -------------------------- SAVE PASSWORD ------------------------------ #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password} \n\nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ----------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title("MyPass")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


# Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)

password_label = Label(text="Password")
password_label.grid(row=3, column=0)


# Entries
website_entry = Entry(width=39)
website_entry.config(bg=GRAY, fg=WHITE, insertbackground=WHITE)
website_entry.grid(row=1, column =1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=39)
email_entry.config(bg=GRAY, fg=WHITE, insertbackground=WHITE)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "rikki.ehrhart@g.austincc.edu")

password_entry = Entry(width=21)
password_entry.config(bg=GRAY, fg=WHITE, insertbackground=WHITE)
password_entry.grid(row=3, column=1)


# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=37, command=save)
add_button.grid(row=4, column=1, columnspan=2)




# Workaround for a macOS Tk bug: the window doesn't draw until it's
# resized,so nudge the size by 1px and back once the window is on screen.
def force_redraw():
    width, height = window.winfo_width(), window.winfo_height()
    window.geometry(f"{width + 1}x{height}")
    window.after(10, lambda: window.geometry(f"{width}x{height}"))

window.after(100, force_redraw)
window.mainloop()