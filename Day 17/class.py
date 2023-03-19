class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.followers = 0
        self.followings = 0

    def follow(self, user):
        user.followers += 1
        self.followings += 1


u1 = User("Priyanshu", 21832)
u2 = User("Ben", 10)

u1.follow(u2)

print(u2.followers)
