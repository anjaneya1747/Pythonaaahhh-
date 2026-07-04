# Data Structures(Advanced data types):-

# 1. List
# 2. Dictionary
# 3. Tupes
# 4. Set







# #1. List
# '''
# denoted by -> [] Square Brackets
# 1. Heterognous Data Structure - multiplle type ke data ko store krwa skte ho
# 2. Duplicacy is allowed 
# 3. list is ordered
# 4. Mutable :- We can change the value in the list
# '''

# # l = [] Empty list
# l = [10,20,30,40,50]
# print(l)
# print(type(l))

# #you can assign in a list using assignment operator
# l = [10,20,30,40,50]
# l[3] = 400   # list ke 3 index pr 400 ko assign kr diya (item assignment)
# #l[5] = 100 index out of range
# print (l)




# #Item wise loop
# l = [10,20,30,40,50]
# for i in l:
#     print(i)

# #Index wise loop
# for i in range(len(l)): #i -> 0,1,2,3,4
#     print(i, l[i])
#     #i-> index of list
#     #l[i]-> item at index







#Q. print items that are greater than 15 and also index that are greater than 15
# l = [1,67,10,25,14,77]
# for i in l:
#     if i>15:
#         print(i)
# for i in range(len(l)):
#     if l[i]>15:
#         print(i)







# #Q. Sum all the element of the list
# l = [10,20,30,40,50]
# sum = 0
# for i in l:
#     sum +=i
# print(sum)





# #Slicing
# #[Start=0: Stop-1:Step=1]
# l = [10,20,30,40,50]
# print(l[1:4:1])  #String



#Methods in list       (kisi bhi function ke aage . lg gya to wo methood hai ex: .append())

# #1. .append()      -> Adds element at the last.... do alue ek saath add nhi kr skta
# l = [10,20,30,40,50]
# l.append(100)
# print(l)

# #2.  .extend()         -> l2 list l1 ke aage add ho jaygi
# l1 = [10,20,30,40,50]
# l2 = [60,70,80]
# l1.extend(l2)          
# print(l1)
# print(l1+l2)

# #3.  .insert(index,value)       -> index ki current value pr given value aa jaygi
# l1 = [10,20,30,40,50]
# l1.insert(1,100)
# print(l1)

# #4.  .pop()         -> to remove a value of given index... default pr ye last ko remove karega
# l1 = [10,20,30,40,50]
# l1.pop(1)
# print(l1)

# #5.  .remove(element)         -> remove or pop mai diff. remove mai value dete hai or pop mai index
# l1 = [1,5,5,5,4,3,2]    
# l1.remove(5)      #agr duplicate value hai toh first occurange remove
# print(l1)

# #6. len()  -> list length
# l1 = [1,5,5,5,4,3,2]
# print(len(l1))






# #Q. Accept list elements and reprint it

# #part 1 Accept elements
# n = int(input("Enter the size of the list: "))   #5
# l = []
# for i in range(n):  #0,1,2,3,4,
#     element = input(f'Enter element {i} for your list: ')
#     l.append(element)
# print(l)




# #Q2. Reverse a list without using slicing
# l1 = [1,2,3,4]
# l1.reverse()
# print(l1)


# #Q3. Print positive and nnegative values of a list
# l1=[10,20,-30,45,-23,-90]
# for i in l1:
#     if i>1:
#         print("It is positive")
#     else:
#         print("It is negative")









#Ques. You have a list [1,2,3,4,5] and you have a variable k = 2 and you just have to rotate the list by k elements.
"""
l = [1,2,3,4,5]
k = 3
for i in range(k):
    last=l[-1]   #Storing last value of the list

    for j in range(len(l)-1,0,-1):
        l[j] = l[j-1]
    l[0] = last
print(l)
"""



