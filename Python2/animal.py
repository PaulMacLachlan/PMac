class Animal(object):
    def __init__(self, name="Beast", health=100):
        self.name = name
        print name
        self.health = health
        print health
        print "New Animal!"

    def walk(self):
        print self.health
        health = self.health - 10
        print "Were walking!"
        print health
        return self

    def run(self):
        print "Were running!"
        health = self.health - 5
        print health
        return self

    def displayHealth(self):
        output = 'My name is ' + str(self.name) + '\n' + 'My health is ' + str(self.health) + '\n'
        # return self
        # display on screen the name of the Animal and the health.
        print output

# class DerivedClassName(BaseClassName):

class Dog(Animal):
    def pet(self):
        self.health += 5
        print "Look, a new dog!"
        print "My health is " + str(self.health) + '\n'
        return self

class Dragon(Animal):
    def __init__(self):
        super(Animal, self).__init__()

    def fly():
        self.health -= 10

# Now, create another class called Dragon that also inherits everything from Animal, but 1) have the default health be 170 and 2) add a new method called fly, which when invoked, decreased the health by 10. Have the Dragon walk() three times, run() twice, fly() twice, and have it displayHealth(). When the Dragon's displayHealth function is called, have it say 'this is a dragon!' before it displays the default information (by calling the parent's displayHealth function).


# crow = Animal("Doctor", 50)
# animal = Animal("Animal", 200)
pooch = Dog(76)
dragon = Dragon(500)

def myDog():
    print "This is my Dog!"
    pooch.walk().walk().walk().run().run().pet().displayHealth()

def myCrow():
    print "were doing my crow!"
    crow.walk().displayHealth()

def myAnimal():
    print "this is my Animal"
    animal.walk().walk().walk().run().run().displayHealth()

def myDragon():
    print "This is a Dragon!"
    # Dragon walk() three times, run() twice, fly() twice, and have it displayHealth().
    dragon.walk().walk().walk().run().run().fly().fly().displayHealth()

# myCrow()
# myAnimal()
# myDog()
myDragon()


# Now for the first instance of the animal (instance called 'animal'), try calling fly() or pet() and make sure this doesn't work.  (-:
