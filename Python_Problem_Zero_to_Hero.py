1) Addition of Two Numbers
Code:
a=int(input())  
b=int(input())  
sum=a+b  
print(sum)  
Review: ✅ (Correct)

2) Check Even or Odd
Code:
n=int(input())  
if n%2===0:  
    print("even")  
else:  
    print("odd")  
Review: ✅ (correct)

For checking even or odd, use if n % 2 == 0: for even and else: for odd.
Corrected Output:
Input: 8 → even
Input: 5 → odd

3) Find the Largest of Two Numbers
Code:

a=int(input())  
b=int(input())  
if a>b:  
    print(a)  
else:  
    print(b)  
Review: ✅ (Correct)

4) Swap Two Numbers Without Using a Third Variable
Code:

a=int(input())  
b=int(input())  
a,b=b,a  
print(a,b)  
Review: ✅ (Correct)

5) Find the Square of a Number
Code:

a=int(input())  
c=a*a  
print(c)  
Review: ✅ (Correct)

6) Convert Celsius to Fahrenheit
📌 Problem: Write a program that converts a temperature from Celsius to Fahrenheit.
🔹 Formula: F = (C * 9/5) + 32

🔹 Input:
25
🔹 Output:
77.0

# Celsius to Fahrenheit conversion
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{fahrenheit:.1f}")

7) Simple Interest Calculator
📌 Problem: Write a program to calculate simple interest.
🔹 Formula: SI = (P * R * T) / 100

🔹 Input:
1000 5 2
🔹 Output:
100
# Simple Interest calculation
P, R, T = map(float, input("Enter Principal, Rate, and Time: ").split())
SI = (P * R * T) / 100
print(f"{SI:.1f}")

8) Check if a Year is a Leap Year
📌 Problem: Write a program to check whether a given year is a leap year.

🔹 Input:
2024
🔹 Output:
Leap Year
🔹 Input:
2023
🔹 Output:
Not a Leap Year

# Leap Year Checker
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


9) Find the Greatest of Three Numbers
📌 Problem: Write a program to find the largest number among three given numbers.

🔹 Input:
5 12 7
🔹 Output:
12
# Finding the largest number among three
a, b, c = map(int, input("Enter three numbers: ").split())
print(max(a, b, c))


10) Calculate the Area of a Circle
📌 Problem: Write a program to calculate the area of a circle given its radius.
🔹 Formula: Area = π * r²

🔹 Input:
5
🔹 Output:
78.5
CODE:
# Circle Area Calculation
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print(f"{area:.1f}")

 11)Check if a Number is Positive, Negative, or Zero
📌 Problem: Write a program to check if a given number is positive, negative, or zero.

🔹 Input:
5
🔹 Output:
Positive
🔹 Input:
-3
🔹 Output:
Negative

🔹 Input:
0
🔹 Output:
Zero

SOURCE CODE:
num = int(input("Enter a number :"))
if num>0:
    print("Positive number")
elif num==0:
    print("Zero")
else:
    print("Negetive")

12) Sum of First N Natural Numbers
📌 Problem: Write a program to calculate the sum of the first N natural numbers.

🔹 Formula: Sum = n * (n + 1) / 2

🔹 Input:
10
🔹 Output:
55
Method - 1
num=int(input())
sum1=num*(num+1)/2
print(int(sum1)

Method-2 
num=10 
sum1=0 
for i in range(num+1):
    sum1+=i 
print(sum1)

13) Multiplication Table of a Given Number
📌 Problem: Write a program to print the multiplication table of a given number.

🔹 Input:
3
🔹 Output:
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
...
3 x 10 = 30

Method - 1
num=3 
for i in range(1,11):
   print(num,"x",i,"=",num*i)

Method-2 
num=3
i=1 
while i<=10:
    print(num,"x",i,"=",num*i)
    i+=1

14) Factorial of a Number
📌 Problem: Write a program to calculate the factorial of a number.

🔹 Input:
5
🔹 Output:
120

Method-1 
num=5 
fact=1 
for i in range(1,num+1):
    fact=fact*i 
print(f"factorial of {num} is : {fact}")


    
15) Reverse a Given Number
📌 Problem: Write a program to reverse the digits of a number.

🔹 Input:
1234
🔹 Output:
4321

Method-1 

num=1234
b=str(num)
rev=b[::-1]
print(rev)

