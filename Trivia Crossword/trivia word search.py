#Nick /// #Andrew
#11/14/2018
#ask trivia, then word search
#modular design, Functions
import random


####==================================================Variables================================================================####

puzzle = "xkilcwhileebjvnohtypdgfamiwdeknvursnwydjibninpavizsvcahupvpnmdtbatrwdpniilibiprlafoeningobkwnbpjtefd"
score = 0

#words
word1 = "for"
word2 = "function"
word3 = "while"
word4 = "python"
word5 = "index"
word6 = "if"
word7 = "variable"
word8 = "ide"
word9 = "print"
word10 = "input"

recentWord = ""

#word lengths
word1_length = len("for")*2
word2_length = len("function")*2
word3_length = len("while")*2
word4_length = len("python")*2
word5_length = len("index")*2
word6_length = len("if")*2
word7_length = len("variable")*2
word8_length = len("ide")*2
word9_length = len("print")*2
word10_length = len("input")*2

word1_check = False
word2_check = False
word3_check = False
word4_check = False
word5_check = False
word6_check = False
word7_check = False
word8_check = False
word9_check = False
word10_check = False

word1_input = ""
word2_input = ""
word3_input = ""
word4_input = ""
word5_input = ""
word6_input = ""
word7_input = ""
word8_input = ""
word9_input = ""
word10_input = ""





#puzzle
def displayPuzzle():
    print()
    print(puzzle[0:10])
    print(puzzle[10:20])
    print(puzzle[20:30])
    print(puzzle[30:40])
    print(puzzle[40:50])
    print(puzzle[50:60])
    print(puzzle[60:70])
    print(puzzle[70:80])
    print(puzzle[80:90])
    print(puzzle[90:])
    print()


####==================================================Trivia===================================================================####

#trivia variables and input
def trivia():
    #globals
    global recentWord
    
    global word1
    global word2 
    global word3
    global word4 
    global word5
    global word6 
    global word7 
    global word8 
    global word9 
    global word10

    global word1_check
    global word2_check
    global word3_check
    global word4_check
    global word5_check 
    global word6_check
    global word7_check
    global word8_check 
    global word9_check 
    global word10_check

    global word1_input
    global word2_input
    global word3_input
    global word4_input
    global word5_input
    global word6_input
    global word7_input
    global word8_input
    global word9_input
    global word10_input

    
    x = random.randrange(0,10)
    if x == 0:
        if word1_check == True:
            trivia()
        elif word1_check == False:
            print()
            word1_input = input("A type of loop that triggers at intervals with set iterations\n").lower() #for
            if word1_input == "for":
                word1_check = True
                recentWord = "for"
                wordSearch()
            else:
                print("You answered incorrectly, here is a new question...")
                trivia()

    elif x == 1:
        if word2_check == True:
            trivia()
        elif word2_check == False:
            print()
            word2_input = input("A piece of code used to organize parts of a program and can be rerun.\n").lower() #function
            if word2_input == "function":
                word2_check = True
                recentWord = "function"
                wordSearch()
            else:
                print("You answered incorrectly, here is a new question...")
                trivia()
            
    elif x == 2:
        if word3_check == True:
            trivia()
        elif word3_check == False:
            print()
            word3_input = input("A loop that continues until it reaches a certain parameter that breaks it.\n").lower() #while
            if word3_input == "while":
                word3_check = True
                recentWord = "while"
                wordSearch()
            else:
                print("You answered incorrectly, here is a new question...")
                trivia()


            
    elif x == 3:
        if word4_check == True:
            trivia()
        elif word4_check == False:
            print()
            word4_input = input("computer programming language that starts with p\n").lower() #python
            if word4_input == "python":
                word4_check = True
                recentWord = "python"
                wordSearch()
            else:
                print("You answered incorrectly, here is a new question...")
                trivia()

            
    elif x == 4:
        if word5_check == True:
            trivia()
        elif word5_check == False:
            print()
            word5_input = input("A position or location in a string that can be separated\n").lower() #index
            if word5_input == "index":
                word5_check = True
                recentWord = "index"
                wordSearch()
            else:
                print("You answered incorrectly, here is a new question...")
                trivia()
            
    elif x == 5:
        if word6_check == True:
            trivia()
        elif word6_check == False:
            print()
            word6_input = input("A split in the code that choose a direction based on a variable, or logic\n").lower() #if
            if word6_input == "if":
                word6_check = True
                recentWord = "if"
                wordSearch()
            else:
                print("You answered incorrectly, here is a new question...")
                trivia()

            
    elif x == 6:
        if word7_check == True:
            trivia()
        elif word7_check == False:
            print()
            word7_input = input("A value set to a int or string\n").lower()#variable
            if word7_input == "variable":
                word7_check = True
                recentWord = "variable"
                wordSearch()
            else:
                print("You answered incorrectly, here is a new question...")
                trivia()
            
            
    elif x == 7:
        if word8_check == True:
            trivia()
        elif word8_check == False:
            print()
            word8_input = input("A program used to facilitate code production, it is an acronym.\n").lower() #ide
            if word8_input == "ide":
                word8_check = True
                recentWord = "ide"
                wordSearch()
            else:
                print("You answered incorrectly, here is a new question...")
                trivia()

            
    elif x == 8:
        if word9_check == True:
            trivia()
        elif word9_check == False:
            print()
            word9_input = input("A standard function used to display variables or strings.\n").lower() #print
            if word9_input == "print":
                word9_check = True
                recentWord = "print"
                wordSearch()
            else:
                print("You answered incorrectly, here is a new question...")
                trivia()

            
    elif x == 9:
        if word10_check == True:
            trivia()
        elif word10_check == False:
            print()
            word10_input = input("A function used to set a value from a user\n").lower() #input
            if word10_input == "input":
                word10_check = True
                recentWord = "input"
                wordSearch()
            else:
                print("You answered incorrectly, here is a new question...")
                trivia()
                
