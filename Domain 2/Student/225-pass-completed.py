#pass: it doesn't break out of a loop or pause a loop. it pass a set of code
coins = ('Bronze','Silver','Platinum','Gold')
for coin in coins:
    
    if coin == 'Platinum':
        pass# allows people to bulid parts of code without info and continue to structure code w/o waiting
        continue
    print ('You possess a', coin, 'coin.')
