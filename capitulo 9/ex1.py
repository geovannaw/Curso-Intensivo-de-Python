class restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " e o nome do restaurante")
        print("tipo de cozinha: " + self.cuisine_type.title())

    def open_restaurant(self):
        print("o restaurante esta aberto!\n")

r1 = restaurant('la mafia', 'italiana')
r1.describe_restaurant()
r1.open_restaurant()
