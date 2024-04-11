templist= [10,20,30,40,50,60,70,80,90]

def linear_search(list,target):
    for i in range(len(templist)):
        if list[i]==target:
            return i
    
    return -1
print(linear_search(templist,70))

del templist[:2]
print(templist)

