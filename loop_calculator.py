print("Calculate")
print("----------------")
x=1
total=int(0)
count=int(0)
num=[]
while True:
    angka=str.lower(input(f'Masukan angka {x} :'))
    if angka!="done":
        x+=1
        angka=int(angka)
        total+=angka
        count+=1
        num.append(angka)
        maks=max(num)
        mini=min(num)
    else :
        break
print("Jumlah : ", total)
print("Total angka : ",count)
print("Nilai Maksimum : ", maks)
print("Nilai Minimun : ", mini)
print("Nilai Rata-rata : ", (total//count))

