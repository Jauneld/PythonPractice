#nested loop: having one loop inside of another
game_state = True
game_lives = 1
while game_lives <= 3:#change to <= from <so they loop through on the 3rd life
    for i in range(10):#want to go through to 10 not 9 so the range is changed from (10) to (1,11)
        print("You have reached position", i, "in game life", game_lives)
    if game_state == True:
        game_lives +=1
print("Thank you for playing.")
