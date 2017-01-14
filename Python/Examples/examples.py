my_string = "This is a string stored in the my_string variable"
my_num = 5 # an integer stored in a variable
my_tuple = (1,2,3,4,5) # a tuple stored in a variable
# a dictionary stored in a variable
my_dictionary = {'name': 'Michael Choi', 'fave_lang': 'Python', 'level': 'Sensei'}

greetings = "Hello Ninja!"
print greetings

# print "What is your name?"
# #name = raw_input()
# print "How old are you?"
# age = 40
# print "You are", age, "years old"
# #age = raw_input()
# name = "Paul"
# print "My name is " + name

first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name, last_name)

greeting = "HellO WorlD!"
print greeting.upper()

my_string = "hello world"
print my_string.find("ld")



x = [99,4,2,5,-3]
print x[:]
#the output would be [99,4,2,5,-3]
print x[0:]
#the output would be [99,4,2,5,-3]
print x[:4]
#the output would be [99,4,2,5]
print x[2:4]
#the output would be [2,5]
