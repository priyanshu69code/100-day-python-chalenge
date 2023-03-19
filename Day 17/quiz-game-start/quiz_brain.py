import random


class quiz:

    def __init__(self, q_list):
        self.q_list = q_list
        self.used_question = []
        self.l = ""

    def next_question(self, num):
        q = random.choice(self.q_list)
        while q in self.used_question:
            q = random.choice(self.q_list)
        self.used_question.append(q)
        self.l = q
        print(q.answer)
        choice = input(f"{num} .. {q.question}(True/False)")
        return choice

    def check(self, ans):
        if self.l.answer == ans:
            return True
        else:
            return False
