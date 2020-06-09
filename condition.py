print("Salary")
input1=int(input("Enter your working hours: "))
input2=int(input("Enter your rate per hours: "))

if input1>40 :
    print('Your salary is ' + str((input1*input2)+500) )
else :
    print('Your salary is ' + str(input1*input2))
py