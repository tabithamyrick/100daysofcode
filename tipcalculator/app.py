#simple python project 
print("PyTip - a Python Tip Calculator")
#get check ammount
checkAmount = 0
while(checkAmount <= 0):
    checkAmount = float(input("Enter Check Total: \n"))
#get number of people
checkSplit = 0
while(checkSplit <= 0):
    checkSplit = float(input("Number of people to Split The Check: \n"))
#get tip percentage amount
tipPercentage = 0
while(tipPercentage <= 0):
    tipPercentage = (float(input("Enter the Tip Percetnage, 15, 20, 25 etc: \n"))/100)
#calulate and print total amountclear
paymentAmount = (checkAmount * (1.00 + tipPercentage)) / checkSplit
print("The Amount Per Person is - $ %.2F" % paymentAmount)