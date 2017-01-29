
def keyVal(arg):
	for key in arg:
		print key, ":", arg[key]

myDict = {"key1": "value1", "key2": "value2", "key3": "value3"}

keyVal(myDict)


def numbers():
	for i in range(1, 101):
		if i % 3 == 0 and i % 5 == 0:
			print "fizzbuzz"
		elif i % 3 == 0:
			print "fizz"
		elif i % 5 == 0:
			print "buzz"

numbers()