####=================================================Word Search===============================================================####



def wordSearch():
    #globals
    global recentWord
    global word1_length
    global word2_length
    global word3_length
    global word4_length
    global word5_length
    global word6_length
    global word7_length
    global word8_length
    global word9_length
    global word10_length

    global score
    
    global puzzle

    ##print("you guessed correctly!\n")

    #show puzzle
    displayPuzzle()

    print("the word you are looking for is", recentWord)
    x = input("enter the location of the word. use a 0 when it is a single digit number. ex. '050856'. The puzzle starts at 00.\n")
    xlen = len(x)
    
    if recentWord == "for":
        if word1_length == xlen:
            if x == "988878":
                score += 1
                if score >= 10:
                    win()
                print("you got the word. heres another trivia")     #for
                trivia()
            else:
                print("thats not the correct sequence.")
                wordSearch()            
        else:
            print("that is not the correct length for this word")
            wordSearch()

    elif recentWord == "function":
        if word2_length == xlen:
            if x == "2232425262728292":
                score += 1
                if score >= 10:
                    win()
                print("you got the word. heres another trivia")     #function
                trivia()
            else:
                print("thats not the correct sequence.")
                wordSearch()            
        else:
            print("that is not the correct length for this word")
            wordSearch()

    elif recentWord == "while":
        if word3_length == xlen:
            if x == "0506070809":
                score += 1
                if score >= 10:
                    win()
                print("you got the word. heres another trivia")     #while
                trivia()
            else:
                print("thats not the correct sequence.")
                wordSearch()            
        else:
            print("that is not the correct length for this word")
            wordSearch()

    elif recentWord == "python":
        if word4_length == xlen:
            if x == "191817161514":
                score += 1
                if score >= 10:
                    win()
                print("you got the word. heres another trivia")     #python
                trivia()
            else:
                print("thats not the correct sequence.")
                wordSearch()            
        else:
            print("that is not the correct length for this word")
            wordSearch()

    elif recentWord == "index":
        if word5_length == xlen:
            if x == "4030201000":
                score += 1
                if score >= 10:
                    win()
                print("you got the word. heres another trivia")     #index
                trivia()
            else:
                print("thats not the correct sequence.")
                wordSearch()            
        else:
            print("that is not the correct length for this word")
            wordSearch()

    elif recentWord == "if":
        if word6_length == xlen:
            if x == "7181":
                score += 1
                if score >= 10:
                    win()
                print("you got the word. heres another trivia")     #if
                trivia()
            else:
                print("thats not the correct sequence.")
                wordSearch()            
        else:
            print("that is not the correct length for this word")
            wordSearch()

    elif recentWord == "variable":
        if word7_length == xlen:
            if x == "1323334353637383":
                score += 1
                if score >= 10:
                    win()
                print("you got the word. heres another trivia")     #variable
                trivia()
            else:
                print("thats not the correct sequence.")
                wordSearch()            
        else:
            print("that is not the correct length for this word")
            wordSearch()

    elif recentWord == "ide":
        if word8_length == xlen:
            if x == "483828":
                score += 1
                if score >= 10:
                    win()
                print("you got the word. heres another trivia")     #ide
                trivia()
            else:
                print("thats not the correct sequence.")
                wordSearch()            
        else:
            print("that is not the correct length for this word")
            wordSearch()

    elif recentWord == "print":
        if word9_length == xlen:
            if x == "5666768696":
                score += 1
                if score >= 10:
                    win()
                print("you got the word. heres another trivia")     #print
                trivia()
            else:
                print("thats not the correct sequence.")
                wordSearch()            
        else:
            print("that is not the correct length for this word")
            wordSearch()

    elif recentWord == "input":
        if word10_length == xlen:
            if x == "2535455565":
                score += 1
                if score >= 10:
                    win()
                print("you got the word. heres another trivia")     #input
                trivia()
            else:
                print("thats not the correct sequence.")
                wordSearch()            
        else:
            print("that is not the correct length for this word")
            wordSearch()
####==================================================Win!======================================================================####

#first line code
def win():
    global score
    if score >= 10:
        print("You win the game!")
        input("Press enter to exit game.")
        exit(100)

####===================================================Start===================================================================####

trivia()
wordSearch()






























































