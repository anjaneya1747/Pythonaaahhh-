"""
args - accepts argumemt in the form of tuple and gives output also in the form of tuple
symbol -> "*"
# * lagane se saare arguments ek baar mein function ke andar aa jaayenge
"""
# def add(*chacha):
#     for i in chacha:
#         print(i)

# add(10,20,30)

# def add(*chacha): #a = 10,20,30
#     sum = 0
#     for i in chacha:
#         sum += i
#     return sum

# print(add(10,20,30))

"""
kwargs - data accept and return in the form of dictionary
symbol -> **
"""

# def info(**details):
#     print(details)
# info(name= 'chacha',age= 40, gender='M' ,address= 'Bhopal' )
# info(name= 'chacha',age= 40, gender='M' ,address= 'Bhopal' , wife= 'chachi')  # we can as many keys and values as we want


#print keys and values separately

# def info(**details):
#     for key, value in details.items():
#         print(key,value)
# info(name= 'chacha',age= 40, gender='M' ,address= 'Bhopal' , wife= 'chachi') 

"""
lamda function -> when we have to write function just in single line 
"""
# add = lambda a,b: a + b  # we have to define a and b unless rest of the code will not execute
# print(add(10,20))  


#Make a lambda function which accepts two variables as a = 2 and b = 3 but give output as a^b 
# power = lambda a,b: a**b
# print(power(2,3))
