coins = 5
games = 0
try:#cant run by its self w/o except and finally
    result = coins/games
except:# to catch execeptions. only runs if the try causes a runtime error
    print('This did not work. Did you to divide by zero?')
else:#if there is a correct value. runs if try is succesful. except block is needed for the else block
    print('You are averaging', coins/games, 'coins per game.')
finally:#run reguardless
    print('Thank you for playing')
