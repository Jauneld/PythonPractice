capitals=["Montgomery","Juneau","Phoenix"]
capitals.append("Sacramento")
capitals.insert(3, "LittleRock")
capitals.remove("Juneau") #Montgomery, Phoenix, LittleRock, Sacramento
population=[200000,32000,1600000]
capitals[3]="Little Rock"
capitals.sort(reverse=True)
print(capitals.pop(0))
print(capitals)
print(min(population))
print(len(capitals))
#********Error********
#the list will have 2 "Little Rock" because when the element "Juneau" was removed, even thing after 
#it in the list moved down so the index number of "LittleRock" was now two. When the code said to 
#edit index 3 that was not "Little Rock" but "Phoenix" who was now in position 3 due to the removal
