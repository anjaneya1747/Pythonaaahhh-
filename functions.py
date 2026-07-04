# #function ka naam = variable naam

# def greet():   #Function defining
#     name = input("Enter your name:")
#     print(f"hello {name}!")
# greet()      #Function call  





# def greet(name):    #Parametres
#     print(f"hello {name}!")
# greet("Vinii")      #Arguments




# #Q. Print greatest between two variables
# def greatest():
#     a = 10
#     b = 5
#     if a>b:
#         print(f"{a} is greater than {b}")
#     elif a<b:
#         print(f"{b} is greater than {a}")
#     else:
#         print("both are equal")
# greatest()




# def pallindrome(name):
#     reverse = name[::-1]
#     if name == reverse:
#         print(f"{name} is a palindrome")
#     else:
#         print(f"{name}is not a palindrome")
# pallindrome("madam")






# #return statement

# def add():
#     a = 10
#     b = 20
#     c = a+ b
#     return c   # return value ko function mai save kr dega, print krna padhega
# print(add())





# def greet():
#     return "Hello"
#                            #Ek function ke andr doosre function ko call kr rhe hai
# def add():
#     print(greet())
#     a = 10
#     b = 20 
#     return a + b
# print(add())







# def add(a,b):                #Function define krte time parameterrs
#     print(a+b)
# add(10,20)                   #Function call kete time arguments

# def add(a,b):
#     return(a+b)
# print(add(10,20))






#Positional parameteres


# #Type Hinting
# #syntax:- function(variable : type)


# def add(a : int, b : int):               
#     print(a+b)
# add(10,20.5)               #we are not converting we are just hinting


# #Default Parameter
# #What if b ki default value 0 predefine kare, then the code will be


# def add(a,b=0):                #Default Parameter  
#     print(a+b)
# add(10)  
# add(10,20)




# #Q. Accept an Parameter named as 'n' and print factorial of 'n' using function

# def factorial(n: int):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i  #Shorthand operator
#     return fact
# print(factorial(5))








# #Keyword parameters

# def info(name, gender, age, address):
#     print(name)
#     print(gender)
#     print(age)
#     print(address)
# info(name="Mukesh", gender="M", age="52", address="Bhopal")

  
        


# #Check if a number is palindrome or not using keyword argument


# def pallindrome(num):
#     copy = num
#     reverse = 0
#     while num>0:
#         last = num %10
#         reverse = reverse * 10 + last
#         num = num // 10

#     if copy == reverse:
#         print(f"{copy} is a palindrome no.")
#     else:
#         print(f"{copy}is not a palindrome no.")

# pallindrome(num = 1221)







# #Recursion      
# def display(num):
#     if num>10:
#         return     #in this condition return works like break
#     print(num)
#     display(num+1)     #Function calling itself
# display(1)



# def display(num):
#     if num<1:
#         return     #in this condition return works like break
#     print(num)
#     display(num-1)     #Function calling itself
# display(10)






# # #Q. Factorial

# def factorial(n: int):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i  #Shorthand operator
#     return fact 
# print(factorial(5))

# #Using if else condition and recursion
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factorial(num-1)
# print(factorial(5))


# #These topics are skipped
# 1. lambda function
# 2. args (interview)
# 3. kwargs (interview)   







#Revision



# def multiply(a,b=0):                #Default Parameter  
#     print(a*b)
#     return

# multiply(10**2)  
# multiply(10,20**2)








#Pallindrome
#Prinme no.
#factors using funct