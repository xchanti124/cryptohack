def single_byte_xor(text: bytes, key: int) -> bytes:
    """Given a plain text `text` as bytes and an encryption key `key` as a byte
    in range [0, 256) the function encrypts the text by performing
    XOR of all the bytes and the `key` and returns the resultant.
    """
    return bytes([b ^ key for b in text])


def decryption(keys):
    message = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
    decoded_message = bytes.fromhex(message)
    return single_byte_xor(decoded_message, keys)


for i in range(0, 256):
    if b"crypto{" in decryption(i):
        print(decryption(i))
