# a**2 + b**2 = c**2
# (a+b+c)**2 = 1e6
# a**2 + b**2 + c**2 + 2ab + 2bc + 2ac = 1e6
# 2*c**2 + 2*(ab+bc+ac) = 1e6
# c**2 + ab + bc + ac = 5e5
# c(c+b) + a(b+c) = 5e5
# (a+c)(b+c) = 5e5
# (1000-b)(1000-a) = 5_00_000

def specialPythogoreanTriplet():
    for a in range(1,1000):
        for b in range(a+1,1000):
            if (1000-b)*(1000-a) == 5e5:
                print(a,b,1000-a-b)
                print(a*b*(1000-a-b))
                print(a**2+b**2)
                print((1000-a-b)**2)
                return 0
    return 1

specialPythogoreanTriplet()
