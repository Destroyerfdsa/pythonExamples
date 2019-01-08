import random
timesplayed = 0
humanwin = 0
compwin = 0
ties = 0
def main():
    global ties
    global humanwin
    global compwin
    global timesplayed
    timesplayed += 1
    
    if timesplayed == 30:
        print("wow you played 30 games!")
    elif timesplayed == 60:
        print("wow you played 60 games!\nYou seem to really like this game!")
    elif timesplayed == 100:
        print("You have played 100 games!?!?!?!\nThat is a lot. FREE TRIAL IS OVER,\nNow you have to pay me lots of money to continue to play.\njk")
    
    
    #start==============================================================
    print("Enter rock paper or scissors")
    user = input("> ")
    lists = ["rock","paper","scissors"]
    comp = random.choice(lists)
    print("\nComputer: ",comp)
    
    #tie================================================================
    if user.lower() == comp:
      print("\n========================Its a tie!========================")
      ties += 1
      print("You have played a total of: ", timesplayed,"time(s)")
      print("You have won",humanwin,"matches")
      print("Computer has won",compwin,"matches")
      print("You have tied ",ties,"time(s)")
      input("Press enter to play again.")
      main()
      
    #not tie============================================================
    elif user.lower().startswith("r") and comp == "paper":
      print("\npaper beats rock!")
      print("========================Computer wins!========================")
      compwin += 1
      print("You have played a total of: ", timesplayed,"time(s)")
      print("\nYou have won",humanwin,"matches")
      print("Computer has won",compwin,"matches")
      print("You have tied ",ties,"time(s)\n")
      input("Press enter to play again.")
      main()
    
    elif comp == "rock" and user.lower().startswith("p"):
      print("\npaper beats rock!")
      print("==========================User wins!==========================")
      humanwin += 1
      print("You have played a total of: ", timesplayed,"time(s)")
      print("\nYou have won",humanwin,"matches")
      print("Computer has won",compwin,"matches")
      print("You have tied ",ties,"time(s)\n")
      input("Press enter to play again.")
      main()
    
    elif comp == "scissors" and user.lower().startswith("p"):
      print("\nscissors beats paper!")
      print("========================Computer wins!========================")
      compwin += 1
      print("You have played a total of: ", timesplayed,"time(s)")
      print("\nYou have won",humanwin,"matches")
      print("Computer has won",compwin,"matches")
      print("You have tied ",ties,"time(s)\n")
      input("Press enter to play again.")
      main()
    
    elif user.lower().startswith("s") and comp == "paper":
      print("\nscissors beats paper!")
      print("==========================User wins!==========================")
      humanwin += 1
      print("You have played a total of: ", timesplayed,"time(s)")
      print("\nYou have won",humanwin,"matches")
      print("Computer has won",compwin,"matches")
      print("You have tied ",ties,"time(s)\n")
      input("Press enter to play again.")
      main()
    
    elif comp == "scissors" and user.lower().startswith("r"):
      print("\nrock beats scissors!")
      print("==========================User wins!==========================")
      humanwin += 1
      print("You have played a total of: ", timesplayed,"time(s)")
      print("\nYou have won",humanwin,"matches")
      print("Computer has won",compwin,"matches")
      print("You have tied ",ties,"time(s)\n")
      input("Press enter to play again.")
      main()
    
    elif user.lower().startswith("s") and comp == "rock":
      print("\nrock beats scissors!")
      print("========================Computer wins!========================")
      compwin += 1
      print("You have played a total of: ", timesplayed,"time(s)")
      print("\nYou have won",humanwin,"matches")
      print("Computer has won",compwin,"matches")
      print("You have tied ",ties,"time(s)\n")
      input("Press enter to play again.")
      main()
      
    #tie===============================================================  
    elif user.lower().startswith("r") and comp.startswith("r"):
      print("\n========================Its a tie!========================")
      ties += 1
      print("You have played a total of: ", timesplayed,"time(s)")
      print("\nYou have won",humanwin,"matches")
      print("Computer has won",compwin,"matches")
      print("You have tied ",ties,"time(s)\n")
      input("Press enter to play again.")
      main()
      
    elif user.lower().startswith("p") and comp.startswith("p"):
      print("\n========================Its a tie!========================")
      ties += 1
      print("You have played a total of: ", timesplayed,"time(s)")
      print("\nYou have won",humanwin,"matches")
      print("Computer has won",compwin,"matches")
      print("You have tied ",ties,"time(s)\n")
      input("Press enter to play again.")
      main()
      
    elif user.lower().startswith("s") and comp.startswith("s"):
      print("\n========================Its a tie!========================")
      ties += 1
      print("You have played a total of: ", timesplayed,"time(s)")
      print("\nYou have won",humanwin,"matches")
      print("Computer has won",compwin,"matches")
      print("You have tied ",ties,"time(s)\n")
      input("Press enter to play again.")
      main()
    
    
    else:
      print("\n\ni dont know what happend(error)")
      print("You have played a total of: ", timesplayed,"time(s)")
      print("\nYou have won",humanwin,"matches")
      print("Computer has won",compwin,"matches")
      print("You have tied ",ties,"time(s)\n")
      input("Press enter to play again.")
      main()
      
      
main()