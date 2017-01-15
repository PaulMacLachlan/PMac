# Create a function called 'multiply' that reads each value in the list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
#
# The function should multiply each value in the list by the second argument. For example, let's say:
#
# a = [2,4,10,16]
# Then:
# b = multiply(a, 5)
# print b
# Should print [10, 20, 50, 80 ].


def multiply(list,num): #defines the function to accept list and num params
    newList = [] #declares our "new list"
    for idx in list: #iterates over each item in the given list
        newList.append(idx * num) #appends the multiplied data to the newList
    print newList #prints our output

# multiply([2,4,10,16],5)
multiply([3,6,8,9],2)
