class Bike(object):
    def __init__(self, miles=0):
        self.price = 200
        self.max_speed = "25mph"
        self.miles = miles
        self.color = "Black"
        print "New Bike!"

    def displayInfo(self):
        # print self.price
        print self.price , "is my price!"
        print self.max_speed , "is my max speed!"
        print self.miles , "is my mileage!"

    def riding(self):
        print "Riding"
        self.miles += 10
        print self.miles

    def reverse(self):
        print "Reversing"
        self.miles -= 5
        print self.miles

fixie = Bike(40)
# print fixie.miles, fixie.price
mounty = Bike(700)
# print bike2.miles, bike2.color
tricycle = Bike(10)

print "I WANT TO RIDE MY BIIIIICICLE, BIIIIICICLE, BIIIIICICLE!"

def fixie_does_it():
    # how best to perform these functions multiple times?
    fixie.riding()
    fixie.riding()
    fixie.riding()
    fixie.reverse()
    fixie.displayInfo()

fixie_does_it()

def mounty_does_it():
    # how best to perform these functions multiple times?
    mounty.riding()
    mounty.riding()
    mounty.reverse()
    mounty.reverse()
    mounty.displayInfo()

mounty_does_it()

def tri_does_it():
    # how best to perform these functions multiple times?
    #how best to deal with not going past negative mileage?
    # if tricycle.self.miles > 5
    #     tricycle.reverse
    #
    # else return False
    #     print "Were back at zero, we cant reverse anymore!"
    tricycle.reverse()
    tricycle.reverse()
    tricycle.reverse()
    tricycle.displayInfo()

tri_does_it()

# Have the third instance reverse three times and displayInfo().




def ride(self, num):
        print "Riding {}".format(self.name)
        self.miles = self.miles + 10
        if num >= 1:
            self.miles = self.miles * num
            return self.miles
        else:
            return self.miles
