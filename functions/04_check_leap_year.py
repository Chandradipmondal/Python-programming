def is_leap(year):
    leap = False
    year = int(input("Enter year"))
    if year%4==0:
        if year%100==0:
            if year%400==0:
                leap = True
            else :
                leap = False
        else :
            leap = True
    return leap

year = 3000
a = is_leap(year)
print(a)