#FibonacciSeries
print('Fibonacci: How many terms would you like to have?')
numberOfTerms = int(input())

firstTerm = 0
secondTerm = 1
print(firstTerm)
for i in range (numberOfTerms - 1):
    nextTerm = firstTerm + secondTerm
    print(nextTerm)
    firstTerm = secondTerm
    secondTerm = nextTerm
    if i == numberOfTerms:
        break
