#doc string are used to document modules, objects, functions, classes
#doc string vs comment 
#doc string: located in triple quotation marks""", can go for mulitple lines, can be printed using print(__doc__)
#function: uses #, only for one line, can't be printed

"""Hello [user]
"""
items = ['Wand', 'Rock', 'Pogo Stick']
levels = [1, 2, 3]
print(__doc__)
for level in levels:
    for item in items:
        if level == 2 and item == 'Rock':
            continue
        else:
            print(f"You can get a {item} at level {level}.")
