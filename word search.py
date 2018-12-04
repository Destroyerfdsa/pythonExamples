attempts = 0

print("Python terms")
puzzle = ("fjvfloatdyyopxedninsmspfycnnalxeaeeukgeislufryprlcabeeiagco"+
          "ibuclqttbongojlivxobgadmyahgerjstringwvrs")

def displayPuzzle():
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

print()

#display
displayPuzzle()

print("Word List")
word_list = "float, while, if, boolean, double, operators, string, slicing, index"
print(word_list)
print()
    
#get length of word
word1_length=len("float")
word2_length=len("while")
word3_length=len("if")
word4_length=len("boolean")
word5_length=len("double")
word6_length=len("operators")
word7_length=len("string")
word8_length=len("slicing")
word9_length=len("index")

#get answer input
x=0
while x==0:
    word1=input("Enter index pos of 'float': ")
    attempts+=1
    i=0
    foundword=""
    while i < word2_length:
        index=word1[i]
        index=int(index)
        foundword = foundword+puzzle[index]
        i+=1
    if foundword == "float":
        print(foundword)
        print("Great Job")
        x=1
    else:
        print("Incorrect, try again")


##while x==1:
##    word2=input("Enter index pos of 'while': ")
##    attempts+=1
##    i=0
##    foundword=""
##    while i < word3_length:
##        index=word2[i]
##        index=int(index)
##        foundword = foundword+puzzle[index]
##        i+=1
##    if foundword == "while":
##        print(foundword)
##        print("Great Job")
##        x=2
##    else:
##        print("Incorrect, try again")


while x==1
    word2=input("Enter index pos of 'while': ")
    attempts+=1
    i=0
    foundword=""
    
    
























