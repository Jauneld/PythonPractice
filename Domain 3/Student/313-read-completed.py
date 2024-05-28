message = open('313-message.txt','w')# w: write mode
message.write('Testing file for player configuration')
message.write('Testing file for player score')
message.close()

message_test = open('313-message.txt','r')#opens the files(argument 1) in read mode(argument 2)
#r+: read and write mode
content = message_test.read()# a variable is requires to store the contents of the file being read
print(content)# to 
message_test.close()