Method-2 
num=1234 
temp=num 
rev=0
while temp>0:
    rem=temp%10 
    rev=rev*10+rem 
    temp//=10 
print(rev)

16) Check if a Number is Prime
📌 Problem: Write a program to check if a given number is prime.

🔹 Input:
7
🔹 Output:
Prime
🔹 Input:
10
🔹 Output:
Not Prime


SOURCE CODE:
def is_prime(num):
    if num<=1:
        return False 
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True 
num=int(input())
if is_prime(num):
    print("prime")
else:
    print("not prime")



18) Find the Greatest Common Divisor (GCD)
📌 Problem: Write a program to find the GCD of two numbers.

🔹 Input:
8 12
🔹 Output:
4

Source code:

def Gcd(a,b):
    while b:
        a,b=b,a%b 
    return a 
a,b=map(int,input().split(" "))
print(Gcd(a,b))


18) Check if a String is a Palindrome
📌 Problem: Write a program to check if a given string is a palindrome.

🔹 Input:
madam
🔹 Output:
Palindrome
🔹 Input:
hello
🔹 Output:
Not a Palindrome

Method - 1
name = input()
pal = name[::-1]
if pal == name:
    print("Palindrome")
else:
    print("Not palindrome number")
 

Method- 2

def pal(name):
    pali=name[::-1]
    return pali 

name=input()
if pal(name)==name:
    print("palindrome")
else:
    print("not palindrome")
    
19 ) Print Fibonacci Series Up to N Terms
📌 Problem: Write a program to print the Fibonacci series up to N terms.

🔹 Input:
5
🔹 Output:
0 1 1 2 3

def fibonacci(n):
    if n<=1:
        return n 
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input())
if n<=1:
    print("Please enter positive integer")
else:
    for i in range(n):
        print(fibonacci(i),end=" ")


20) Count the Number of Vowels in a String
📌 Problem: Write a program to count the number of vowels in a given string.

🔹 Input:
hello world
🔹 Output:
3

def vowels(text):
    vowels ="AEIOUaeiou"
    count=0 
    for i in text:
        if i in vowels:
            count+=1 
    return count 
text=input()
print(vowels(text)) 



21) Find the Maximum Element in a List
📌 Problem: Write a program to find the maximum number in a list.

🔹 Input:
[3, 7, 2, 9, 5]
🔹 Output:
9

SOURCE CODE:

num=list(map(int,input().split(" ")))
print(max(num))

Method-2 

def find_maximum(numbers):
    if not numbers:
        return None 
    maximum=numbers[0]
    for number in numbers:
        if number>maximum:
            maximum=number
    return maximum

numbers=list(map(int,input().split(" ")))
print("Maximum number is :",find_maximum(numbers))


22) Reverse a String using a Function
📌 Problem: Write a function to reverse a string.
🔹 Input:
hello
🔹 Output:
olleh

Method-1 
def reverse_string(name):
    return name[::-1]

name=input()
print(reverse_string(name))

Method-2 
name=input()
rev=name[::-1]
print(rev) 

23) Find the Sum of Elements in a List
📌 Problem: Write a program to calculate the sum of all elements in a list.

🔹 Input:
[4, 2, 6, 8]
🔹 Output:
20


SOURCE CODE:
list_of_sum=list(map(int,input().split(" ")))
sum1=0
for i in list_of_sum:
    sum1=sum1+i 
print(sum1) 


24) Check if a Number is a Perfect Square
📌 Problem: Write a program to check if a number is a perfect square.

🔹 Input:
16
🔹 Output:
Perfect Square
🔹 Input:
10
🔹 Output:
Not a Perfect Square


SOURCE CODE:
import math
def perfect_square(num):
    if num < 0:
        return "Not a square number"
    sq = int(math.sqrt(num)) 
    return "Perfect square number" if sq * sq == num else "Not a square number"

num = int(input())
print(perfect_square(num))



25) Find the Second Largest Element in a List
📌 Problem: Write a program to find the second largest number in a list.

🔹 Input:
[10, 5, 8, 12, 15]
🔹 Output:
12

SOURCE CODE:

def second_largest_number(numbers):
    unique_num=sorted(list(set(numbers)),reverse=True)
    if len(unique_num)<2:
        return None 
    else:
        return unique_num[1]
numbers=list(map(int,input().split(" ")))
print(second_largest_number(numbers))



PROBLEM - 26:

