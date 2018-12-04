import random

name = input("Enter your name: ")
print(name[0])
length =len(name)
print(length)
indexPos = random.randint(0,length)
if indexPos <= length:
    char = name[indexPos]
    print("Character:",char)
else:
    print("that is out of the range")



rLetter = random.randint(0,11)




testName = name[random.randint(0,length)]
testName = testName+name[random.randint(0,length)]
testName = testName+name[random.randint(0,length)]
testName = testName+name[random.randint(0,length)]
testName = testName+name[random.randint(0,length)]
testName = testName+name[random.randint(0,length)]
testName = testName+name[random.randint(0,length)]
print("Random letters:",testName)
