# #Q1.
# percentage = int(input("Enter the percentage:-"))

# if percentage>=80:
#     print("Grade A+")
# elif percentage >=70 and percentage<80:
#     print("Grade A")
# elif percentage>=60 and percentage<70:
#     print("Grade B")
# elif percentage>=50 and percentage<60:
#     print("Grade C")
# else:
#     print("Fail")



# #Q2.
# num = int(input("Enter your no.:-"))
# copy = num
# reverse = 0
# while num>0:
#     last = num%10
#     num = num //10
#     reverse = reverse *10 +last
# if reverse == copy:
#     print(f"{copy}is a pallindrome")
# else:
#     print(f"{copy} is not a pallindrome")





# #Q.3.
# def factorial(n: int):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i  #Shorthand operator
#     return fact
# print(factorial(5))




# #Q5.
# for i in range(1,51):
#     if i%3==0 and i %5==0: 
#         print(i)



#Q4.
a = int(input("Enter a starting number"))
b = int(input("Enter a ending number"))
count_even = 0
count_odd = 0
for i in range(a,b+1):
    if i%2==0:
        count_even = count_even + 1