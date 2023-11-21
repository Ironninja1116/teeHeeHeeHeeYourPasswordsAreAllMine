# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import hashlib
import bcrypt
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


# MAIN
# Automatically sets hash values to false as default, important later
mdfive = False
bcryptCheck = False
shatwofivesix = False
# Asks whether user will be inputting a password or if they want the program until the end
inputtingPassword = trueorfalse("Will you provide a password? ")
# Automatically picks up features about password if given, asks user for these features if the password is not given
if inputtingPassword:
    endPassword = input("Please input a password: ")
    print(endPassword)
    analysis = analyzecharacters(endPassword)
    passwordLength = len(endPassword)
else:
    passwordLength = int(input("(ENTER AS NUMBER) How many characters long is the password? "))
    analysis = [False, False, False, False]
    analysis[0] = trueorfalse("Does the password contain symbols? (such as $, *, !, etc)")
    analysis[1] = trueorfalse("Does the password contain numbers?")
    analysis[2] = trueorfalse("Does the password contain uppercase characters?")
    analysis[3] = trueorfalse("Does the password contain lowercase characters?")
# creates arrays based on information about the password
optionsarray = makeoptionsarray(analysis)
printedarray = makeprintedarray(passwordLength)
print(optionsarray)
print(printedarray)
# sets a target password if none was given
if not inputtingPassword:
    endPassword = ""
    for x in range(passwordLength):
        endPassword += chr(optionsarray[len(optionsarray)-2])
print("Test: " + endPassword)
# asks what type of hash encrypting is being used and updates endPassword based on what type of hash encryption is being used
if trueorfalse("Is the password encrypted?"):
    mdfive = trueorfalse("MD5 encryption?")
    if not mdfive:
        bcryptCheck = trueorfalse("BCrypt encryption?")
        if not bcryptCheck:
            shatwofivesix = trueorfalse("SHA-256 encryption")
            if shatwofivesix:
                endPassword = hashlib.sha256(bytes(endPassword, 'utf-8')).hexdigest()
        else:
            # gensalt sets rounds to 12, prefix to b"2b"
            mysalt = bcrypt.gensalt()
            endPassword = bcrypt.hashpw(bytes(endPassword, 'utf-8'), mysalt)
    else:
        endPassword = hashlib.md5(bytes(endPassword, 'utf-8')).hexdigest()
# cracks password, using newly created arrays as
currentPassword = None
# adds one to the rightmost index of printed array
while currentPassword != endPassword:
    # updates currentpassword and prints password (only for debugging purposes)
    currentPassword = ""
    for x in range(0,passwordLength):
        currentPassword += chr(optionsarray[printedarray[x]])
    # updates current password based on has encryption
    if mdfive:
        currentPassword = hashlib.md5(bytes(currentPassword, 'utf-8')).hexdigest()
    if bcryptCheck:
        currentPassword = bcrypt.hashpw(bytes(currentPassword, 'utf-8'), mysalt)
    if shatwofivesix:
        currentPassword = hashlib.sha256(bytes(currentPassword, 'utf-8')).hexdigest()
    print(currentPassword)
    # adds one to the rightmost index of printed array
    printedarray[passwordLength-1] += 1
    # checks to make sure no index has reached the reset row (0)
    for x in range(passwordLength-1, 0, -1):
        if optionsarray[printedarray[x]] == 0:
            printedarray[x] = 0
            printedarray[x-1] += 1

# Use a breakpoint in the code line below to debug your script.
# Press Ctrl+F8 to toggle the breakpoint.
# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
