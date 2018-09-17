##<Destro>
##<email destroyerasdfdev@gmail.com>
##<Project name: Mad Lib Example>
##<9/7/2018>



first_name = "nick"

print(first_name)

fact = "Skyrim is great"
print("my name is",first_name,"and i think",fact)
message = first_name+fact
print(message)

num1 = 10
num2 = 15
answer = num1+num2-num1*num1
print(answer)

##body_parts = input("Enter a Body Part(plural): ")
##body_part = input("Enter a Body Part: ")
##noun = input("Enter a Noun: ")
##noun2 = input("Enter a second Noun: ")
##
##adjective = input("Enter an Adjective: ")
##adjective2 = input("Enter a second Adjective: ")
##plur_noun = input("Enter a Noun(plural): ")
##
##
##print("Here is a list of the most",adjective,"horror",plur_noun,
##      "ever made in Hollywood!\nEach of these",adjective,"films received a rating of two",body_parts,
##      "-up from Siskel and Ebert.\n1. The Hunch",body_part,"of Notre",noun,
##      "\n2. The",noun,"of the Living",noun2,"\n3.",noun," of Frankenstein\n4. Invasion of the",noun,
##      "Snatchers\n5.",noun,
##      "from the",adjective2,"Lagoon\n6. Last",noun,"on the Left\n7. The",noun,
##      "of the Opera")
secret = input("Press Enter To Continue...")
if secret == "secret":
    print("you found the secret!")   

    noun = input("Enter a Noun: ")
    if noun == "secret":
        print("wow you are good at finding secrets")
    noun2 = input("Enter a second Noun: ")
    if noun2 == "secret":
        print("now youre just entering secret for everthing")
    plur_noun = input("Enter a plural Noun: ")
    if plur_noun == "secret":
        print("what do you want? why are you asking for more secrets?")
    verb = input("Enter a verb: ")
    if verb == "secret":
        print("im not going to give you any more secrets. Thats not the point of this game.")
    ing_verb = input("Enter a ing verb: ")
    adjective = input("Enter an Adjective: ")
    if adjective == "secret":
        print("wow you are persistent. But the story wont make sense anymore!")
    adjective2 = input("Enter a second Adjective: ")
    if adjective2 == "secret":
        print("Fine im DONE. The game is over now.")
        nope = input()
        if nope == "nope":
            print("What? Why cant i close the game?\n You did this. Didnt you.")
            lol = input()
            if lol == "secret":
                print("*sigh* fine if thats what you want, then you can end the game.\nI will wait.")
                input()
                exit(102)
        else:
            exit(101)
else:
    noun = input("Enter a Noun: ")
    noun2 = input("Enter a second Noun: ")
    plur_noun = input("Enter a plural Noun: ")
    verb = input("Enter a verb: ")
    ing_verb = input("Enter a ing verb: ")
    adjective = input("Enter an Adjective: ")
    adjective2 = input("Enter a second Adjective: ")
    
    year = input("Enter a Year: ")
    name2 = input("Enter a First Name: ")
    animal = input("Enter an Animal: ")
    print("wow there is a lot to type...")
    adverb = input("Enter an adverb: ")

    print("They say my school is haunted; my",adjective,"friend",name2,"says she saw a",adjective,noun,"floating at the end of the hall near the cafeteria.\n"
          "Some say if you",verb,"down that hallway at night, you'll hear a",animal,ing_verb,adverb,". My",adjective,"friend",name2,"saw a",adjective,noun,ing_verb," under one of the tables once.\n"
          "I hope i never see any",plur_noun,ing_verb,"; eating lunch there is scary enough!")    

    input()
