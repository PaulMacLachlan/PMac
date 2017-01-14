# Build a function that takes in a list of numbers and a value. Multiply each number in the list by the value given and return the updated list.
def multiply(list, val):
    for i in range(len(list)):
        list[i] = list[i] * val
    return list

x = multiply([10, 20, 30], 5)
print x
