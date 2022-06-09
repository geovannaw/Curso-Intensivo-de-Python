class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("restaurant's name is", self.name.title())
        print("cuisine type is", self.cuisine_type)

    def open_restaurant(self):
        print(self.name.title(),"'s restaurant is open")

class iceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ['creme', 'chocolate', 'misto']

sorveteria = iceCreamStand("gelatto", "ice cream")
sorveteria.describe_restaurant()
print("flavors: ")
for sabor in sorveteria.flavors:
    print(sabor)