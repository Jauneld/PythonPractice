#whitespace is used so separating code blocks so it has better readablility
#doesn't normally affect code
game_state = True
game_lives = 1

while game_lives <= 3:
    for i in range(1,11):
        print(f"You have reached position {i} in game life {game_lives}")#there cant be a space between the f and the string
    if game_state == True:
        game_lives += 1
        
print("Thank you for playing.")
