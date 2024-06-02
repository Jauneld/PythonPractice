import io

game_stream = io.StringIO()#allows to input strings into memory and then retrieve them later

game_stream.write("The game has started.\n")#write info
game_stream.write("Here is your first question. \n")

game_stream.seek(0)#seeks info at a given character 
print(game_stream.read())
