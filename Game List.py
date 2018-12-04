game_list = []

while True:
    option = int(input("""
    1 - Add a game to our list
    2 - Remove a game from our list
    3 - Insert a game in to the list
    """))
    if option == 1:
        game = input("What game would you like to add to your list?")
        game_list.append(game)
        print(game_list)
    elif option == 2:
        print(game_list)
        game = input("What game would you like to remove from your list?")
        while True:
            if game in game_list:
                q=input("Are you sure you want to remove "+game+"?")
                if q == "yes":
                    game_list.remove(game)
                    print(game_list)
                else:
                    print("Then why did you choose to remove it?")
                    break
            else:
                print(game+"is not in your list, but you can add it, so that you can remove it.")
                break
                
    elif option == 3:
        game = input("What game would you like to insert into your list?")
        pos = int(input("At what position would you like to place "+game+" in your list?"))
        pos -=1

        while True:
            if pos<len(game_list):
                game_list.insert(pos,game)
                print(game_list)
                break
            else:
                print("Invalid position")
    elif option == 4:
        input("Press enter to exit")
        break
                  
    else:
        print("That is not an option")
