class car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self .odometer_reading = 23
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make+ ' ' + self.model 
        return long_name.title()

    def read_odometer(self):
        #mostrar a milhagem do carro
        print("this car has " + str(self.odometer_reading) + " miles on")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer")
    #caso compre um caso usado, somar o q vc andou com o q ja tinha
    def increment_odometer(self, miles):
        #soma  a qnt ao odometro
        self.odometer_reading += miles

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("this car has a "+ str(self.battery_size) + "-kwh") 
    
    def get_range(self):
        if self.battery_size == 70:
            range=  240
        elif self.battery_size == 85:
            range=  270
        message = "this car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    
    def upgrate_battery(self, newB):
        if newB != 70 or newB != 85:
            self.battery_size = 85
        

class eletricCar(car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year) #ou super(eletricCar, self).__init__(make, model, year)
        self.battery = Battery()
    
    def describe_battery(self):
        #descreve a capacidade da bateria
        print("this car has a " + str(self.battery_size) + "-kwh battery.")


my_tesla = eletricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery();
my_tesla.battery.get_range()
#capacidade da bateria default 
my_tesla.battery.upgrate_battery(10)
my_tesla.battery.describe_battery();
my_tesla.battery.get_range()
