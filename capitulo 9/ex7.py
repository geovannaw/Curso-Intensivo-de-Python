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

class admin(user):
    def __init__(self, name1, name2, age):
        super().__init__(name1, name2, age)
        self.privileges = ["can add post", "cand delete post", "can be user"]
    
    def show_privileges(self):
        print("privileges: ")
        for p in self.privileges: 
            print(p)

admin1 = admin("Geovanna", "Weber", 20)
admin1.show_privileges()