#Within loops, there may be a time in which you need to have a condition for exiting a loop early
coins = ('Bronze','Silver','Platinum','Gold')
for coin in coins:
    print ('You possess a', coin, 'coin.')
    if coin == 'Platinum':
        print('Congratulations! You move to the next level!')
        break#break exits the loop
        
