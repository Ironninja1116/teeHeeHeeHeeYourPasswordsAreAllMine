# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import hashlib
import bcrypt
mybytes = ''
mysalt = ''
myhash = ''


# checking if my filename matches actual file + extension bc im using windows (only used for testing)
# import os
# print(os.listdir('.'))
# ARGPARSE
import argparse
myparser = argparse.ArgumentParser(prog='main', description='crack a password')
myparser.add_argument('--password', type=str, help='if you would like to insert your own plaintext password to crack (whether to test the program or to decrypt), this will store that password as a string')
myparser.add_argument('--passwordlength',  type=int, help='use this to manually specify the length of the password if the password is not provided [MUST BE SPECIFIED FOR HASHES]')
myparser.add_argument('--uppercase',  type=bool, help='if the password you\'re trying to crack includes uppercase characters, use this argument [MUST BE SET TO TRUE IF NO PASSWORD IS SPECIFIED OR IF USING A HASH]')
myparser.add_argument('--lowercase',  type=bool, help='if the password you\'re trying to crack includes lowercase characters, use this argument [MUST BE SET TO TRUE IF NO PASSWORD IS SPECIFIED OR IF USING A HASH]')
myparser.add_argument('--numbers',  type=bool, help='if the password you\'re trying to crack includes number characters, use this argument [MUST BE SET TO TRUE IF NO PASSWORD IS SPECIFIED OR IF USING A HASH]')
myparser.add_argument('--symbols',  type=bool, help='if the password you\'re trying to crack includes symbol characters, use this argument [MUST BE SET TO TRUE IF NO PASSWORD IS SPECIFIED OR IF USING A HASH]')
myparser.add_argument('--hash',  type=str, help='use this to input a hash (IF BCRYPT, DO THIS: \'hash\'')
myparser.add_argument('--encryption',  type=str, choices=['md5', 'bcrypt', 'sha256'], help='if your password/hash uses md5 encryption use this argument, options are md5, bcrypt, and sha256')
myparser.add_argument('--dictionary',  type=bool, help='use this argument if you want to do a dictionary attack')
myparser.add_argument('--bruteforce',  type=bool, help='use this argument if you want to do a brute force attack')

args = myparser.parse_args()

# FUNCTIONS
# For passwords that are given, this automatically determines what type of characters are in the password (ie: numbers, uppercase, lowercase, etc.) index 0 represents symbol, index 1 represents number, index 2 represents uppercase, index 3 represents lowercase
def analyzecharacters(word):
    letterlist = [*word]
    booleananalysis = [False, False, False, False]
    i = 0
    for x in range(len(letterlist)):
        # print("current index = " + str(i))
        current = ord(letterlist[i])
        # print("currently checking " + letterlist[i])
        # print("currently checking " + str(current))
        if (33 <= current <= 47) or (58 <= current <= 64) or (91 <= current <= 96) or (123 <= current <= 126):
            booleananalysis[0] = True
        elif 48 <= current <= 57:
            booleananalysis[1] = True
        elif 65 <= current <= 90:
            booleananalysis[2] = True
        elif 97 <= current <= 122:
            booleananalysis[3] = True
        else:
            print("Unexpected Character")
        i = i + 1
        # print("current list: " + str(booleananalysis))
    return booleananalysis


# There are multiple places where users are asked true or false questions. This asks these questions and ensures correct responses.
def trueorfalse(question):
    response = ""
    while response != 'true' and response != 'false':
        response = input("PLEASE ANSWER TRUE OR FALSE: " + question).lower()
    if response == 'true':
        return True
    else:
        return False


# Adds ascii values of possible characters into an array. index 0 is symbols, 1 is numbers, 2 is uppercase, 3 is lowercase
def makeoptionsarray(analysisarray):
    optionsarray = []
    if analysisarray[0]:
        for x in range(33,48):
            optionsarray.append(x)
    if analysisarray[1]:
        for x in range(48,58):
            optionsarray.append(x)
    if analysisarray[0]:
        for x in range(58,65):
            optionsarray.append(x)
    if analysisarray[2]:
        for x in range(65,91):
            optionsarray.append(x)
    if analysisarray[0]:
        for x in range(91,97):
            optionsarray.append(x)
    if analysisarray[3]:
        for x in range(97,123):
            optionsarray.append(x)
    if analysisarray[0]:
        for x in range(123,127):
            optionsarray.append(x)
    optionsarray.append(0)
    return optionsarray

# creates an array of indexes that will refer to the indexes of the options array
def makeprintedarray(passwordsize):
    printedarray = []
    for x in range(passwordsize):
        printedarray.append(0)
    return printedarray

# compares the most common passwords in the dicitionary to the correct password. If there's a match, the loop ends and returns true (ending the entire program). If none match, false is returned.
def dictionaryattack(correctPassword):
    attacklist = open("10-million-password-list-top-1000.txt", "r")
    for password in attacklist:
        if args.password:
            print(password.replace("\n", "") + " == " + correctPassword + " ?")
            if password.replace("\n", "") == correctPassword:
                return True
        # checks if an inputted HASH equals the dictionary value when coverted to a hash
        if args.hash:
            if args.encryption == 'md5':
                print("current plaintext: " + password.replace("\n", "" + " current hash: " + hashlib.md5(bytes(password.replace("\n", ""), 'utf-8')).hexdigest() + " Your hash: " + correctPassword + " ?"))
                if hashlib.md5(bytes(password.replace("\n", ""), 'utf-8')).hexdigest() == correctPassword:
                    return True
            if args.encryption == 'bcrypt':
                print("does " + password.replace("\n", "") + " == " + correctPassword + " ?")
                # print("correct hash: " + correctPassword)
                if bcrypt.checkpw(((password.replace("\n", "")).encode('utf-8')), bytes(correctPassword,'UTF-8')):
                    return True
            if args.encryption == 'sha256':
                print("current plaintext: " + password.replace("\n", "" + " current hash: " + hashlib.sha256(bytes(password.replace("\n", ""), 'utf-8')).hexdigest() + " Your hash: " + correctPassword + " ?"))
                if hashlib.sha256(bytes(password.replace("\n", ""), 'utf-8')).hexdigest() == correctPassword:
                    return True
    return False




