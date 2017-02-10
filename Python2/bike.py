class Bike(object):
    def __init__(self, miles=0):
        self.price = 200
        self.max_speed = "25mph"
        self.miles = miles
        self.color = "Black"
        # return self
        print "New Bike!"

    def displayInfo(self):
        # print self.price
        print self.price , "is my price!"
        print self.max_speed , "is my max speed!"
        print self.miles , "is my mileage!"
        return self

    def riding(self):
        print "Riding"
        self.miles += 10
        print self.miles
        return self

    def reverse(self):
        print "Reversing"
        self.miles -= 5
        print self.miles
        return self

fixie = Bike(40)
# print fixie.miles, fixie.price
mounty = Bike(700)
# print bike2.miles, bike2.color
tricycle = Bike(10)

def fixie_does_it():
    print "* * * Lets take the Fixie for a trip!"
    fixie.riding().riding().riding().reverse().displayInfo()

def mounty_does_it():
    print "* * * Lets take Mounty for a spin!"
    mounty.riding().riding().reverse().reverse().displayInfo()

def tri_does_it():
    print "* * * Dont forget my Tricycle!"
    tricycle.reverse().reverse().reverse().displayInfo()
#     # how best to perform these functions multiple times?
#     #how best to deal with not going past negative mileage?
#     # if tricycle.self.miles > 5
#     #     tricycle.reverse
#     #
#     # else return False
#     #     print "Were back at zero, we cant reverse anymore!"


print "I WANT TO RIDE MY BIIIIICICLE, BIIIIICICLE, BIIIIICICLE!"

fixie_does_it()
mounty_does_it()
tri_does_it()

# def ride(self, num):
#         print "Riding {}".format(self.name)
#         self.miles = self.miles + 10
#         if num >= 1:
#             self.miles = self.miles * num
#             return self.miles
#         else:
#             return self.miles
