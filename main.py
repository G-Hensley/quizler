from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Create a question bank
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create a quiz brain and pass in the question bank
quiz = QuizBrain(question_bank)

# Create a quiz interface and pass in the quiz brain
interface = QuizInterface(quiz)

