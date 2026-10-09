# Try it yourself
weight = float(input("Enter the value of weight"))
height = float(input("Enter the value of height"))
bmi = weight / (height**2)
print(bmi)
if bmi>=30:
    print("Obses")
elif bmi>=25:
    print("Overweight")
elif bmi >=18.5:
    print("Normal")
elif bmi<18.5:
    print("Underweight")
else:
    print("PLease enter Correct input")