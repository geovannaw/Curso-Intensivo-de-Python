class restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " e o nome do restaurante")
        print("tipo de cozinha: " + self.cuisine_type.title())
        print("numero de pessoas servidas: " + str(self.number_served))

    def open_restaurant(self):
        print("o restaurante esta aberto!\n")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

r1 = restaurant('la mafia', 'italiana', '1')
r1.open_restaurant()
r1.describe_restaurant()
r1.set_number_served(2)
r1.describe_restaurant()
r1.increment_number_served(1)
r1.describe_restaurant()



