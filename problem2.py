def generateFibonacciSequence(maxElement = 4e6):
    a1 = 1
    a2 = 2
    elements = [a1,a2]
    evenElements = [a2]
    while 1:
        element = elements[-1]+elements[-2]
        if element > maxElement:
            break
        elements.append(element)
        if element % 2 == 0:
            evenElements.append(element)
    return sum(evenElements)

print(generateFibonacciSequence())
