# Perfect Number--> sum of all divisors equal to given number
num = 6
sum = 0
for i in range(1,num):
    if num % i == 0:
        sum = sum + i
if sum == num :
    print(num,"is a Perfect number")
else:
    print(num,"is not a Perfect number")


# Sum of non-prime digits
start, end = 1,3
sum_non_primes = 0
for num in range(start, end + 1):
    if num < 2:
        sum_non_primes += num
    else:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors += [i]
        if len(factors) > 2:
            sum_non_primes += num
print(sum_non_primes)


# Sum of odd digits
num = 135768
oddSum = 0
for i in str(num):
    if int(i) % 2 != 0:
        oddSum = oddSum + int(i)
print(oddSum)

# LCM and GCD
a, b = 12, 18
gcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i
lcm = (a * b) // gcd
print("LCM is", lcm)
print("GCD is", gcd)

