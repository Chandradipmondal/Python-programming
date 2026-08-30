email = input("Write your email")
if '@' in email :
    password = input("Write your password")
    if email == 'chandradipmondal07@gmail.com' and password == '1234':
        print("Welcome")
    elif email == 'chandradipmondal07@gmail.com' and password != '1234':
        print('Password is wrong try again')
        password = input('Re-enter password')
        if password =='1234':
                print("Password is correct")
        else:
                print('password is incorrect')
    else:
        print("error")
else:
    print("your entered email is incorrect")
 
