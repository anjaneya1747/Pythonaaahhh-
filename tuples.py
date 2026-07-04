'''Tuples'''

#1. (Paranthesis) -> Emptry Tuple
#2. Tuples are ordered -> indexinng is done
#3. Tuples are Heterogenous 
#4. Tuples are Immutable(does not support item assignment)
#5. Tuples can have duplicate values
#6. As there is indexing so slicing can be done

# t = (1,2,"Hello",True,3.14)    #Immutable
# t[2] = 10
# print(t)



# a = 1,2,3,4
# print(a)
# print(type(a))

# print(a[1:7])  #[start:stop-1:step]

a = (1,1,1,1,2,2,3,4,5,6,7,8)


print(a.count(1))     # .count() will count the  occurance of any value    

print(a.index(1))     # First occurance of index

