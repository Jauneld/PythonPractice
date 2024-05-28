message = open('311-message.txt','w')#open: open the files
message.write('Testing file for player configuration')
message.close()

message_test = open('311-message.txt','r')#r argument opens the file it read mode
print('311-message is open')
