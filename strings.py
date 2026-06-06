# #Q31. 
# name = "mohit"
# print(name[::-1])
# print(len(name))
# print(name.upper())
# print(name.lower())






#Q32. 
name = "PyThon"
lower = ""
upper = ""
for i in name:
    if i.islower():  # . se check kr rhe hai if number is lower or not if yes then if work karega
        lower = lower + i
    else:
        upper = upper + i
print(lower + upper)
    

