import math

max = 600851475143
#max = 34

# Using the Sieve of Eratosthenes to find all of the primes less than or
# equal to max number. Algorithm taken from Wikipedia.

# 1. Create a list of consecutive integers from 2 to max (including max).
#numbers = range(2,int(math.sqrt(max))+1)
#numbers.append(max)
numbers = range(2,max+1)

# 2. Initially, let p equal 2, the first prime number.
p = 2
index = 0

while index < len(numbers):
    # 3. Remove all numbers from the list that are multiples of p.
    index = numbers.index(p)
    for i in numbers[index + 1:]:
        if i % p == 0:
            numbers.remove(i)

    # 3.5 Additionally check if p is a factor of max and remove it if
    #     it isn't. If it gets removed, use the same index to get the
    #     next p value, otherwise increment the index.
    if max % p != 0:
        numbers.remove(p)
        if index < len(numbers):
            p = numbers[index]
    else:
        # 4. Find the first number greater than p in the list that is
        #    not deleted. Iterate until there are no more such numbers.
        if index + 1 < len(numbers):
            p = numbers[index + 1]
        else:
            break


print max
print numbers
print numbers[len(numbers) - 1]
