from Crypto.Util.number import *

message = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
dec = bytes.fromhex(message)
flag_format = b"crypto{"
repeated_flag_format = ""
final_arr = []

# print(type(byte_flag_format), repeated_flag_format)

part_key = bytes_to_long(flag_format)
byte_message = bytes_to_long(dec[:7])

print(long_to_bytes(part_key ^ byte_message))

key = b"myXORkey"
decrypted_message = bytearray()

for i in range(len(dec)):
    decrypted_message.append(dec[i] ^ key[i % len(key)])


print(decrypted_message)


# key = a
# flag = b
# message = c

# a ^ b = c
# a = b ^ c
# b = a ^ c


# key ^ flag = message
# key = message ^ flag
# flag = message ^ key
