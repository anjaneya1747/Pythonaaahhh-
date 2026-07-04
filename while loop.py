#While loop -> condition true hai.
# we have to make while condition false at some point otherwise it willl become infinite loop


# i = 0
# while i <11:  #jb tk condition true hai while will keep executing
#     if i == 5:
#         break
#     print(i)
#     i += 1



# num = 1054
# sum = 0
# while num>0:   #print(1054 % 10)
#     print(num % 10)  #last digit ko print karega
#     num = num // 10  #last digit ko one by one remove karega
   



# num = 1054
# sum = 0
# while num>0:   #print(1054 % 10)
#     last = num % 10  #last digit ko print karega
#     num = num // 10  #last digit ko one by one remove karega
#     sum = sum + last
# print("sum of num is",sum)





# #Q30. Check a no. is pallindrome or not?
# num = 1221
# copy = num

# reverse = 0
# while num>0:
#     last = num %10
#     reverse = reverse * 10 + last
#     num = num // 10

# if copy == reverse:
#     print(f"{copy} is a palindrome no.")
# else:
#     print(f"{copy}is not a palindrome no.")




# #Q. number is armstrong or not.   (agr koi number hai and apn uske no. of digit ke sum ko sabke power mai chadhake add kaenge, agr wo sum same hai then no. is armstrong )
# num = int(input("Enter your no:")) #ex. 153
# copy = num
# power = len(str(num))
# sum = 0
# while num>0:
#     last = num%10
#     sum = sum + last**power
#     num = num//10
# if copy == sum:
#     print(f'{copy} is an armstrong number')
# else: 
#     print(f"{copy} is not an armstrong no.")





# #Q. Perfect numbers 
# num = 6
# sum = 0
# for i in range(1,num):
#     if num % i == 0:
#         sum = sum + i
# if sum == num:
#     print(f"{num} is a perfect number")
# else:
#     print(f"{num} is not a perfect number")
     



# #Q. print * pattern
# #   *
# #   **
# #   ***
# #   ****
# #   *****
# rows = 5
# for i in range(1,rows+1):
#     print("*" * i)