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
        print "Were printing health info!" + str(self.health)


# walk, run, and displayHealth.

crow = Animal()

crow.walk()displayHealth()
