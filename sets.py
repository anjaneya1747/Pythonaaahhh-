'''SETS'''


# 1. empty set -> {}, set()
# 2. set is the only data structure where values cannot be duplicated
# 3. set is the  only data structure where indexing is not done, Hence, they are UNORDERED they are SUBSCRIPTABLE
# 4. It is HETEROGENOUS...   Boolean is not accepted
# 5. set is MUTABLE


'''
s = {}          #type dict aata hai by default
s = set()
print(type(s))
'''


# s = {1,2,3,4,5}
# print(type(s))

# s = {'hello',1 ,3.14,True}
# print(s)




''''Method in Sets'''


# #1. add a new value in the set
# s = {1,1,1,2,2,3,3,4,4,5,5}

# #Item adding
# s.add(100)

# #If you want to add multiple values use [] brackets and .update
# s.update([200,300,400])  
# print(s)


# #2. Removing an elemment from the set
# s = {1,1,1,2,2,3,3,4,4,5,5}

# #l.  .remove(element)
# s.remove(1)    #isme agr aisi value daali jo exist nhi krti ex. 6 it will show error
# print(s)

# s.discard(6)   #isme agr aisi value daali jo exist nhi krti ex. 6 then it will give same set
# print(s)

# #ll.  .clear (remove all elements)
# s.clear()
# print(s)




'''Advanced methods in sets'''

#1. Union -> saare elements b/w your sets
#2. Intersection ->  Dono set ke beech ke common values
#3. Difference   -> s1 mai ho but s2 mai na ho
#4. Symmetric Difference  -> Common elements ko chod ke jo bach rhe wo laa do


# s1 = {1,2,3,4,5}
# s2 = {1,6,7,8}

# print(f"Union of set1 and s2 is {s1.union(s2)}")
# print(f"Intersection of set1 and set2 is {s1.intersection(s2)}")
# print(f"Difference of set1 and set 2 {s1.difference(s2)}")
# print(f"Symmetric difference between set1 and set2 {s1.symmetric_difference(s2)}")




#Q. Convert the given list into set
l  = [1,2,1,2,1,3,3,3,4,5,6,7]
s = set()
for i in l:
    s.add(i)
print(s)
    


