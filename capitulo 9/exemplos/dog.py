class dog():
    def __init__(self, name, age): #inicializa nome e idade
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

my_dog = dog('bolt', 5)
your_dog = dog('prin', 14)

print("o nome do meu cachorro e " + my_dog.name.title() + "." )
print("meu cachorro tem " + str(my_dog.age) + " anos.")
my_dog.sit()

print("\no nome do seu cachorro e " + your_dog.name.title() + ".")
print("seu cachorro tem " + str(your_dog.age) + " anos.")
your_dog.sit()
