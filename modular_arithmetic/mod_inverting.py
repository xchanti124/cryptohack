# 3 * d ≡ 1 mod 13
# 3 ^ 12 = 1 mod 13
# (3 ^ 12) / 3 = 1/3 mod 13
# (3 ^ 12) / 3 % 13


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


def modular_inverse(a, m):
    bezout_coefficients = extended_gcd(a, m, 0, 0, 1, 0, 1, 0, 1, 0)
    return bezout_coefficients[0] % m


print(modular_inverse(3, 13))
