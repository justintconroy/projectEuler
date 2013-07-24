
# Add all of the even fibonacci numbers less than the max value.

max = 4000000

sum = 0

n1 = 0
n2 = 1
n3 = 1

while n3 < max:
    # Add the n3 value right after checking the loop condition to ensure
    # that a value greater than the max won't be added to it.
    if n3 % 2 == 0:
        #print n3
        sum += n3

    # Generate the next value in the sequence.
    n3 = n1 + n2

    # Update the sum values for the next iteration.
    n1 = n2
    n2 = n3

print 'Total: ' + str(sum)
