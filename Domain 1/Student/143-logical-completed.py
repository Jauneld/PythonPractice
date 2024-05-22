#Keywords
#"and": Both criterias are made will produce true
#"not": The value is not found will not this true
#"or": If one of the values are true, the output will be true

#read from "not" ---> "and" ---> "or"
gases = ('Hydrogen','Helium','Nitrogen','Oxygen')
number_of_gases = 11
number_of_liquids = 2

print('Sodium' not in gases and number_of_liquids < number_of_gases)#True

print('Hydrogen' in gases or 'Helium' in gases and number_of_liquids == 4)#True
#the "and" portion ('Helium' in gases and number_of_liquids == 4) is False but 
#When the "or" section is run, ('Hydrogen' in gases or 'Helium' in gases) it was
#true so the statement is overall true. 

print(('Hydrogen' in gases or 'Helium' in gases) and number_of_liquids == 4)#False
#() around the "or" section tells the system to focus on that statment first
#the "or" statement would be true but thhe "and statement would be false so 
#the overall statement would be False
