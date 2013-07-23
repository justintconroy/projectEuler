
# Calculate the sum of all multiples of 3 or 5 below the given max and
# print it to the attached terminal.

max = 1000

sum = 0

for n in range(max):
    if (n % 3 == 0) or (n % 5 == 0):
#        print n
        sum += n

print 'Total: ' + str(sum)
