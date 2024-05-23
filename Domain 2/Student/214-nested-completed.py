#Defined variables
coins = ['Bronze', 'Silver', 'Gold','Platinum']
coin = 'Bronze'
score = 10000

#nested if statement
if score > 10000:#is the score greater than 10000
    if coin in ('Gold','Platinum'):#if true, is the coin that the player has in the list 
        print("You have reached level 3")#if true, the player is at level 3
    else:
        print("You have reached level 2")#if false, the player is at level 2
elif score > 5000 and coin in coins:#if the inital if statement was false, if score is greater than 5000 and the coin that the playe has in the list coins
    print("You have reached level 1. Keep going")#if true, the player is at level 1
else:#if everything is false
    print("Increase your score and collect coins to move up")#this will print 
