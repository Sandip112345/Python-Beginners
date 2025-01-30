class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

l = Number(1)
m = Number(2)

print(l + m)