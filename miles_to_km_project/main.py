from tkinter import *

# Screen
window = Tk()
window.title("Mile to Km Convertor")
window.minsize(width=500, height= 300)
window.config(padx=50, pady=50)
window.config(bg="#ADD8E6")  # Set light blue background color

# Entry box to convert miles to km. User can type immediately without clicking on the box with focus().
miles_entry = Entry(window, bg="white", fg="black", font=("Times New Roman", 12))
miles_entry.grid(row=0, column=1, padx=10, pady=10)
miles_entry.focus()

# Miles label next to it
miles_label = Label(window, text="Miles", font=("Times New Roman", 12, "bold"), bg="#ADD8E6")
miles_label.grid(row = 0, column= 2)

# is equal to label...
is_equal_to_label = Label(window, text="is equal to", font=("Times New Roman", 12 , "normal"), bg="#ADD8E6")
is_equal_to_label.grid(row = 1, column= 0)

# Label to display converted value
converted_label = Label(window, text="", font=("Times New Roman", 12, "normal"))
converted_label.grid(row=1, column=1)

# Button actions below...
# Calculates miles to km except when nothing is typed out, which returns a blank value.
# Importing modules with Tkinter is a bit different from past lessons so no OOP for this project.


def calculate_button():
    try:
        miles = float(miles_entry.get())
        km = miles * 1.60934
        converted_label.config(text=f"{km:.2f} Km")
    except ValueError:
        converted_label.config(text="Please enter a valid number for miles.")


def clear_button():
    miles_entry.delete(0, END)
    converted_label.config(text="")


# Calc button below
cal_button = Button(window, text="Calculate", command=calculate_button)
cal_button.grid(row= 3, column= 1)

# Clear Button
clear_button = Button(window, text="Clear", command=clear_button)
clear_button.grid(row=2, column=2)



window.mainloop()
