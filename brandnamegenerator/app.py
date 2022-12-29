#simple python project 
print("Weclome to the Band Name Generator, \n Answer the questions to generate a Band Name")

city = ""
pet = ""
while(len(city) == 0 or len(pet) == 0):
#city you grew up ins
    city = input("What city did you grow up in?\n")
    #pets name
    pet = input("What is your pets name?\n")

if(len(city) > 0 and len(pet) > 0):
    print("Your Bands Name is " + city + " " + pet)