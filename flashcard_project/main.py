import tkinter as tk
from tkinter import messagebox
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# Read in csv file for flashcards and change it into a dataframe.

flashcard_csv = pd.read_csv("data/combined_python_tkinter_pandas_methods_functions.csv")
default_flashcard_set = pd.DataFrame(flashcard_csv)
user_flashcards = default_flashcard_set

# ------------------------------- Card Logic ------------------------------- #


def change_card():
    """Selects a random row from the DataFrame to update the card displayed on the canvas.
    Uses that same number to apply to the rest of the item configs."""
    global current_card
    current_card = user_flashcards.sample().iloc[0]
    canvas.itemconfig(category, text=current_card["Category"])
    canvas.itemconfig(desc, text=current_card["Description"])
    canvas.itemconfig(answer_for_flashcard, text=current_card["Function/Method"])


def flip_card():
    """Makes a variable called current_image which checks if the image equals 'question_flashcard',
    toggles between the question side and answer side of the flashcard, including changing text content and color to
    suit each side's design"""
    current_image = canvas.itemcget(card_image, "image")
    if current_image == str(question_flashcard_img):
        canvas.itemconfig(card_image, image=answer_flashcard_img)
        canvas.itemconfig(desc, text=current_card["Function/Method"])
        canvas.itemconfig(desc, fill="white")
        canvas.itemconfig(category, fill="white")
    else:
        canvas.itemconfig(card_image, image=question_flashcard_img)
        canvas.itemconfig(desc, text=current_card["Description"])
        canvas.itemconfig(desc, fill="black")
        canvas.itemconfig(category, fill="black")

# ------------------------------- Remove flashcards from user's dataframe ------------------------------- #


def remove_card():
    global user_flashcards
    # Check if the DataFrame is empty before attempting to remove a card
    if len(user_flashcards) == 0:
        # Show message
        messagebox.showinfo(title="Nice Job!", message="You ran out of cards! Restarting program!")
        # Set users cards to default cards to restart the program.
        user_flashcards = default_flashcard_set
        # Start with a new card.
        change_card()
    else:
        # Proceed with removing the card if the DataFrame is not empty
        try:
            if current_card.name in user_flashcards.index:
                # Correctly use the drop method with inplace=True
                user_flashcards.drop(index=current_card.name, inplace=True)
                # Calculate the number of cards left after the removal
                number_of_cards_left = len(user_flashcards)
                print(f"Card removed, you have {number_of_cards_left} left!")
                change_card()
        except KeyError:
            print("Error removing the card. That card index cannot be found.")


# Screen
screen = tk.Tk()
screen.title("Flashy: Flashcards for Python Methods and Functions")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Image
canvas = tk.Canvas(width=800, height=526)
question_flashcard_img = tk.PhotoImage(file="../flashcard_project/images/card_front.png")
answer_flashcard_img = tk.PhotoImage(file="../flashcard_project/images/card_back.png")
x_image = tk.PhotoImage(file="../flashcard_project/images/wrong.png")
checkmark_img = tk.PhotoImage(file="../flashcard_project/images/right.png")

# Canvas
card_image = canvas.create_image(400, 263, image=question_flashcard_img)
category = canvas.create_text(400, 150, text=default_flashcard_set["Category"][0],
                              font=("Times New Roman", 30, "italic"))
desc = canvas.create_text(400, 263, text=default_flashcard_set["Description"][0], font=("Times New Roman", 15, "bold"))

# This line of code is simply added to make it easier when flipping the flash card.
# The answer is off the screen so the user can't see it until it switches position with the desc.
answer_for_flashcard = canvas.create_text(800, 350, text=default_flashcard_set["Function/Method"][0],
                                          font=("Times New Roman", 1, "normal"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
x_button = tk.Button(image=x_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=change_card)
x_button.grid(row=1, column=0)

checkmark_button = tk.Button(image=checkmark_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=remove_card)
checkmark_button.grid(row=1, column=1)

flip_card_button = tk.Button(bg="white", command=flip_card, width=50, text="Click to flip card.")
flip_card_button.grid(row=2, column=0, columnspan=2)

# Call change card to start the program.
change_card()


screen.mainloop()
