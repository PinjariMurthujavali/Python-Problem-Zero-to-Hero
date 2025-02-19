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







 

























