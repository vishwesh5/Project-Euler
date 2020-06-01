# Find nth prime
primes = [2,3,5,7,11,13]

def isPrime(n):
    i = 3
    while i*i <= n:
        if n%i==0:
            return False
        i += 2
    return True
        
def appendPrime():
    start = 15
    while len(primes) != 10001:
        if isPrime(start):
            primes.append(start)
        start += 2

appendPrime()
print(primes[-1])
