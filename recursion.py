"""Recursion Assignment 13"""


# Returns the nth Fibonacci number
def fibonacci(n):
    """
    Returns the nth Fibonacci number using recursion.
    Assumes the Base cases are: F(0) = 0, F(1) = 1
    """
    if n < 0:
        raise ValueError("Your input must be a positive integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def gcd(a,b):
    """
    Applying Euclid's Algorithm to solve for gcd. a and b must be integers.
    """
    if b == 0:
        return a
    return gcd(b, a % b)


def compareTo(s1, s2):
    """
    This will recursively compare two strings.
    Marks to hit:
    • -1 if s1 < s2
    •  0 if s1 == s2
    •  1 if s1 > s2
    """
    if len(s1) == 0 and len(s2) == 0:
        return 0
    if len(s1) == 0:
        return -1
    if len(s2) == 0:
        return 1
    if s1[0] < s2[0]:
        return -1
    if s1[0] > s2[0]:
        return 1
    return compareTo(s1[1:], s2[1:])

#  This section runs sample tests when executed from the command line.
if __name__ == "__main__":
    print("Fibonacci example:", fibonacci(5))
    print("GCD example:", gcd(48, 18))
    print("String comparison example:", compareTo("apple", "apricot"))
