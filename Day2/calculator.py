user=int(input("Enter your operations(1-4):"))
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
if user==1:
    Sum=num1+num2
    print("Total value is:",Sum)
elif user==2:
    sub=num1-num2
    print("Total value is:",sub)
elif user==3:
    div=num1/num2
    print("Total value is:",div)
elif user==4:
    multi=num1*num2
    print("Total value is:",multi)
else:
    print("Wrong Operations!!")
