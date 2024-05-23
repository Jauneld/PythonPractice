#important when speed is vital. Mostly used in games
#keywords
#"is": Do the varaibles share the same memory space?
team1 = {"color":"red", "rank":1}
team2 = team1#team2 is assigned the value of team1
team3 = {"color":"red", "rank":1}

print(team1 is team2)
print(team1 is team3)#Identity ~ False
print(team1 == team3)#Comparison ~ True



