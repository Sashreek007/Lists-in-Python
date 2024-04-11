tempList= [1,2,3,4,5]
import random

fruit = ['apple', 'banana', 'papaya', 'cherry']
random.shuffle(fruit)
print(fruit)


def access_element(list,index):
    if index >= len(list):
        print("Not possible")
    else:
        print(list[index])
access_element(tempList,2)

def traveral_element(list):
    for i in list:
        print(i)
traveral_element(tempList)

for i in range(len(tempList)):
    tempList[i]= tempList[i] +1
    print(tempList[i])

a=[1,2,3,4,5]
print(a[3:0:-1])

def f(value, values):
    v = 1
    values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])

fruit=['apple', 'banana', 'papaya', 'cherry']
random.shuffle(fruit)
print(fruit)