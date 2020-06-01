# Python program to find LCM of two numbers 
  
# Recursive function to return gcd of a and b 
def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
  
# Function to return LCM of two numbers 
def lcm(a,b): 
    return (a*b) // gcd(a,b)

answer = 1
upper = 20
for i in range(1,upper+1):
    answer = lcm(answer,i)

print(answer)
