# import random #random library is a library jo ki random no. generate karvaati hai within the range

# number = random.randint(1,100) #45 #randint hume random integers value dega within the range
# count = 0

# while count<5:
#     count += 1
#     user = int(input("Enter your number:"))#21
#     if user == number:
#         print("Yeeeeeee kahi to chl rhi hai kismat!!")
#         print(f"You  took {count} chances to win")
#         break
#     elif user < number:
#         print(f"Too low, guess higher value")
#     elif user > number:
#         print("Too high,guess lower value")
# print(f"Game over!! chutiye computer ne {number} guess kiya tha.")


#User have only 5 chances annd if those chances are over either he will win or loose


# Streamlit   -> To generate UI
#CLI    -> Command Line 






import random 

number = random.randint(1,100) 

count =  0

print("You have only 5 chances to guess the number!")


while count < 5:  

    count += 1

    user = int(input("Enter your number:"))

    if user == number:

        print("YUPEEEEEE!!!! YOU WON!!")

        print(f"You took {count} chances to win!")

        break

    elif user > number:

        print("Too high!! Guess low.")

    elif user < number:

        print("Too low!! Guess high.")


print(f"OOPPSIIEEEEE!!!!! YOU LOST !!! The actual number is{number}")