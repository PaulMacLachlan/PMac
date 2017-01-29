import random
# dict = {}
# list = []
# 	for x in range(0, 100):
# 	dict[1] = x
# 	list.append(dict)
# 	dict = {}

# print list



session = {}
session['activities'] = []

gold = random.randint(10,20)
# session['current_gold'] = session['current_gold'] + gold
activity_text = "My String"
print activity_text
session['activities'].append(activity_text)
print type(session['activities'])
print session['activities']
