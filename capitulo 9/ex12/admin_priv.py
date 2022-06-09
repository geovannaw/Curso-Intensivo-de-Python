from user import user

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
