import string
import random as rand
import re

pwdOptions = [list(string.ascii_letters), list(string.digits), list(string.punctuation)]

pwdLength = 0
pwdComplexity = 0
while pwdLength < 8 or pwdLength > 20:
    pwdLength = int(input("Welcome to the PyPasswordGenerator.\nEnter Password Length(8 to 20): "))
while(pwdComplexity == 0):
    pwdComplexity= int(input("Use Letters(1), and Numbers(2), and Special Charactors(3): "))

pwdString = ""
while len(pwdString) < pwdLength:
    optionsIndex = rand.randint(0, pwdComplexity - 1)
    subListLength = len(pwdOptions[optionsIndex])
    charIndex = rand.randint(0, subListLength - 1)
    selectedChar = pwdOptions[optionsIndex][charIndex]
    invalidChar = re.match("[`&()*:;'<=>^{}]", selectedChar)
    if(invalidChar == None): 
        pwdString += selectedChar
    else:
        continue

print(pwdString)
