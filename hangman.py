h={"h":"H"}
i={"i":"I"}
a={"a":"A"}
words=[h,a,i]
for word in words:
    print(word)

answer=input("Enter your letter :").lower()

if answer not in words:
    print("Your are wrong") 
    

