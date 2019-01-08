#Nicholaus Whites
#1/2/19
#trivia game

import sys

def open_file(file_name,mode):
    """Open a file."""
    try:
        the_file = open(file_name,mode)
    except IOError as e:
        print("Unable to open the file", file_name,"Ending the program.\n")
        print(e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from file, replacing slash"""
    line = the_file.readline()
    line = line.replace("/","\n")
    return line


def next_block(the_file):
    """return the next block of data from trivia file."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
        
    explain = next_line(the_file)
        
    return category,question,answers,correct,explain
    



def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t",title,"\n")


def main():
    """Main function for trivia game"""
    the_file = open_file("Trivia_Game.txt","r")
    title = next_line(the_file)
    welcome(title)
    score = 0
    
    category,question,answers,correct,explain = next_block(the_file)
    while category:
        print(category)
        print(question)
        num = 0
        for i in range(4):
            print(answers[i])
        answer = input("What is your answer? (1, 2, 3, or 4): ")
        
        if answer == correct:
            print("You got it correct!")
            score += 1
        else:
            print("That was incorrect!")
        print(explain)
        print("Score:",score)

        category,question,answers,correct,explain = next_block(the_file)
        
    the_file.close()
    
    print("Thanks for playing!")
    print("Your final score was:",score)
            
          
main()
input("Press enter to exit.")

