# 11 ≡ x mod 6
# 8146798528947 ≡ y mod 17


def calculate_b(a, m):
    # given a and m, calculate b (a = b mod m)
    return a % m


print(calculate_b(11, 6))
print(calculate_b(8146798528947, 17))
