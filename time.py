import time
print("timer")
print("1:Jam \n 2:Menit \n 3:Detik")
jenis=int(input("Dalam satuan apa bor : "))
waktu=int(input("Berapa lama bos :"))
if jenis==1:
    time.sleep(waktu)
elif jenis==2:
    time.sleep(waktu*60)
else :
    time.sleep(waktu*3600)

print("Kelar")