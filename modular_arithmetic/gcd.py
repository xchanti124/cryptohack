# prime -> gcd(a, b) = 1
# coprime -> if a is prime, b < a, then a and b are coprime
#         -> numbers that have only one common factor (1)
#         -> if a is prime, b > a, then it could be not coprime, example: a = 3, b = 9


def gcd(a, b):
    if a > b:
        remainder = a - b
        if remainder == 0:
            return a
        return gcd(remainder, b)
    else:
        remainder = b - a
        if remainder == 0:
            return b
        return gcd(a, remainder)


print(gcd(66528, 52920))
