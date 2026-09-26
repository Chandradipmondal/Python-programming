num = int(input("Enter a number: "))
i = 2
prime = True

if num < 2:
    prime = False
else:
    while i < num:
        if num % i == 0:
            prime = False
            break
        i = i + 1

if prime == True:
    print("The number is Prime")
else:
    print("The number is Not Prime")