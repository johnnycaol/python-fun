# Math

# Find all the prime numbers smaller than max
def findPrime(max):
    prime = []
    i = 2
    while(i < max):
        j = 2
        while(j <= (i/j)):
            if not(i%j): break
            j = j + 1
        if (j > i/j):
            prime.append(i)
        i = i + 1
    return prime

print(findPrime(100))