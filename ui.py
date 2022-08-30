from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Ariel"


class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=50, pady=30, bg=THEME_COLOR)

        self.score_label = Label(
            text=f"Score: 0",
            bg=THEME_COLOR, fg="white",
            font=(FONT_NAME, 15, "bold")
        )
        self.score_label.grid(padx=20, pady=10, row=1, column=2)

        self.canvas = Canvas(width=400, height=300, bg="White")
        self.Question = self.canvas.create_text(200, 150, width=380, text="Question", font=(FONT_NAME, 20, "italic"))
        self.canvas.grid(pady=10, row=2, column=1, columnspan=2)

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, command=self.true_option)
        self.true_button.grid(pady=15, row=3, column=2)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, command=self.false_option)
        self.false_button.grid(pady=15, row=3, column=1)

        self.get_question()
        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz.is_question_remaining():
            self.get_score()
            return self.canvas.itemconfig(self.Question, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.Question, text="You've completed the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def get_score(self):
        score = self.quiz.score
        quiz_len = len(self.quiz.question_list)
        self.score_label.config(text=f"Score: {score}/{quiz_len}")

    def true_option(self):
        is_right = self.quiz.is_correct("True")
        self.give_feedback(is_right)

    def false_option(self):
        is_right = self.quiz.is_correct("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_question)
        
       
