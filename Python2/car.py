class Car(object):
    def __init__(self, speed, fuel, mileage, price=20000, location='Detroit'):
        self.speed = 200
        self.fuel = 'empty'
        self.mileage = 32000
        self.price = price
        self.location = location
        self.tax = 0.15 if price >= 10000 or location == 'California' else 0.12
        print "Its a brand new carrrr!" + "\n"
        # return Car.display_all()

    def display_all(self):
        output = 'Speed: ' + str(self.speed) + '\n'
        output += 'Fuel: ' + str(self.fuel) + '\n'
        output += 'Mileage: ' + str(self.mileage) + '\n'
        output += 'Price: ' + str(self.price) + '\n'
        output += 'Location: ' + str(self.location) + '\n'
        output += 'Tax: ' + str(self.tax) + '\n'
        return output

car1 = Car(280, 'Full', 3000, 9999, "California")
car2 = Car(110, 'full', 0, 22000, "Vacaville")
car3 = Car(120, '50%', 10000, 5000, "Seattle")
car4 = Car(300, 'Full', 5500, 30000, "Denver")
car5 = Car(25, 'Empty', 530, 1999, "Los Angeles")
car6 = Car(65, '1/4 tank', 420, 3100, "New York")

print car1.display_all()
print car2.display_all()
print car3.display_all()
print car4.display_all()
print car5.display_all()
print car6.display_all()


# class Parent(object): # inherits from the object class
#   # parent methods and attributes here
# class Child(Parent): #inherits from Parent class so we define Parent as the first parameter
#   # parent methods and attributes are implicitly inherited
#   # child methods and attributes
