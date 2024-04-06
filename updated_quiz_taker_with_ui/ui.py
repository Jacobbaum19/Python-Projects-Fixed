from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    """This class contains all the UI for the quiz and the logic for changing the screen color."""
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Window
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Score label
        self.score_label = Label(text="Score: 0", font=("Times New Roman", 15, "normal"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125,
            text="",
            width=200,
            fill=THEME_COLOR,
            font=('Arial', 12, 'italic')
        )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=50, pady=50)
        # Loaded images
        check_mark_img = PhotoImage(file="images/true.png")
        x_img = PhotoImage(file="images/false.png")

        # Buttons
        self.check_mark_button = Button(image=check_mark_img, highlightthickness=0, bg=THEME_COLOR,
                                        command=self.true_pressed)
        self.check_mark_button.grid(row=2, column=0, padx=15, pady=15)
        self.x_button = Button(image=x_img, highlightthickness=0, bg=THEME_COLOR, command=self.false_pressed)
        self.x_button.grid(row=2, column=1, padx=20, pady=20)
        # Changes the text to the first question the quiz.
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """This function turns the screen white immediately and reactivates the user buttons. If enough
        questions still remain (less than 10 with the current code) it will replace the canvas with the
        next question."""
        self.canvas.config(bg="white")
        self.x_button.config(state="active")
        self.check_mark_button.config(state="active")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have reached the end of the quiz, "
                                                            f"your score is {self.quiz.score}/10")
            self.x_button.config(state="disabled")
            self.check_mark_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """If the correct answer matches the user's answer for the quiz_brain, the screen will change
        accordingly is_right is a boolean that will return true or false. It will then use that value
        the logic below."""
        if is_right:
            self.canvas.config(bg="green")
            self.x_button.config(state="disabled")
            self.check_mark_button.config(state="disabled")
        else:
            self.canvas.config(bg="red")
            self.x_button.config(state="disabled")
            self.check_mark_button.config(state="disabled")
        self.window.after(1000, self.get_next_question)
