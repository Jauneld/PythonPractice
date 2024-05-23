coins = ('Bronze','Silver','Platinum','Gold')
for coin in coins:
    if coin == 'Platinum':
        print('Congratulations! The platinum coin will move you to the next level!')
        continue#skips an iteration of a loop
    print ('You possess a', coin, 'coin.')
