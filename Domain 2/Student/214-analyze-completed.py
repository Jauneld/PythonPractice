coins = ['Bronze', 'Silver', 'Gold','Platinum']
coin = 'Gold'#change the title case from common to capital
score = 10000

if score >= 10000:#change to greater than or equal
    if coin in ('Gold','Platinum'):
        print("You have reached level 3") #expected
    else:
        print("You have reached level 2")
elif score > 5000 and coin in coins:
    print("You have reached level 1. Keep going")
else:
    print("Increase your score and collect coins to move up")

#the score variable has a value of 10000 which is not greater than 10000 so it will not be true
#the value 'gold' is not the same as the because they have different cases than the item in the list
