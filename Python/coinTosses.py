import random
print "Starting the program..."

for toss in range(5000):
    random_num = random.random()
    random_num = round(random_num)
    print "Attempt#" + toss + ": Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far"
print "Ending the program, thank you!"


# x = .3456789
# y = .9876544
# x_rounded = round(x)
# y_rounded = round(y)
