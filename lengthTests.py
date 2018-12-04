##word = input("Type in a word: ")
##pos1 = word.find("e")
##pos2 = word.find("e",pos1+1)
##substring=word[pos1:pos2]
##print(substring)


name = input("Enter your First and Last name: ")
x=name.find(" ")
firstName = name[:x]
lastName = name[x+1:]
print(firstName)
print(lastName)
input("Press enter to continue.")
