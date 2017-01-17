# users is a dictionary with 2 lists of subsequent dictionaries.
# the first key is STUDENTS, and its VALUE is a LIST of 4 DICTIONARIES.
# the second key is INSTRUCTORS and its VALUE is a LIST of 2 DICTIONARIES.

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def printNames(a, b):
	print b
	for x in range(len(a)):
		full_name = a[x]['first_name'] + " " + a[x]['last_name']
		print (x + 1), "-", full_name, "-", (len(full_name) - 1)

students = users['Students']
instructors = users['Instructors']


printNames(students, 'Students')
#printNames(instructors, 'Instructors')
