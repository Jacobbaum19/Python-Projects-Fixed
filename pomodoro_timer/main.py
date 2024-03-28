from tkinter import *
import math

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 45
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
Reps = 0
Timer = NONE

######## Timer Mechanism ########
def start_timer():
    global Reps
    Reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if Reps % 8 == 0 and Reps != 0:
        count_down(long_break_sec)
        print(f"# of Reps: {Reps}")
        window.lift()
        window.attributes('-topmost', True) # Moves the timer to the front of the user's screen
        print("Take a long break!")
    elif Reps % 2 == 0 and Reps != 0:
        count_down(short_break_sec)
        window.lift()
        window.attributes('-topmost', True)
        print(f"# of Reps: {Reps}")
        print("Take a short break!")
    elif Reps > 8:
        window.lift()
        window.attributes('-topmost', True)
        reset_app()
    else:
        count_down(work_sec)
        window.attributes('-topmost', False)
        print(f"# of Reps: {Reps}")
        print("Focus on your work!")
    set_title_text()  # Set the title text after modifying Reps
    update_check_mark() # Adds check mark if a work session was completed

######## Countdown and Reset Mechanisms ########
def count_down(count):
    global Timer
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        Timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# Set title text based on Reps
def set_title_text():
    if Reps % 2 == 0 and Reps != 0 or Reps % 9 == 0 and Reps != 0:
        title_text.config(text="Break Time")
    elif Reps % 2 != 0 and Reps != 0:
        title_text.config(text="Work Time")
    else:
        title_text.config(text="Timer")


# Check mark system
def update_check_mark():
    marks = ""
    work_sessions = math.floor(Reps / 2)
    for _ in range(work_sessions):
        marks += "✅"
    check_marks_txt.config(text=marks)

def reset_app():
    global Timer, Reps
    Reps = 0
    if Timer is not None:
        window.after_cancel(Timer)
    Timer = None
    canvas.itemconfig(timer_text)
    set_title_text()
    update_check_mark()


######## UI Setup ########

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=GREEN)

title_text = Label(text="Timer", font=(FONT_NAME, 36, "bold"), fg=RED, bg=GREEN, highlightthickness=0)
title_text.grid(row=0, column=1)

check_marks_txt = Label(text="", bg=GREEN)
check_marks_txt.grid(row=3, column=1)
check_marks_txt.config(padx=10, pady=10)

start_button = Button(text="Start", font=(FONT_NAME, 12, "bold"), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 12, "bold"), command=reset_app)
reset_button.grid(row=2, column=2)

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(110, 125, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

window.mainloop()
