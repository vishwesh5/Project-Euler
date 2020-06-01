def isPrime(n):
    if n%2 == 0:
        if n == 2:
            return True
        else:
            return False
    i = 3
    while i*i <= n:
        if n%i == 0:
            return False
        i+=2
    return True

primes = [2,3,5,7,11,13,17,19]

num = 21
while num < 2e6:
    if isPrime(num):
        primes.append(num)
    num += 2

print(sum(primes))
