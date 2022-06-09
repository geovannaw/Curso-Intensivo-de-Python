class user():
    def __init__(self, name1, name2, age):
        self.first_name = name1
        self.last_name = name2
        self.age = age

    def describe_user(self):
        print("nome completo do usuário é", self.first_name.title(), self.last_name.title())
        print("e sua idade é", self.age)

    def greet_user(self):
        print("Seja bem vindo", self.first_name.title())
        print("\n")

class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "cand delete post", "can be user"]
    
    def show_privileges(self):
        print("privileges: ")
        for priv in self.privileges: 
            print(priv)

class admin(user):
    def __init__(self, name1, name2, age):
        super().__init__(name1, name2, age)
        self.privileges = Privileges()


admin1 = admin("Geovanna", "Weber", 20)
admin1.privileges.show_privileges()