# MAIN
# Automatically sets hash values to false as default, important later
mdfive = False
bcryptCheck = False
shatwofivesix = False
# Asks whether user will be inputting a password or if they want the program until the end (no longer needs to be asked
# inputtingPassword = trueorfalse("Will you provide a password? ")
# Automatically picks up features about password if given (args.password is the password from the argparser), otherwise the program will take in the information given about the password in the arguments
if args.password:
    print("YES")
    endPassword = args.password
    print(endPassword)
    analysis = analyzecharacters(endPassword)
    passwordLength = len(endPassword)
else:
    passwordLength = args.passwordlength
    analysis = [False, False, False, False]
    analysis[0] = args.symbols
    analysis[1] = args.numbers
    analysis[2] = args.uppercase
    analysis[3] = args.lowercase
# creates arrays based on information about the password
optionsarray = makeoptionsarray(analysis)
printedarray = makeprintedarray(passwordLength)
print(optionsarray)
print(printedarray)
# sets a target password if none was given
if not args.password:
    endPassword = ""
    for x in range(passwordLength):
        endPassword += chr(optionsarray[len(optionsarray)-2])
print("Test: " + endPassword)
# asks what type of hash encrypting is being used and updates endPassword based on what type of hash encryption is being used
# if trueorfalse("Is the password encrypted?"):
#     mdfive = trueorfalse("MD5 encryption?")
#     if not mdfive:
#         bcryptCheck = trueorfalse("BCrypt encryption?")
#         if not bcryptCheck:
#             shatwofivesix = trueorfalse("SHA-256 encryption")
#             if shatwofivesix:
#                 endPassword = hashlib.sha256(bytes(endPassword, 'utf-8')).hexdigest()
#         else:
            # gensalt sets rounds to 12, prefix to b"2b"
#             mysalt = bcrypt.gensalt()
#           endPassword = bcrypt.hashpw(bytes(endPassword, 'utf-8'), mysalt)
#    else:
#        endPassword = hashlib.md5(bytes(endPassword, 'utf-8')).hexdigest()

# changes password based on encryption pattern
if args.encryption == 'md5':
    endPassword = hashlib.md5(bytes(endPassword, 'utf-8')).hexdigest()
if args.encryption == 'bcrypt':
    # gensalt sets rounds to 12, prefix to b"2b"
    endsalt = bcrypt.gensalt()
    endbytes = endPassword.encode('utf-8')
    endhash = bcrypt.hashpw(endbytes, endsalt)
#    endPassword = bcrypt.hashpw(bytes(endPassword, 'utf-8'), mysalt)
if args.encryption == 'sha256':
    endPassword = hashlib.sha256(bytes(endPassword, 'utf-8')).hexdigest()
# if user inputted a hash, no encryption needs to be done
if args.hash:
    endPassword = args.hash
# asks for and performs dictionary attack
if args.dictionary:
    if dictionaryattack(endPassword):
        print("Password Found!")
        exit()
    print("Dictionary Attack Failed")
# cracks password, using newly created arrays
currentPassword = None
# adds one to the rightmost index of printed array
if args.bruteforce:
    while currentPassword != endPassword:
        # updates currentpassword and prints password (only for debugging purposes)
        currentPassword = ""
        for x in range(0,passwordLength):
            currentPassword += chr(optionsarray[printedarray[x]])
        if args.password:
            print(currentPassword)
        # for encrypted hashes, encrypts the current password into a hash and checks if the hashes match
        if args.encryption == 'md5':
            print("plaintext: " + currentPassword + " hash: " + hashlib.md5(bytes(currentPassword, 'utf-8')).hexdigest())
            currentPassword = hashlib.md5(bytes(currentPassword, 'utf-8')).hexdigest()
        if args.encryption == 'bcrypt':

              #  if bcrypt.checkpw(((currentpassword.replace("\n", "")).encode('utf-8')), bytes(endPassword,'UTF-8')):
                   # return True
            #
            print("testing plaintext: " + currentPassword)
            # currentBytes = currentPassword.encode('utf-8')
            if bcrypt.checkpw(((currentPassword.replace("\n", "")).encode('utf-8')), bytes(endPassword,'UTF-8')):
            # if bcrypt.checkpw(currentBytes, endhash):
                print("Password Found!")
                exit(1)
           # currentPassword = bcrypt.hashpw(bytes(currentPassword, 'utf-8'), mysalt)
        if args.encryption == 'sha256':
            # currentPassword = hashlib.sha256(bytes(currentPassword, 'utf-8')).hexdigest()
            print("plaintext: " + currentPassword + " hash: " + hashlib.sha256(bytes(currentPassword, 'utf-8')).hexdigest())
            currentPassword = hashlib.sha256(bytes(currentPassword, 'utf-8')).hexdigest()
        # adds one to the rightmost index of printed array
        printedarray[passwordLength-1] += 1
        # checks to make sure no index has reached the reset row (0)
        for x in range(passwordLength-1, 0, -1):
            if optionsarray[printedarray[x]] == 0:
                printedarray[x] = 0
                printedarray[x-1] += 1
    # prints result of attack
    if currentPassword == endPassword:
        print("Password Found!")
    else:
        print("Failed")
# Use a breakpoint in the code line below to debug your script.
# Press Ctrl+F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
