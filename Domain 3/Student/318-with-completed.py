#message = open('318-message.txt','w')
#message.write('Testing file for player configuration\n')
#message.write('Testing file for player score\n')
#message.close()

#with statement: is used to open, perform an action on a file and closes a file in one go
with open('318-message.txt','w') as message:
  message.write('Testing file for player configuration\n')
  message.write('Testing file for player score\n')
  print('File created')

