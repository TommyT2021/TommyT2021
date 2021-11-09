import random 

def dice_game():
    playera = open("Player_A.txt","w")
    playerb = open("Player_B.txt","w")
    loop = 0
    totala = 0
    totalb = 0
    while loop != 3:
        rollone = random.randint(1,6)
        playera = open("Player_A.txt","a")
        playera.write(str(rollone))
        playera.write("\n")
        rolltwo = random.randint(1,6)
        playerb = open("Player_B.txt","a")
        playerb.write(str(rolltwo))
        playerb.write("\n")
        loop +=1
    playera = open("Player_A.txt")
    for line in playera:
        totala += int(line)
    playerb = open("Player_B.txt")
    for line in playerb:
        totalb += int(line)
    if totala > totalb:
        print("The winner is Player A with",totala,"points.")
    elif totalb > totala:
        print("The winner is Player B with",totalb,"points.")
    elif totala==totalb:
        print("Player A and Player B are tied with",totala,"points.")
    
        
    

