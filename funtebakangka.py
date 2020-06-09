

def angka1():
    angka=input("Tebak aku dong antara 1-9:")
    return angka
    if cek(angka):
        return int(angka)
    else:
        print("Invalid")
        angka1()

        
def cek(angka2):
    try:
        angka=int(angka2)
    except: 
        return False
    return 1<=angka<=9

        
    
def run():
    print("Games Tebak Angka :")
    
    
    while True:
        angka=int(angka1())
        if angka>5:
            print("Kegedean bos")
        elif angka<5:
            print("Terlalu mungil")
        else :
            print("Jawaban benar")
            break
    
run()

