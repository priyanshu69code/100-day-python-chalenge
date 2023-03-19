from question_model import Question
from data import question_data
from quiz_brain import quiz


question_bank = []

for q in question_data:
    q_text = q["text"]
    q_ans = q["answer"]
    new_question = Question(q_text, q_ans)
    question_bank.append(new_question)

score = 0
life = 3
qu_num = 1

quiz = quiz(question_bank)


while (life > 0 and qu_num <= 10):
    choice = quiz.next_question(qu_num)
    if quiz.check(choice):
        score += 1
        print(f"You Score :: {score}")
    else:
        print("Wrong Answer")
        life -= 1
        print(f"You life :: {life}")
    qu_num += 1

print("Game Over")
