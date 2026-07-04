# #for loop for strings
# a = "SHERYIANS" 
# for i in range(9):
#     print(a[i])




# #count number of factors
# count = 0
# num = 10 
# for i in range(1,num+1):
#     if num % i == 0:
#         count = count + 1 #this is same as count += 1
#         print("factors of number", num, "is",count)    



# #count number of factors of prime number
# count = 0
# num = 17
# for i in range(1,num+1):
#     if num % i == 0:
#         count = count + 1 #this is same as count += 1

# if count==2:
#     print(f"{num}is a prime number")
# else:
#       print(f"{num}is not a prime number")




# #Q 25
# sum = 0
# num = int(input("enter a number:"))
# for i in range(1,num+1):
#     if num % i == 0:
#         sum = sum + i
# print("sum of factors is ", sum)



# #Q. Print prime numbers from 1 to 50
# for i in range(1,51):
#     count = 0
#     for j in range(1,i+1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         print(i)



# #Q26. to print numbers vertically
# num = 1024
# num2 = str(num)
# for i in num2:
#     print(i)