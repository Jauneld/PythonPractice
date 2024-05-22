#The parentheses supersedes the operator 
#*****Operator hierarchy*******
#Arithmetic <--- Containment <--- Comparison <--- Identity <--- Logical <--- Assignment
#Why first place? we need to solve the problem first
#Containment is 2nd because it is not as specific as the other comparison types: Comparison, identity, logical
# Logical operator
#Logical keywords: not, if, or, and, else
#"not" takes Presedence over "and" & "or" because it only requires one value to check is the the statment
#meets the criteria, "and" & "or" require 2 values
#The parentheses supersedes the operator 
#*****Logical keywords hierarchy*******
#not ---> and ---> or 
unlock_level = True
target_score = 10000
score = 8000
if score < target_score or not unlock_level:
    print("You still have some goals to make")
else:
    print("Goals met")
