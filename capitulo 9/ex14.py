from random import randint

class Die():
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))

print("dado 1: ")
dado = Die(6)
for k in range(10):
    dado.roll_die()

print("dado 2: ")
dado2 = Die(10)
for k in range(10):
    dado.roll_die()

print("dado 3")
dado3 = Die(20)
for k in range(10):
    dado.roll_die()





