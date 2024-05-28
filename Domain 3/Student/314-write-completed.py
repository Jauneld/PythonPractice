message = open('314-message.txt','w')#open the file in write mode
#w+: opens a file for reading and writing
#if there is no file the computer mights 
#a. Create the file 
message.write('Testing file for player configuration\n')
message.write('Testing file for player score')
#write methods tells the computer what to write on the file
message.close()#closes the file
#when writing to text, the file was overwritten 
