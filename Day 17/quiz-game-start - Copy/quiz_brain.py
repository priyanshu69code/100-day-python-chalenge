import random
from clear_screan import clr


class QuizBrain:
    def __init__(self, qlist):
        self.life = 3
        self.qnum = 1
        self.score = 0
        self.qlist = qlist
        self.usedquestion = []

    def check(self, qans, ans):
        if qans.lower() == ans.lower():
            self.score += 1
            print("Correct")
            return True
        else:
            self.life -= 1
            print(f"Incorect and your life is {self.life}")
            print(f"The Correct Answer Was {qans}")
            return False

    def nextQuestion(self):
        Question = random.choice(self.qlist)
        while Question in self.usedquestion:
            Question = random.choice(self.qlist)
        self.usedquestion.append(Question)
        return Question

    def isGameover(self):
        return self.life > 0 and self.qnum < 11

    def start(self):
        ans = None
        while self.isGameover():
            q = self.nextQuestion()
            ans = input(f'{self.qnum}. {q.question} (True/False)')
            self.check(q.answer, ans)
            input("Hit Enter for Next Question")
            self.qnum += 1
            clr()
