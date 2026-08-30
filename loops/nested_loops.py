#num = int(input("Enter how many star should print"))
#for i in range(1,num + 1):
 #   print("*"*i)
num = int(input("Enter how many star should be print"))
for i in range(1,num + 1):
    for j in range(0,i):
        print("*",end = " ")
    print("")