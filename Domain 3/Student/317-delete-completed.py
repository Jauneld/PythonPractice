#files are deleted so that the data in the files do not pose a security risk
import os
message_file = '317-message.txt'

if os.path.exists(message_file):#does the file exists
    os.remove(message_file)#if so delete it using the remove method
    print("Message file removed")
    
else: 
    print("There was no message file to remove")
#Some challenges to delete files are:
#1. If the file is open somewhere else, or used in another process, there will be an error
#2. If the Python Script doesn't have the permission to delete the file, there will be an error.
#3. If there are underlying issues with the file system such as corrption or disk error, there will be an error. 
