'''Pattern printing'''

# #Q. Print
# # '''
# # *
# # **
# # ***
# # ****
# # *****
# # '''

# for i in range (1,6):
#     print(i* "*")



# #Q. take no. of rows from user

# rows = int(input("Enter number of rows: "))

# for i in range(1,rows+1):
#     print(i * "*")





# #Q. Print
# # '''
# # *****
# # ****
# # ***
# # **
# # *
# # '''


# rows = int(input("Enter number of rows: "))

# for i in range(rows,0,-1):
#     print(i * "*")





# #Q. Print
# 1
# 22
# 333
# 4444
# 55555

# for i in range(1,6):   #i->3
#     for j in range(i): #j->i->0,1,2
#         print(i, end=" ")  #end=" " value ko same line pe print krwata hai
#     print()   #ye line change kr rha hai pura comlete hone ke baad

# #ye ek line mai bhi ho skta hai

# for i in range(1,6):
#     print(str(i)*i)
# [
#     str(i) * i 
#     i -> "1" * 1 -> "1"
#     i -> "2" * 2 -> "2 2"
#     ....
# ]





# #Print
# 55555
# 4444
# 333
# 22
# 1

# for i in range (5,0,-1):
#     print(str(i)*i)