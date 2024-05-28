#"string".format: allows one to control the text spacing in on statement using whatever variables should be in the statement 
score = 200000
level = 3
player1 = "Stacey"

print("Player1:", player1, "Score:", score, "Level:", level)
print("{} has {} points and has reached level {}".format(player1, score, level))
print("{2} has {0} points and has reached level {1}".format(score, level, player1))
print(f"{player1} has {score} points and has reached level {level}")
print(f"{player1:<15} {score:>10}")#:<num: take num spaces and be left aligned
#:>num: take num space and be right aligned
#f"(string)" allows you to embed expressions or variables directly within a string, making concatentation and format easier 
#{} placeholder for the info
#if you put the index number in the curly bracket, you can put anything from any location
#.format(1,2,3): place in the order that would like to be displayed 

print("Player1: %1s Score: %.2f" %(player1, score))
#%1s = one space after the word 
#%.2f = 2 decimal points should be shown for the score value
#d = whole number
#s = space
#f = float
