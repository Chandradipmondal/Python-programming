def flexi(*number):#flexible number of input ->*number means convert the input number to a tuple
    product =1
    print(number)
    print(type(number))
    for i in number:
        product*=i
    return(product)
x=flexi(1,2,3,4,5)
print(x)
