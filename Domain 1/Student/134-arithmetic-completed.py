#The parentheses supersedes the operator 
#*****Operator hierarchy*******
#Arithmetic <--- Containment <--- Comparison <--- Identity <--- Logical <--- Assignment
#Why first place? we need to solve the problem first
#Containment is 2nd because it is not as specific as the other comparison types: Comparison, identity, logical
#Arithmetic: Remember PEMDAS
base = 4000
rank = 3
bonus = 500

total_score = (base + bonus) * rank
print(total_score)
