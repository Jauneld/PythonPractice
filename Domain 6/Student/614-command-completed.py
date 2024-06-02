import sys
#sys.argv[0]: always filename in python
filename = sys.argv[1]#used as a placeholder for a command-line argument
#the file being open and read
print (f" {filename} has been specified.")

with open (filename, 'r') as file:
    content = file.read()
    print(content)

