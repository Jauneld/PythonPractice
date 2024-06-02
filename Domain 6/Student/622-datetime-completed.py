import datetime
current_time = datetime.datetime.now()#to get the current date and tim
print("The current date and time is:",current time.strftime("%m-%d-%Y %I:%M %p"))
print("The day of the week is" , current_time.weekday())
print("The day of the week is" , current_time.strftime("%A"))
#strftime method: format a date and time to a presentable format
#to format in mm/dd/yyyy hh:mm -current time.strftime("%m-%d-%Y %I:%M %p")
#H - 24-hr time
#I - 12-hr time 
#p - am or pm
#A - the name of the weekday
