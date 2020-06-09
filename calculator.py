print("Calculator")
input1=float(input("Enter your first number :"))
input2=float(input("Enter your second number :"))
print("Operasi hitung \n 1=tambah \n 2=kurang \n 3=kali \n 4=bagi")

operasi=input("operasi yang diinginkan :")
if operasi=="1":
    print( "hasilnya adalah", input1+input2)
elif operasi=="2":
    print("Hasilnya adalah ", input1-input2)
elif operasi=="3":
    print("Hasilnya adalah ", input1*input2)
else :
    print("Hasilnya adalah", input1/input2)