# Write a Python program to print the following string in a specific format (see the output). Go to the editor
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" 
# Output :
# Twinkle, twinkle, little star,
#     How I wonder what you are! 
#         Up above the world so high,
#         Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
#     How I wonder what you are
# ----------------------------------------------------
# Hints
# Using \n (newline) and \t (tab) to format the string



SOLUTION:


print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!") 




PROBLEM - 27:


# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.



SOLUTION:


name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((2014 - age)+100)
print(name + " will be 100 years old in the year " + year)



PROBLEM - 28:


# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5 
# Expected Result : 615


SOLUTION:

# Accept input from the user
n = input("Enter an integer: ")

# Compute n + nn + nnn
result = int(n) + int(n*2) + int(n*3)

# Display the result
print("Result:", result)



#PROBLEM - 29:


# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1 
# j = 0,1, n-1.
# Input
# Input number of rows: 3                                                                                       
# Input number of columns: 4  
# Output
# [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
 
row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]
for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col
print(multi_list)


       

       
#PROBLEM - 30
# Write a Python program to check a triangle is valid or not 

def triangle_check(l1,l2,l3):
    if (l1>l2+l3) or (l2>l1+l3) or (l3>l1+l2):
        print('No, the lengths wont form a triangle')
    elif (l1==l2+l3) or (l2==l1+l3) or (l3==l1+l2):
        print('yes, it can form a degenerated triangle')
    else:
        print('Yes, a triangle can be formed out of it')
length1 = int(input('enter side 1\n'))
length2 = int(input('enter side 2\n'))
length3 = int(input('enter side 3\n'))
triangle_check(length1,length2,length3)


#PROBLEM - 31
# Write a Python program to construct the following pattern, using a nested loop number.
#input  : 10

#Output :  

       
1
22
333
4444
55555
666666
7777777
88888888
999999999
10101010101010101010
999999999
88888888
7777777
666666
55555
4444
333
22
1


#SOURCE CODE:

num=int(input())
for i in range(1,num+1):
    for j in range(1,i+1):
        print(i,end="")
    print()
for i in range(num-1,0,-1):
    for j in range(1,i+1):
        print(i,end="")
    print()



#PROBLEM = 32

# Write a Python program to construct the following pattern, using a nested loop number.
# 1                                                                                                             
# 22                                                                                                            
# 333                                                                                                           
# 4444                                                                                                          
# 55555                                                                                                         
# 666666                                                                                                        
# 7777777                                                                                                       
# 88888888                                                                                                      
# 999999999  

#SOURCE CODE:

num=int(input())
for i in range(1,num+1):
    for j in range(1,i+1):
        print(i,end="")
    print()


#METHOD - 2

for i in range(10):
    print(str(i) * i)



#PROBLEM - 33

#  Write a Python program to construct the following pattern, using a nested for loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *


#source code

