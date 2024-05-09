def xor(text, number):
    # bin_number = bin(number)[2:]
    ascii_arr = []
    final_arr = []

    print(final_arr)
    for word in text:
        for char in word:
            ascii_arr.append(ord(char))

    for i in range(max(len(ascii_arr), len(number))):
        final_arr.append(ascii_arr[i % len(ascii_arr)] ^ number[i % len(number)])

    for item in final_arr:
        print(chr(item))

    return 2


xor(["label"], [13])
