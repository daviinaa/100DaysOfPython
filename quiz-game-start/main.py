from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for ques in question_data:
    question_text = ques["text"]
    question_ans = ques["answer"]
    question = Question(question_text, question_ans)
    question_bank.append(question)


quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You have completed the quiz")
print(f"Your final score is {quiz_brain.score}/{len(question_bank)}")