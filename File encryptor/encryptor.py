#Nicholaus  Whites
#File Encryption
#1/7/19
"""This program is for encrypting files"""

import pyAesCrypt

bufferSize = 64 * 1024

print("Made by Nicholaus Whites")
print("1/7/2019")

#Encrypt file
encrypt = input("Would you like to encrypt a file? (y/n): ")
if encrypt.lower() == "y":
  inFile = input("Enter file name (test.txt): ")
  outFile = input("Enter ecrypted files name (test.txt.aes): ")
  #get password
  password = input("Enter password for file: ")
  #verify password
  password2 = input("Enter password again: ")
  if password == password2:
    pyAesCrypt.encryptFile(inFile,outFile,password,bufferSize)
  else:
    #loop until passwords match
    while password != password2:
      print("Passwords do not match!")
      password = input("Enter password for file: ")
      password2 = input("Enter password again: ")
    #check 1 last time
    if password == password2:
      #try to crypt file
      try:
        pyAesCrypt.encryptFile(inFile,outFile,password,bufferSize)
      #if file not found, print error and exit program.
      except OSError as ex:
        print(ex)
        exit(0)
  print("Done!")




#Decrypt file
else:
  decrypt = input("Would you like to decrypt a file?: ")
  if decrypt.lower() == "y":
    inFile = input("Enter file name (test.txt.aes): ")
    outFile = input("Enter ecrypted files name (test.txt): ")
    password = input("Enter file password: ")
    #try to decrypt file
    try:
      pyAesCrypt.decryptFile(inFile,outFile,password,bufferSize)
    #if password is wrong
    except ValueError as ex:
      print(ex)
      #loop to enter correct password
      while password:
        password = input("Enter file password again: ")
        #if password is correct, decrypt file and break from loop
        try:
          pyAesCrypt.decryptFile(inFile,outFile,password,bufferSize)
          break
        except ValueError as ex:
          print(ex)

    print("Done!")
  else:
    print("This encryptor was made by Nicholaus Whites")
    print("Exiting...")
    exit(0)