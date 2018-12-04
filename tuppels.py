gameList = ["",
            "Skyrim",
            "Metro 2033",
            "Half-Life 2",
            "Counter-Strike: Source",
            "Destiny 2",
            "Fallout 4",
            "Counter-Strike: GO",
            "Terraria",
            "Dragonball Fighterz"]


print(len(gameList))

num5game=gameList[4]
print(num5game)

middle5 = gameList[3:7]
print(middle5)

last4 = gameList[6:]
print(last4)

evens =  gameList[::2]
print(evens)

backwards = gameList[::-1]
print(backwards)

for i in gameList:
    print(i)
print()

print(gameList)

gameList +=("11",12,13.0,14,"15")
print(gameList)

gameList[0]="idk"
gameList[1]="Skyrim"
print(gameList)
