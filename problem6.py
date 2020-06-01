# Sum of squares
def sumOfSquares(upper):
    return sum([i**2 for i in range(1,upper+1)])

# Square of sum
def squareOfSum(upper):
    return (upper*(upper+1)//2)**2


upper = 100
difference = abs(sumOfSquares(upper) - squareOfSum(upper))
print(difference)
