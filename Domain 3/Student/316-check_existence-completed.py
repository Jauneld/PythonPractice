import os#libraries add bulit in functions that we can uses to complete tasks within our code

if not os.path.exists('316-message.txt'):#exists is a method of the path function that is in the os library 
    message = open('316-message.txt','w')
    message.write('Testing file for player configuration\n')
    message.write('Testing file for player score')
    print("Configuration file made")
    message.close()
else: 
    message_test = open('316-message.txt','r')
    content = message_test.read()
    print(content)
    message_test.close()
