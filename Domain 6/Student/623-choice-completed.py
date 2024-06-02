import random
categories = ['Acids','Bases','PH Numbers']
category = random.choice(categories)#one element from the list
category2 = random.sample(categories,2)#return mulitiple random values from a list(listName,amt to retreive)
print(category)
print(category2)
