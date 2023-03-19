from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import pickle
from Questionbank import results

question_bank = []
new_questionbank = []

# for q in question_data:
#     q_text = q["text"]
#     q_ans = q["answer"]
#     new_question = Question(q_text, q_ans)
#     question_bank.append(new_question)

for l in results:
    q_text = l["question"]
    q_ans = l["correct_answer"]
    new_question = Question(q_text, q_ans)
    question_bank.append(new_question)

pri = QuizBrain(question_bank)

pri.start()


with open('pri', 'wb') as f:
    pickle.dump(pri, f)
