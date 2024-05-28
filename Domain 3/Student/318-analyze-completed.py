#message = open('318-message.txt','w')
#message.write('Testing file for player configuration\n')
#message.write('Testing file for player score\n')
#message.close()

with open('318-message.text','w+') as message:#change w to w+ so the file is readable and writeable
    #w is the primary opeartion in w+ so it will wipe out the existing content before reading the file
    #if you want the computer to read and write to an existing file w/o deleting its content before writing use r+ instead
    message.write('Testing file for player configuration\n')
    message.write('Testing file for player score\n')
    print('File created')
    print(message.read())
