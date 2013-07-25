
def factorize(number):
    """ Decompose a number into its prime factors.

    Returns the list of prime factors for the given number.

    """

    primes = []

    # Shortcut to check for even numbers. This way the loop only needs to
    # loop through odd numbers, so it can be twice as fast.
    if number == 2:
        primes.append(number)
        return primes

    if number % 2 == 0:
        primes.append(2)
        primes.extend(factorize(number / 2))
        return primes

    divisor = 3

    while ((divisor*divisor < number)
            and (number % divisor != 0)):
        divisor = divisor + 2

    # If the divisor is greater than the square root of the number after
    # going through the previous loop, it means that no factors were found
    # and, therefore, that the number itself is prime. This will terminate
    # the recursion.
    if divisor * divisor > number:
        primes.append(number)
        return primes
    else:
        # The divisor itself may not actually be prime. Factorize it.
        primes.extend(factorize(divisor))

        # Factorize the result of the division and add all of those
        # factors to the list.
        primes.extend(factorize(number / divisor))

    return primes

factors = factorize(600851475143)

print factors
print max(factors)

