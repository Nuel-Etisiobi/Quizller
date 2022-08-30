import html


class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_position = 0
        self.score = 0
        self.current_question = None

    def is_question_remaining(self):
        return self.question_position < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_position]
        self.question_position += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q{self.question_position}: {q_text}"

        # user_answer = input(f"Q{self.question_position}: {q_text} (True/False): ")
        # self.is_correct(user_answer)

    def is_correct(self, user_choice) -> bool:
        correct_answer = self.current_question.answer
        if user_choice == correct_answer:
            self.score += 1
            return True
        else:
            return False
