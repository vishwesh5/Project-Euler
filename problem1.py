# Specify upper limit
UPPER = 1000
# Multiples of 3 below 1000
multiplesOf3 = [i for i in range(0,UPPER,3)]
# Multiples of 5 below 1000
multiplesOf5 = [i for i in range(0,UPPER,5)]
# Multiples of 15 below 1000
multiplesOf15 = [i for i in range(0,UPPER,15)]
# Sum of multiples of 3 or 5 below 1000
answer = sum(multiplesOf3) + sum(multiplesOf5) - sum(multiplesOf15)
print(answer)
