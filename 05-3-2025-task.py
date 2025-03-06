# Sum of odd digits in given number
num = int(input("Enter a number"))
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


# smallest prime digit in a given number eg:4567 o/p:5 if no primes print there are no primes
num = int(input("Enter a number: "))
smallest_prime_digit = 10
while num > 0:
    digit = num % 10
    if digit in (2, 3, 5, 7) and digit < smallest_prime_digit:
        smallest_prime_digit = digit
    num //= 10
if smallest_prime_digit == 10:
    print("No prime digits found.")
else:
    print("The smallest prime digit is:", smallest_prime_digit)
