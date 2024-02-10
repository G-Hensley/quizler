from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=30, pady=30, bg=THEME_COLOR)

        self.true_img = PhotoImage(file="images/true.png", height=97, width=100)
        self.false_img = PhotoImage(file="images/false.png", height=97, width=100)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="Some question.",
                                                     fill=THEME_COLOR, font=("Arial", 20, "italic"),
                                                     width=280)
        self.canvas.grid(row=1, columnspan=2, column=0, pady=50)

        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, foreground="white",
                                 font=("Arial", 10))
        self.score_label.grid(row=0, column=1)

        self.true_button = Button(image=self.true_img, highlightthickness=0,
                                  command=self.clicked_true)
        self.false_button = Button(image=self.false_img, highlightthickness=0,
                                   command=self.clicked_false)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.score}", bg=THEME_COLOR, foreground="white")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.canvas.config(bg="white")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def clicked_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def clicked_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score += 1
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
