import random
from tkinter import *
from tkinter import messagebox
import string

# Constants
Number_Of_Chars = 5


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
password_bank = []
all_letters = list(string.ascii_letters)
password_completed = False


def generate_password():
    generated_password = ""
    for _ in range(Number_Of_Chars):
        generated_password += random.choice(all_letters)
    for _ in range(Number_Of_Chars):
        generated_password += str(random.randint(0, 9))
    generated_password_list = list(generated_password)
    random.shuffle(generated_password_list)
    shuffled_password = ''.join(generated_password_list)
    return shuffled_password


def generate_new_password():
    """Deletes old password and inserts new one after functions is complete."""
    password_entry.delete(0, END)
    new_password = generate_password()
    password_entry.insert(0, new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_entries():
    website = website_entry.get()
    username = email_or_username_entry.get()
    password = password_entry.get()

    is_ok = False

    # Asks the user if it is okay to save their password and username/email.
    if len(website) > 0 and len(password) > 0:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                              f"Email/username: {username}\nPassword: {password} "
                                                              f"\nIs it okay to save?")

    else:
        # Warning that one of the fields is blank.
        warning_message = messagebox.showwarning(title="Error", message="Incorrect: Website or Password is too short.")

    if is_ok:
        # Writes the entries into a new or existing document called saved_passwords.
        with open("saved_passwords", "a") as password_list:
            password_list.write(f"Website: {website}\n")
            password_list.write(f"  Username: {username}\n")
            password_list.write(f"  Password: {password}\n\n")

        # Delete the entries in the UI after
        website_entry.delete(0, END)
        password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


# Screen
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Image
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_or_username_label = Label(text="Email/Username:")
email_or_username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry Boxes
website_entry = Entry(width=42)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_or_username_entry = Entry(width=42)
email_or_username_entry.grid(row=2, column=1, columnspan=2)
email_or_username_entry.insert(index=0, string="Bob.Saget@colostate.edu")

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate", command=generate_new_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_entries)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