num=int(input())
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(num-1,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


#PROBLEM - 34

#  Write a Python program to construct the following pattern, using a nested for loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * *


#SOURCE CODE:


num=int(input())
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print() 

   

#PROBLEM - 35

# Write a Python program that accepts a string and calculate the number of digits and letters
# Sample Data : "Python 3.2"
# Expected Output :
# Letters 6 
# Digits 2

#SOURCE CODE:

name = "Python 3.2"
letters = 0
digits = 0

for i in name:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        letters += 1
    else:
        pass

print("Letters:", letters)
print("Digits:", digits)


#PROBLEM - 36

# Count the number of even and odd numbers from a series of numbers
# Input 
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
# Output
# Number of even numbers : 4                                                                                    
# Number of odd numbers : 5

#SOURCE CODE:

num =  (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd= 0
for i in num:
    if i%2==0:
        even+=1 
    else:
        odd+=1 
print("even :",even)
print("odd :",odd)



#PROBLEM - 37

# Write a Python program to get the Fibonacci series between 0 to 50 

#SOURCE CODE :

a = 0
b = 1 

while a<=50:
    print(a,end=" ")
    a,b=b,a+b

#PROBLEM - 38

#find number
#  Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700

#METHOD -1 

for i in range(1500,2700):
    if i%5 == 0 and i%7==0:
        print(i,end=",")

 #METHOD -2

 n=[]
for i in range(1500,2700):
    if i%5 == 0 and i%7==0:
        n.append(str(i))
        print(i,end=",")




#PROBLEM - 39 

# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 


import random
number = random.randint(1,9)
guess=0
count=0

while guess != number and guess != 'exit':
    guess = input("what's your guess: ")
    
    if guess == 'exit':
        break
    guess = int(guess)
    count +=1 
    
    if guess<number:
        print("To Low!")
    elif guess>number:
        print("To High")
    else:
        print("you got it!")
        print("And it only took you",count,"tries!")



#PROBLEM - 40

# Write a Python program to check the validity of a password (input from users).
# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
# Input
# W3r@100a
# Output
# Valid password


import re 

password = input("Enter the password : ")

if(6<=len(password) <= 16 and
    re.search(r"[a-z]",password) and
    re.search(r"[A-Z]",password) and
    re.search(r"[0-9]",password) and
        re.search(r"[$#@]",password)):
            
            print("Valid password")
else:
    print("Invalid password")



#PROBLEM - 41

# Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.

x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
    print("Equalitrial Triangle")
elif x != y != z:
    print("Scalene Triangle")
else:
    print("isosceles triangle")



 #PROBLEM - 42 :

 # Write a Python program to check whether an alphabet is a vowel or consonant

 #METHOD - 1

string = input("Enter a string: ")
vowels_list = "AEIOUaeiou"
vowels = 0
consonants = 0

for i in string:
    if i.isalpha():
        if i in vowels_list:
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)



#METHOD - 2

 # Write a Python program to check whether an alphabet is a vowel or consonant
l = input("Input a letter of the alphabet: ")
if l in ('a', 'e', 'i', 'o', 'u'):
    print("%s is a vowel." % l)
elif l == 'y':
    print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
    print("%s is a consonant." % l) 



#PROBLEM - 43

 # Convert a list of characters into a string
# Input ['a', 'b', 'c', 'd']
# Output abcd

l=['a','b','c','d']
for i in l:
    print(i,end="")

 # Convert a list of characters into a string
# Input ['a', 'b', 'c', 'd']
# Output abcd
s = ['a', 'b', 'c', 'd']
str1 = ''.join(s)
print(str1)


#PROBLEM - 44

 
 # Write a Python program to check whether a list contains a sublist.
# Input
# a = [2,4,3,5,7]
# b = [4,3]
# c = [3,7]
# print(is_Sublist(a, b))
# print(is_Sublist(a, c))
# Output
# True
# False
 
def is_Sublist(main_list,sub_list):
    n=len(sub_list)
    for i in range(len(main_list)-n+1):
        if main_list[i:i+n] == sub_list:
            return True
    return False
    
    
a = [2,4,3,5,7]
b = [4,3]
c = [3,7]
print(is_Sublist(a, b))
print(is_Sublist(a, c))


#PROBLEM - 45

 # Write a Python program to find common items from two lists.
# input
# color1 = "Red", "Green", "Orange", "White"
# color2 = "Black", "Green", "White", "Pink"
# output
# {'Green', 'White'}


# Input lists
color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]

# Find common items using set intersection
common_colors = set(color2) & set(color1)

# Output
print(common_colors)


#PROBLEM - 46

# Write a Python program to get the difference between the two lists
# Input 
# list1 = [1, 2, 3, 4]
# list2 = [1, 2]
# Output
# [3,4]


list1 = [1, 2, 3, 4]
list2 = [1, 2]
print(set(list1) - set(list2))


#PROBLEM - 47

# Write a Python program to get the smallest number from a list.
# max_num_in_list([1, 2, -8, 0])
# return 2

def max_num_in_list(list):
    max = list[0]
    for i in list:
        if i>max:
            max=i
    return max
print(max_num_in_list([1, 2, -8, 0]))



#PROBLEM - 48 

# Write a Python program to get the frequency of the elements in a list.
# input
# my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# outout
# {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}
import collections
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
print("Orginal List:",my_list)
result=collections.Counter(my_list)
print("frequency of the elements in a list: ",result)
      
#PROBLEM - 49

#  Write a Python program to generate all permutations of a list in Python
# Input [1,2,3]
# Output [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
import itertools
print(list(itertools.permutations([1,2,3])))


#PROBLEM - 50 

# Write a Python program to remove duplicates from a list.
# Input a = [10,20,30,20,10,50,60,40,80,50,40]
# Output {40, 10, 80, 50, 20, 60, 30} 

a = [10,20,30,20,10,50,60,40,80,50,40]
dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)
print(uniq_items)




















