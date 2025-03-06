# 1. If else and if else ladder: Easy Questions
# Number is positive, Negative or Zero
num = 58
if num>0:
    print("positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Even or Odd
num = 58
if num%2==0:
    print(num,"is an even number")
else:
    print(num,"is an odd  number")

# Using Terinary Operator
res = "Even" if num%2==0 else "Odd"
print(res)

# Eligible to vote
age = 19
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible")

# Greatest number
a = 10
b = 20
if a > b:
    print(a,"is greatest")
else:
    print(b,"is a greatest")

# If score is greater than 40, then print pass otherwise print fail
score = 60
if score > 40:
    print("Pass")
else:
    print("Fail")
# Using Terinary Operator
res="Pass" if score > 40 else "Fail"
print(res)

# If we give input as 1 then output is Monday etc...
day = 3
if day == 1:
    print("Monday")
elif day == 2:
    print("Tueday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day ==7:
    print("Sunday")
else:
    print("Invalid")

# Implement a simple calculator to perform different operations
a=8
b=5
print(a+b)
print(a-b)
print(a*b)
print(a&b)
print(a%b)
# or
operation = input("Enter operator to perform").lower()
a=8
b=5
if operation == "add": #if input is Add ADD AdD aDd so thats why .lower() is used in input to convert all characters into lower case
    print(a+b)
elif operation == "sub":
    print(a-b)
elif operation == "mul":
    print(a*b)
elif operation == "div":
    if b == 0:
        print("Divisible not possible")
    else:
        print(a/b)
else:
    print("Invalid")


# If we give input as 1 then output is January etc...
month=9
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Invalid month")

# if-else: Medium Questions:

# To classify a character entered by the user as a vowel, consonants or special characters
char=input("Enter a character").lower()
if len(char) != 0:
    print("Invalid")
if char in ['a','e','i','o','u']:
    print("Vowel")
# elif isalpha():
#     print("Consonant")
else:
    print("Special Characters")


# 2. Loops: Easy Questions:

# Print all numbers from 1 to 100 using a for loop.
for i in range(1,101):
    print(i)

# Write a program to print the sum of the first n natural numbers. (n*n+1/ 2)
n = 10
sum=0
for i in range(1,n+1):
    print(i)
    sum=sum+1
print(sum)
# or
n = 15
print(n*(n+1)/2)

# Print all even numbers between 1 and 50 using a while loop.
num = 1
while num <= 50:
    if num % 2 == 0:
        print(num,"Even")
    num += 1


for i in range(1,51):
    if i % 2 == 0:
        print(i,"Even")

# Write a program to display the multiplication table of a given number. First 20
table = 5
for i in range(1,21):
    print(table*i)


# Reverse a number using a while loop. 1. Also can we get the sum of all the digits.
num = 1234
rev = 0
sum = 0
while num != 0:
    rem = num % 10
    rev = (rev*10) + rem
    sum += rem
    num //= 10
print(rev)
print(sum)


# Write a program to count the number of digits in a given number using a while loop.
num = 123456
count=0
while num != 0:
    num //= 10
    count += 1
print(count)

# Write a program that keeps asking the user to enter numbers until they enter a negative number. Use a while loop.
while True:
    num = int(input("Enter a number"))
    if num < 0:
        print("Negative Number")
        break

# Implement a basic login system where the user has three attempts to enter the correct password using a loop.

db_username = 'Pooji'
db_password = '1234'
total_chances = 3
while total_chances > 0:
    input_username = input("Enter a username")
    input_password = input("Enter a password")
    if input_username == db_username and input_password == db_password:
        print("Login successful")
        break
        # total_chances = 0
    else:
        total_chances -= 1
        print("Invalid creds")
        print("You still have", total_chances, "chances")

# Check if a given number is a prime number using a for loop.
# approach-1
num = int(input())
if num in [0,1] or num < 0:
    print("Neither prime nor composite")
else:
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        print("Prime")
    else:
        print("Not prime")

# approach-2
num1 = int(input())
if num1 in [0,1] or num1 < 0:
    print("Neither prime nor composite")
else:
    res = True
    for i in range(2,num1):
        if num1 % i == 0:
            res = False
            print("Not a prime")
            break
    if res:
        print("prime")

# approach-3
num1 = int(input())
if num1 in [0,1] or num1 < 0:
    print("Neither prime nor composite")
else:
    res = True
    for i in range(2,(num1 // 2)+1): #--> If we take one number eg: 16-->takes 15--> half of this number is 7 +1 =8-->there is no factors between 8 and 15
        if num1 % i == 0:
            res = False
            print("Not a prime")
            break
    if res:
        print("prime")

# approach-4
num1 = int(input())
if num1 in [0,1] or num1 < 0:
    print("Neither prime nor composite")
else:
    res = True
    for i in range(2,int(num1 ** 0.5) + 1):
            res = False
            print("Not a prime")
            break
    if res:
        print("prime")

# Print the first 10 terms of the Fibonacci series using a for loop.

n1 = 0
n2 = 1
print(n1)
print(n2)
for i in range(0,13):
    temp = n1+n2
    print(temp)
    n1 = n2
    n2 = temp

    # or  

num = 5
n1 = 0
n2 = 1
print(n1)
print(n2)
for i in range(2,num):
    n3 = n1+n2
    n1 = n2
    n2 = n3
    print(n3)
    
      # or

def check_prime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
if check_prime(8):
    print("prime")
else:
    print("not prime")


# Sum of non-primes in given number
num1 = int(input())
temp = num1
sum = 0
while temp > 0:
    digit = temp % 10
    if(check_prime(digit)):
        sum += digit
    temp //= 10
print(sum)


# Armstrong number
num = 153
temp = num
sum = 0
while temp > 0:
    digit = num % 10
    sum += digit ** 3 # sum += digit ** len(str(num))--> if number is user input.
    temp //= 10
if(sum == num):
    print(num,"is a armstrong number")
else:
    print(num,"is not a armstrong number")


# Nearest prime
# 8 - 7
# 12 - 11,13
# 24 - 23

num1 = int(input("Enter a number"))
temp = num1
right_side_prime = -1
while True:
    temp += 1
    if(check_prime(temp)) == True:
        right_side_prime = temp
        break
print(right_side_prime)

temp2 = num1
left_side_prime = -1
while True:
    temp2 -= 1
    if temp2 < 2:
        break
    if(check_prime(temp2)) == True:
        left_side_prime = temp2
        break
print(left_side_prime)
left_dis = num1 - left_side_prime
right_dis = right_side_prime - num1
if left_side_prime == -1:
    print(right_side_prime)
elif left_dis < right_dis:
    print(left_side_prime)
elif right_dis < left_dis:
    print(right_side_prime)
else:
    print(left_side_prime, right_side_prime)


# Sum of odd digits in given number
num = 123456
temp = num
odd_sum = 0
while temp > 0:
    digit = temp % 10
    if digit % 2 != 0:
        odd_sum += digit
    temp //= 10
print(odd_sum)


# Print armstrong number in given range
min_num = int(input("Enter min value"))
max_num = int(input("Enter max value"))
for num in range(min_num, max_num + 1):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** len(str(num))
        temp //= 10
    if(sum == num):
        print(num,"is a armstrong number")


# Assignments
# sum of odd digits in given number
# Print armstrong number in given range
