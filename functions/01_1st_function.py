def is_even(number):
    if type(number) is int:
        if number%2==0:
            return "Even"
        else:
            return "Odd"
    else:
        return "Not allowed"
x = is_even(4)
print(x)