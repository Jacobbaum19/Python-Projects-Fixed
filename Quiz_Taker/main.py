"""Importing data from question data, Question and Quiz Brain.
Question formats the question and Quiz Brain has 2 methods, still_has_question checks if the
quiz is over and next_question asks the question and adds a +1 after every question answered. """

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data["results"]:
    """This gets the text and answer to send over to the QuizBrain class. Basically making it global."""
    question_text = question["question"]
    question_answer = question[("correct_answer")]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

# Notes for self: Use the (.) to call methods from a class
while quiz.still_has_questions():
    quiz.next_question()

"""End of the quiz."""
print("You've completed the quiz!")
print(f"Your final score was: {quiz.q_score}/{quiz.q_number} ")
