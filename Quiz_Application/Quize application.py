"""
Quiz Application
-----------------
A simple console-based multiple-choice quiz.

Features:
- Stores a list of questions, each with 4 options and a correct answer.
- Displays one question at a time.
- Accepts and validates the user's answer (A/B/C/D).
- Keeps track of the score as the user progresses.
- Displays the final score and a performance message at the end.
"""

import time


class Question:
    """Represents a single multiple-choice question."""

    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options            # dict like {"A": "...", "B": "...", ...}
        self.correct_option = correct_option.upper()

    def is_correct(self, user_answer):
        return user_answer.strip().upper() == self.correct_option


class Quiz:
    """Manages the flow of the quiz: asking questions, scoring, and results."""

    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.total = len(questions)

    def ask_question(self, index, question):
        print(f"\nQ{index + 1}. {question.text}")
        for key in sorted(question.options.keys()):
            print(f"   {key}) {question.options[key]}")

        while True:
            answer = input("Your answer (A/B/C/D): ").strip().upper()
            if answer in question.options:
                return answer
            print("Invalid choice. Please enter one of:", ", ".join(question.options.keys()))

    def run(self):
        print("=" * 50)
        print("           WELCOME TO THE QUIZ APP")
        print("=" * 50)
        print(f"There are {self.total} questions. Good luck!\n")
        time.sleep(1)

        for index, question in enumerate(self.questions):
            user_answer = self.ask_question(index, question)
            if question.is_correct(user_answer):
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {question.correct_option}) "
                      f"{question.options[question.correct_option]}")

        self.show_result()

    def show_result(self):
        print("\n" + "=" * 50)
        print("                 QUIZ COMPLETED")
        print("=" * 50)
        percentage = (self.score / self.total) * 100
        print(f"Your Score: {self.score}/{self.total} ({percentage:.2f}%)")

        if percentage >= 80:
            print("Excellent! Great job!")
        elif percentage >= 50:
            print("Good effort! Keep practicing.")
        else:
            print("Keep trying! You'll do better next time.")
        print("=" * 50)


def load_questions():
    """Returns a list of Question objects. Add/edit questions here."""
    questions_data = [
        {
            "text": "What is the capital of France?",
            "options": {"A": "Berlin", "B": "Madrid", "C": "Paris", "D": "Rome"},
            "correct": "C",
        },
        {
            "text": "Which language runs natively in a web browser?",
            "options": {"A": "Python", "B": "C++", "C": "Java", "D": "JavaScript"},
            "correct": "D",
        },
        {
            "text": "What does 'CPU' stand for?",
            "options": {
                "A": "Central Processing Unit",
                "B": "Computer Personal Unit",
                "C": "Central Process Utility",
                "D": "Control Processing Unit",
            },
            "correct": "A",
        },
        {
            "text": "Which data structure uses FIFO (First In First Out)?",
            "options": {"A": "Stack", "B": "Queue", "C": "Tree", "D": "Graph"},
            "correct": "B",
        },
        {
            "text": "In Python, which keyword is used to define a function?",
            "options": {"A": "func", "B": "def", "C": "function", "D": "lambda"},
            "correct": "B",
        },
    ]

    return [Question(q["text"], q["options"], q["correct"]) for q in questions_data]


def main():
    questions = load_questions()
    quiz = Quiz(questions)
    quiz.run()


if __name__ == "__main__":
    main()