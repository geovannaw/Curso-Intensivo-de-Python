from pydoc import describe


class user():
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print("nome do usuario: " + self.first_name.title() + " " + self.last_name.title())
        print("idade: " + self.age.title())
        print("genero: " + self.gender.title())

    def greet_user(self):
        print("bem vindo(a) de volta " + self.first_name.title())

user1 = user('geovanna', 'weber', '20', 'F')
user1.describe_user()
user1.greet_user()

user2 = user('yan', 'vinicius', '23', 'M')
user2.describe_user()
user2.greet_user()