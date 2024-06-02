import sys
"""sys: allows us to import other modules manage files and run comman-line
arguments. The sys library also allows one to work with system-based commands,
such changing file paths and exiting an app
"""
game_lives = 1
while game_lives < 3:
    print("Game in progress")
    game_lives +=1
sys.exit()#end python script
