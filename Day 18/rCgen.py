from random import choice


class cgen:

    def GenC():
        a = "#"
        code = "012345678ABCDEF"
        for _ in range(6):
            a += choice(code)

        return a
