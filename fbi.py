import time

def loading():
    for x in range(3):
        for y in range (4):
            print("Loading" + "."*y)
            time.sleep(0)

def list():
    John={
        "Name"   : "John Smith",
        "Age"    : "25",
        "Crime"  : "First Degree Murder"
    }
    Billy={
        "Name"   : "Billy Brock",
        "Age"    : "30",
        "Crime"  : "Stealing"
    }
    Ethan={
        "Name"   : "Ethan Travis",
        "Age"    : "20",
        "Crime"  : "Drug Dealing"
    }
    Raymond={
        "Name"   : "Raymond Chris",
        "Age"    : "40",
        "Crime " : "Second Degree Murder"
    }
    
    names=[John,Billy,Ethan,Raymond]
    for name in names:
        print(name)

while True:
    password=input("Password in capital:")
    if password=="verena":
        print("----------------------")
        print("FBI MOST WANTED LIST")
        print("----------------------")
        time.sleep(1)
        loading()
        time.sleep(1)
        list()
        break
        
        
    else :
        print("Incorrect Password")
        

