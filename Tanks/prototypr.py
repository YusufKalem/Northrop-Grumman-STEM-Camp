from Tank import Tank

print("Welcome to the Tank game!")

# Set up the game
numPlayers = int(input("How many players? "))
tanks = {}
for player in range(1, numPlayers+1):
    printString = "Player " + str(player) + "'s name: "
    tanks[player] = Tank(input(printString))

aliveTanks = len(tanks)

while aliveTanks > 1:
    # List the tanks and their stats
    print()
    for playerNum in tanks.keys():
        print(playerNum, tanks[playerNum])

    # Loop for players to take turns
    for playerNum in tanks.keys():
        # Get the current player's tank object
        playerTank = tanks[playerNum]

        # if DEAD tank, turn gets skipped
        if not playerTank.alive:
            continue

        print()
        print(playerTank.name + ", it's your turn!")
        target = int(input(tanks[playerNum].name + " fires at player: "))

        # Checking for player, alive, and not self.
        try:
            targetTank = tanks[target]
        except KeyError as name:
            print("There is no player", str(name), "! enter player number")
            continue
        except ValueError as name:
            print(playerTank.name + " lost their turn! Invalid Input")
            continue
        if not targetTank.alive:
            print("Player", str(target) + ",", targetTank.name + ", is dead!")
            continue
        if targetTank.name == playerTank.name:
            print("You shouldn't fire at yourself!")
            continue

        # Fire!
        print()
        print("*" * 30)

        playerTank.fireAt(targetTank)
        if not targetTank.alive:
            aliveTanks -= 1

        print("*" * 30)

# Determine the winner
for tank in tanks.values():
    if tank.alive:
        print(tank.name, "is the winner!")
        break
