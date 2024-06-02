import os
#allows a programmer to work within the operating system to perform actions
print("Your current directory is:", os.getcwd())
#used to rename and modify a file

os.rename('601-message.txt', 'OLD601-message.txt')

for text_file in os.listdir():#list all files in directory
    if text_file.endswith('.txt'):
        print(text_file)

