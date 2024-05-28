#append: adds text to the end of an existing file
message = open('315-message.txt','w')
message.write('Testing file for player configuration\n')
message.write('Testing file for player score\n')

message.close()

message = open('315-message.txt','a')#a: open in append mode
#a+ opens in read and write mode
message.append('[Username]\n')
message.close()
# write vs append
#write overwrites existing files
#append adds on to the end of existing files
