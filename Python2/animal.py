class Animal(object):
    def __init__(self, name="Beast", health=100):
        self.name = name
        self.health = health
        print "New Animal!"

    def walk(self):
        health = self.health - 10
        print "Were walking!"

    def run(self):
        print "Were running!"

    def displayHealth(self):
        output = 'Were printing health info!' + str(self.health) + '\n'
        return output


# walk, run, and displayHealth.

crow = Animal("Doctor", 50)

def myCrow():
    print "were doing my crow!"
    crow.walk().displayHealth()

myCrow()
