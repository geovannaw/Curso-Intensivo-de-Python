class user():
    def __init__(self, first_name, last_name, age, gender, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = login_attempts

    def describe_user(self):
        print("nome do usuario: " + self.first_name.title() + " " + self.last_name.title())
        print("idade: " + self.age.title())
        print("genero: " + self.gender.title())

    def greet_user(self):
        print("bem vindo(a) de volta " + self.first_name.title())

    def increment_login_attempts(self, attempts):
        self.login_attempts += attempts
        print("tentativas: " + self.login_attempts)

    def reset_login_attempts(self, login_attempts):
        self.login_attempts = 0

user1 = user('geovanna', 'weber', '20', 'F')
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts(1)

user2 = user('yan', 'vinicius', '23', 'M')
user2.describe_user()
user2.greet_user()