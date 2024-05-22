#The parentheses supersedes the operator 
#*****Operator hierarchy*******
#Arithmetic <--- Containment <--- Comparison <--- Identity <--- Logical <--- Assignment
#Why first place? we need to solve the problem first
#Containment is 2nd because it is not as specific as the other comparison types: Comparison, identity, logical
#Identity: Determines if 2 variables share the same memory location so they are equal
#identity keywords: "is" 

team1 = {"color":"red", "rank":1}
team2 = team1
team3 = {"color":"red", "rank":1}

print(team1 is team2)#True because Team2 has been made equal to Team1 so they share the same memory space
print(team1 is team3)#False because Team3 is a new variable with its own values so it doesn't share the same memory space

