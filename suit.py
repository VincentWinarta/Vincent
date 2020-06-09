import random

lawan = random.choice(["Gunting","Kertas","Batu"])
print("Permainan Suit:")
print('-----------------')


count_menang=0
count_kalah=0



def menangs():
    global count_menang
    print("Yeay menang")
    count_menang+=1
def kalah():
    global count_kalah
    print("Yah kalah deh")
    count_kalah+=1
def seri():
    print("Seri dong")

def menu():
    print("1=Gunting")
    print("2=Kertas")
    print("3=Batu")
    jawab=input("Pilih (1/2/3/exit) :")
    return jawab

jawab=menu()
while jawab!="exit":
    
    if jawab=="1" and lawan=="Gunting":
        seri()
    elif jawab=="1" and lawan=="Kertas":
        menangs()
    elif jawab=="1" and lawan=="Batu":
        kalah()
    elif jawab=="2" and lawan=="Gunting":
        kalah()
    elif jawab=="2" and lawan=="Kertas":
        seri()
    elif jawab=="2" and lawan=="Batu":
        menangs()
    elif jawab=="3" and lawan=="Gunting":
        menangs()
    elif jawab=="3" and lawan=="Kertas":
        kalah()
    elif jawab=="3" and lawan=="Batu":
        seri()
    
    jawab=menu()

print("Lawan mu :" , lawan)
print("Total menang : ", count_menang)
print("Total kalah : ", count_kalah)