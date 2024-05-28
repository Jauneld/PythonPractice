#in file management, files that are no longer need should be closed so you do not alter the file. 
#it also frees up memory space and allows the file to be safely modified by other programs
message = open('312-message.txt','w')
message.write('Testing file for player configuration')
message.write('Testing file for player score')
message.close()

message_test = open('312-message.txt','r')

message_test.close()#close: closes the file
#() serves multiple purposes: 
#1. Makes functions easily idenifiable and maintains specific syntax
#2. Functions often require arguments and parentheses serves as a container for those arguments
## Not all functions need arguments and soem function scan be passed as arguments themselves without parentheses

