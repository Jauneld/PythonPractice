#a period(.) serves as the "assessor" that allows the programmer to use a method like a toolbox
#methods are functions that are tied to a specific object and are invoked using the period notation
capitals=["Montgomery","Juneau","Phoenix"]
#object(toolbox).method(tool)("....")
capitals.append("Sacramento")#add something to a list, at the end
capitals.insert(3, "LittleRock")#to add an element to the list in a specific index
#object(toolbox).method(tool)(index,"...")
capitals.remove("Juneau")
population = [200000,32000,1600000]
capitals[2]="Little Rock"
capitals.reverse()#make the list in descending order  
print(capitals)
capitals.sort(reverse=True)#reverse alphabetical order. The argument (reverse=True) did that
print(capitals)
print(capitals.pop())#Last item of on the list is removed and shows what that element is
print(capitals.pop(0))#With the pop method you can specify what index should be removed 
print(capitals)
print(max(population))#displays the greatest number in the list population
print(min(population))#displays the smallest number in the list population
print(len(capitals))#displays the length of the list capitals
