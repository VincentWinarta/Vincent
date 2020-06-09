import time

print("timer")

a=int(input("Berapa detik bor:"))
a+=1
while a>1 :
    a-=1
    print(a)
    time.sleep(1)
