class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    # returns True if there are questions left otherwise returns False
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # increases the question number and moves to the next question
    # takes the users answer and uses the check_answer method
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    # puts both the user answer and correct answer to lower case, then compares to see if they are the same
    # if both the user answer and correct answer are the same the score increases by 1
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


