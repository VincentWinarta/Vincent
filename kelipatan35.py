list1=list(range(1,100))
print(list1)
total=int(0)
print("")
list2=[]
for x in list1:
    if x%3==0 or x%5==0:
        list2.append(x)

        total+=x

print(list2)

print("Total :", total)

