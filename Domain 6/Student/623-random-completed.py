import random 
for i in range(10):
    print(random.randrange(6,20,2))#returns a number between the first number and the last number - 1 
    print(random.randint(1,20))#returns a number between the first number and the last number
    x = random.random()#return a floating point decimal between 0 - 1
    if x >= .75:
        print("Bonus")
