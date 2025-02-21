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











 

























