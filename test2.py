# Q1. Factorial Using Recursion
# Write a Python function to find the factorial of a given number using recursion.

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i 
    return fact 
print(factorial(5))


# Q2. Prime Numbers in a Range
# Write a Python program that accepts two numbers and prints all the prime numbers between them




def prime(a,b):
    for i in range(a,b+1):
        count = 0
        for j in range(1,i+1):
            if i % j == 0:
                count += 1
            if count == 2:
                print(i)
prime(1,10)

        


# Q3. Count Vowels Using Function
# Write a function that accepts a string and returns the total number of vowels present in it


def count_vowel(st):
    count = 0
    for ch in st("aeiou"):
        count +=1
        print(count)
count_vowel("abcf")








# Q4. Armstrong Number Using Function
# Write a Python function that accepts a number and checks whether it is an Armstrong Number or not





# Q5. Sum of Digits Using Function
# Write a function that accepts a number and returns the sum of its digits.

def number(num):
    sum = 0
    while num>0:
        last = num % 10
        sum = num + last
        last = num // 10
        return(sum)

print(number(441))

