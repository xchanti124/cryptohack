from Crypto.Util.number import *

# a = key 1
# b = key 2
# c = key 3

# a^b=c
# a=b^c
# b=a^c

# a =
# b ^ a = c
# b = a ^ c

# KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e

# KEY2 = KEY1 ^ 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e

# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1

# KEY3 = KEY2 ^ c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1

# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
# FLAG = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf ^ KEY1 ^ KEY3 ^ KEY2

a = bytes_to_long(bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"))
b = a ^ bytes_to_long(
    bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
)
c = b ^ bytes_to_long(
    bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
)
flag = (
    a
    ^ b
    ^ c
    ^ bytes_to_long(
        bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
    )
)

print(long_to_bytes(flag))
