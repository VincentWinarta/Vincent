print("Tebak angka:")
jawaban=random.randint(1,10)
x="Tebak dong :"
while True:
    tebak=int(input(f'{x}'))
    if tebak>jawaban:
        print("Tua amat gw!")
    elif tebak<jawaban:
        print("Kemudaan dong !")
    else :
        print("Betul sekali !!!")
        break
    x="Tebak lagi dong :"

