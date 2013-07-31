
# I will use a special pattern for generating the products of three digit
# numbers from largest to smallest. For each one generated, I will check
# if it is palindromic. If it is, that is the answer.

def IsPalindrome(number):
    textNumber = str(number)
    start = 0
    end = len(textNumber) - 1

    while (start <= end):
        if textNumber[start] != textNumber[end]:
            return False
        else:
            start = start + 1
            end = end - 1
    return True


def LargestPalindrome(seed):

    # Set the initial values to test with the seed.
    middleValue1 = seed
    middleValue2 = middleValue1


    while middleValue2 > 0:

        # start by multiplying each middle value together, then go down the
        # list by increasing the first middle value and decreasing the
        # second until the first reaches the seed value. This will ensure
        # that the function will iterate through the results in order from
        # largest to smallest.
        factor1 = middleValue1
        factor2 = middleValue2
        while factor1 <= seed and factor2 >= 1:
            result = factor1 * factor2

            if IsPalindrome(result):
                return (result, factor1, factor2)
            else:
                factor1 = factor1 + 1
                factor2 = factor2 - 1

        # On every other iteration, the middle values will start out the
        # same or be off by one.
        if middleValue1 == middleValue2:
            middleValue2 = middleValue2 - 1
        else:
            middleValue1 = middleValue1 - 1



number = 999
print number
print LargestPalindrome(number)

