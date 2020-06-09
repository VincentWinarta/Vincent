import time

def loading():
    for x in range(3):
        for y in range (4):
            print("Loading" + "."*y)
            time.sleep(0.3)

def list():
    John={
        "Name"   : "Name    : John Smith",
        "Age"    : "Age     : 25",
        "Crime"  : "Crime   : First Degree Murder"
    }
    Billy={
        "Name"   : "Name    : Billy Brock",
        "Age"    : "Age     : 30",
        "Crime"  : "Crime   : Stealing"
        }
    Ethan={
        "Name"   : "Name    : Ethan Travis",
        "Age"    : "Age     : 20",
        "Crime"  : "Crime   : Drug Dealing"
        }
    Raymond={
        "Name"   : "Name    : Raymond Chris",
        "Age"    : "Age     : 40",
        "Crime"  : "Crime   : Second Degree Murder"
        }
    
    dicts=[John,Billy,Ethan,Raymond]
    print(len(dicts), "IDENTIFIED")
    for dict in dicts:
        print(dict["Name"])
        print(dict["Age"])
        print(dict["Crime"])
        print("")

while True:
    password=input("Password:")
    password1=password.upper()
    if password1=="VERENA":
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
        

