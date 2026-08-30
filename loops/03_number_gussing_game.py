import random
jakpot = random.randint(1,300)
count = 1
number = int(input("Enter the number that you guess:\n"))
while number != jakpot:
    if number < jakpot:
        print("Guess higher")
    else:
        print("Guess Lower")
    number = int(input("Wrong enter the number:\n"))
    count += 1
print("WOW! you guess the right number")
print("You guess the number", count,"attempt")
    
