#The parentheses supersedes the operator 
#*****Operator hierarchy*******
#Arithmetic <--- Containment <--- Comparison <--- Identity <--- Logical <--- Assignment
#Why first place? we need to solve the problem first
#Containment is 2nd because it is not as specific as the other comparison types: Comparison, identity, logical
x = 5
y = 3
print(x, y)
#it always takes the latest value
#the variable on the left side of the assignment operator (=) is set to teh value on the right
y = x
print(y)
