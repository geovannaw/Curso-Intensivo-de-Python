class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " e o nome do restaurante")
        print("tipo de cozinha: " + self.cuisine_type.title())

    def open_restaurant(self):
        print("o restaurante esta aberto!\n")

r1 = Restaurant('la mafia', 'italiana')
r1.describe_restaurant()
r1.open_restaurant()
r2 = Restaurant('confins', 'churrascaria')
r2.describe_restaurant()
r2.open_restaurant()
r3 = Restaurant('cocole', 'sorveteria')
r3.describe_restaurant()
r3.open_restaurant()
