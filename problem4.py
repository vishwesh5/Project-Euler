# Largest palindrome product
def checkPalindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    return False

maxPalindrome = 0
for x in range(999,99,-1):
    for y in range(999,99,-1):
        if checkPalindrome(x*y):
            print(x,y)
            print(x*y)
            if x*y > maxPalindrome:
                maxPalindrome = x*y

print(maxPalindrome)
