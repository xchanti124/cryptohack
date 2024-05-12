# a * u + b * v = gcd(a,b)
# Using the two primes p = 26513, q = 32321, find the integers u,v such that
# p * u + q * v = gcd(p,q)


def gcd_using_mod(p, q):

    while q:
        p, q = q, (p % q)
        # print(p, q)
    return p


def extended_gcd(a, b, q, r, s1, s2, s3, t1, t2, t3):
    q, r = divmod(a, b)
    s3 = s1 - q * s2
    t3 = t1 - q * t2
    if r == 0:
        return (s2, t2)
    else:
        print(
            f"a = {a}, b = {b}, q = {q}, r = {r}, s1 = {s1}, s2 = {s2}, s3 = {s3}, t1 = {t1}, t2 = {t2}, t3 = {t3}"
        )
        return extended_gcd(b, r, q, r, s2, s3, (s1 - q * s2), t2, t3, (t1 - q * t2))


print(extended_gcd(26513, 32321, 0, 0, 1, 0, 1, 0, 1, 0))
