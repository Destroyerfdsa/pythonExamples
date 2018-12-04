#Hero's Inv
#Nicholaus Whites
#11/28
import os
import random

def hud():
    print("Stats: ",player_stats)
    print("Inventory: ",inventory)
    print("Equipped: ",equipped)

def refresh():
    os.system('cls')
    hud()
    print()
    print()

chest_items = ["gold","gems","elven sword","bow","crossbow","boots","hat","sun","traps"]
player_health = 100
player_armor = 1250
player_attack = 250
player_money = 0
inventory = ["Rusty Sword","Leather Armor","Wooden Shield","Small Healing Potion"]
max_inventory = 10
equipped = []
player_stats = ["Health",player_health,"Armor",player_armor,"Attack",player_attack,"Money",player_money]

print("As you set out on your journey you have the following")
print("player stats")
print(player_stats)
print()
print("Your items include:")
for item in inventory:
    print(item)

input("\nPress enter key to continue...")
refresh()

print("You have",str(len(inventory))+"/"+str(max_inventory),"items in your possession,")
print("so you can pick up ",max_inventory-len(inventory)," more items")
input("\nPress enter key to continue...")
refresh()


print("You get attacked and take damage")
player_stats[1]-=22
input("\nPress enter key to continue...")
refresh()

input("\nYou have taken some damage on your journey \n"+
      "your health is at "+str(player_stats[1])+"\n"+
      "you need to use your healing potion \nPress the enter key to continue...")

if "Small Healing Potion" in inventory:
    print("You live, by healing potion")
    player_stats[1]+=20
    inventory.remove("Small Healing Potion")
input("\nPress the enter key to continue.")
refresh()

for i in range(len(inventory)):
    print(str(i),inventory[i])
print("lets equip some armor")
index = int(input("\nEnter the index number for an armor item in your inventory you wish to equip: "))
while index>len(inventory)-1 or index<0 and index != "":
    print("That number is out of range")
    index = int(input("\nEnter the index number for an armor item in inventory: "))
print("You equip your ",inventory[index])
equipped.append(inventory[index])
inventory.remove(inventory[index])
if "Leather Armor" in equipped:
    player_stats[3] += 1000
if "Wooden Shield" in equipped:
    player_stats[3] +=500
input("\nPress enter to continue...")
refresh()

chest = []
for i in range(random.randrange(len(chest_items))):
    item = random.choice(chest_items)
    chest.append(item)
    

print("You find chest")
print(chest)
print()
print("You steal the items from chest. You filthy theif you..")

if len(inventory)+len(chest)<max_inventory:
    inventory+=chest
else:
    drop = len(inventory)+len(chest) - max_inventory
    for i in range(drop):
        x=random.choice(chest)
        chest.remove(x)
    inventory += chest
input("\nPress the enter key to continue...")
refresh()

#treasure to gold
print("convert treasure to gold")
if "gold" in inventory:
    player_stats[7]+=100
    inventory.remove("gold")
if "gems" in inventory:
    player_stats[7]+=1000
    inventory.remove("gems")
input("\nPress enter key to continue.")
refresh()

if player_stats[7]>100:
    print("Trade sword for crossbow. you sell your sword for 20 gold and buy crossbow for 100 gold")
    player_stats[7]+=20
    player_stats[7]-=100
    inventory[0] = "crossbow"
input("\nPress the enter key to continue.")
refresh()

print("You trade in the last 2 items from your inventory for a new item.")
inventory[len(inventory)-2:len(inventory)] = ["orb of future telling"]
input("\nPress the enter key to continue.")
refresh()

print("In great battle, shield destroyed.")
##for i in range(len(inventory)):
##    if inventory[i] == "Wooden Shield":
##        del inventory[i]
##for i in range(len(equipped)):
##    if equipped[i] == "Wooden Shield":
##        del equipped[i]

if "Wooden Shield" in inventory:
    inventory.remove("Wooden Shield")
if "Wooden Shield" in equipped:
    equipped.remove("Wooden Shield")

input("\nPress the enter key to continue.")
refresh()
print("Your first 2 items in your inventory are stolen by thieves. karma huh. \nThats what happens when you steal in the first place.")
del inventory[:2]
print("Your inventory is now:")
print(inventory)
input("\nPress the enter key to continue.")
refresh()
































