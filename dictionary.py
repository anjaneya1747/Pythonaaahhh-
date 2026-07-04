













# #5.  .get()   -> gives you value of a key and if not present guives you None
# d = {'a':100,'b':200,'c':300}
# print(d.get('d'))









# #6.  .update({key:value})
# d = {'a':100, 'b':200, 'c':300}
# d.update({'c':500})
# print(d)




# #7.   clear()   -> removes all the elements
# d = {'a':100,'b':200,'c':300}
# d.clear()
# print(d)




# del d  #permanently deletes
# print(d)



# #Q!. We have two lists and we have to make list1 as key of the dict and list2 as values

# l1 = ['a', 'b', 'c', 'd']
# l2 = [10, 20, 30, 40]

# d = {}
# for i in range(len(l1)):   #i 0123
#     d[l1[i]] = l2[i]       #item assignment
# print(d)






# #Q2. yau have a list make the indexes as the key and elements present on those indexes as values
# #     0  1  2  3  4   -> Keys
# l = [10,20,30,40,50]
# d ={}
# for i in range






#Q3.   merge 2 dictionaries                     #isko update se krna 1 line mai ho jaygga
d1 = {'a':10, 'b' :20}
d2 = {'c':30, 'd' :40}

for i in d2:      #i ke andr keys aayngi  -> c,d
    if i  not in d1:    #c not in d1, mtlb if ho gya true
        d1[i] = d2[i]
print(d1)





#Q4. Frequency count
l = [1,1,1,1,2,2,3,4,5,5,6,6,7,1,3,4,3,2,2,1,4]
d = {}  #1:4, 2:3
for i in l:
    if i not in d:   #1 not in d
        d[i] = 1
    else:
        d[i] += 1
print(d)




                

  