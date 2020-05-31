def largestPrimeFactor(n):
    i = 2
    while i**2 <= n:
        if n%i == 0:
            n = n//i
        else:
            i += 1
    return n


print(largestPrimeFactor(600851475143))
