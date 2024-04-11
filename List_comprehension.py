templist= [10,20,30,40,50,60,70,80,90]
new_list= [ i/2 for i in templist ]
print(new_list)

another_list=[-1,-2,-7,-9,-10,4,-2,-5,8,3,9]
new_new_list= [i**2 for i in another_list if i <0]
print(new_new_list)
arr = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]
for i in range(0, 4):
    print(arr[i].pop())

    fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
 
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'
 
sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20
 
print(sum)
