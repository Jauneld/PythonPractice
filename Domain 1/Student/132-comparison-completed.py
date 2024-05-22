#The parentheses supersedes the operator 
#*****Operator hierarchy*******
#Arithmetic <--- Containment <--- Comparison <--- Identity <--- Logical <--- Assignment
#Why first place? we need to solve the problem first
#Containment is 2nd because it is not as specific as the other comparison types: Comparison, identity, logical
#Compares 2 values
#Return True or False
#They run left to right and if on part is False, the entire statement is False
x = 5
y = 3
print (x == y)
print (x <= y > 2)
