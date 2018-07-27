#TANK GAME

from Tank import Tank
#Game Setup
tanks = {}
numPlayers = int(input("How many players? "))
for player in range(1, numPlayers+1):
    printString = "Player " + str(player) + "'s name: "
    tanks[player] = Tank(input(printString))

aliveTanks = len(tanks)

while aliveTanks > 1:

#these are the tanks and what there stats are
    print()
    for playerNum in tanks.keys():
        print(playerNum, tanks[playerNum])

    for playerNum in tanks.keys():
        playerTank = tanks[playerNum]

        if not playerTank.alive:
            continue
        print()
        print(playerTank.name + ", it's your turn!")
        #error handling
        try:
            target = int(input(tanks[playerNum].name + " fires at player: "))
            targetTank = tanks[target]
        except KeyError as name:
            print("There is no player",  str(name) + "! enter player number")
            continue
        except ValueError as name:
            try:
                target = input(tanks[playerNum].name + " fires at player: ")
                for key, tank in tanks.items():
                    if tank.name == target:
                        targetTank = tanks[key]

            except KeyError as name:
                print("There is no player",  str(name) + "! enter correct player name")
                continue
            print(playerTank.name + " lost their turn! Invalid Input")
            continue

    if not targetTank.alive:
        print("Player", str(target) + ",", targetTank.name + ", is dead!")
        continue
    if targetTank.name == playerTank.name:
        print("You shouldn't fire at yourself!")
        continue

          print()
                print("*" * 30)

                playerTank.fireAt(targetTank)
                if not targetTank.alive:
                    aliveTanks -= 1

                print("*" * 30)
