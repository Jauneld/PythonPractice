# rating is supposed to be a whole number
#default data type for a variable is a string
rating = float(input("Enter a rating between 1 and 5"))#converting data type from string to a float
points = int(rating) * 100#converting data type from string to a integer
print("You have " + str(points) + " to start.")#converting data type from integer to a string
