#The parentheses supersedes the operator 
#*****Operator hierarchy*******
#Arithmetic <--- Containment <--- Comparison <--- Identity <--- Logical <--- Assignment
#Why first place? we need to solve the problem first
#Containment is 2nd because it is not as specific as the other comparison types: Comparison, identity, logical
#Containment Operator checks of if a value is contained within a list of values
#it is used most for lists, sets, tuples and dictionaries 
#Contaiment keyword: "in"
large_islands = ["Hokkaido", "Honshu", "Shikoku", "Kyushu"]
island1 = "Hokkaido"
print(island1 in large_islands)#True because it is in the list large_islands
