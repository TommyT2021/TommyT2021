tags = input("Enter one to four tags: ").split()
number_tags = 0
for i in tags:
    number_tags += 1

gamefile = open("Lab9_CatGames.txt")
matching_game = []
for line in gamefile:
    matchcount = 0
    gameinfo = line.split()
    for i in tags:
        if i in gameinfo:
            matchcount += 1
    if matchcount == number_tags:
        matching_game.append(gameinfo[0])
        
if len(matching_game) == 0:
    print("Sorry, no games match your criteria")
else:
    print("There are",len(matching_game),"results")
    print("Here are your matching games:",', '.join(matching_game))
