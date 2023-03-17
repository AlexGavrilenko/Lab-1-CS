import math
import os
import bz2

def find_unique_sorted(s):
    s = set(s)
    return ''.join(sorted(s))

def quantity(entropy, textlength):
   return (entropy * textlength) / 8


def output_info(quantity_information, path):
    print(f"File: {path}")
    print(f"Size: {os.path.getsize(path)} bytes")
    print(f"Quantity of information: {quantity_information:.2f} bytes")

def encode_to_base64(bytes):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    output = ""
    b = 0

    for i in range(0, len(bytes), 3):

        b = (bytes[i] & 0xfc) >> 2
        output += alphabet[b]


        b = (bytes[i] & 0x03) << 4

        if i + 1 < len(bytes):

            b |= (bytes[i + 1] & 0xf0) >> 4
            output += alphabet[b]


            b = (bytes[i + 1] & 0x0f) << 2

            if i + 2 < len(bytes):

                b |= (bytes[i + 2] & 0xc0) >> 6
                output += alphabet[b]


                b = bytes[i + 2] & 0x3f
                output += alphabet[b]
            else:

                output += alphabet[b]
                output += "="
        else:

            output += alphabet[b]
            output += "=="
    return output

file_path = input("Назва файлу: ")
file_size = os.path.getsize(file_path)
a = input("Введіть режим роботи ")
if(a == "1"):

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    H = 0
    for symbol in find_unique_sorted(text):
        p = text.count(symbol) / len(text)
        H += p * math.log2(p)

    H *= -1

    print(text.count(input("Введіть символ: "))/len(text))
    print(len(text))
    print(H)
    print(quantity(H, len(text)))
    print("Розмір файлу:", file_size, "байт")
    print("Розмір файлу:", file_size * 8, "біт")
elif(a == "2"):

    with open(file_path, 'rb') as file:
        text = file.read()
    print(encode_to_base64(text))

    with open(file_path.split(".")[0] + "base64." + file_path.split(".")[1], 'w', encoding='utf-8') as file:
        file.write(encode_to_base64(text))
