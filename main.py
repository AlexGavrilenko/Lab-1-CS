import math
import os

def find_unique_sorted(s):
    s = set(s)
    return ''.join(sorted(s))

def quantity(entropy, textlength):
   return (entropy * textlength) / 8

def encode_to_base64(bytes):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    output = ""
    b = 0  # змінна для збереження 6-бітних блоків даних

    for i in range(0, len(bytes), 3):
        # Помножте на 252, а потім зсуньте на 2 біти, щоб отримати перший 6-бітний байт
        b = (bytes[i] & 0xfc) >> 2
        output += alphabet[b]  # закодуйте перший 6-бітний байт і додайте його до рядка виведення

        # Зсуньте останні два біти першого байту на початок 6-бітного блоку
        b = (bytes[i] & 0x03) << 4

        if i + 1 < len(bytes):
            # Візьміть останні чотири біти другого байту, зсуньте їх на 4 біти і додайте до поточного 6-бітного блоку
            b |= (bytes[i + 1] & 0xf0) >> 4
            output += alphabet[b]  # закодуйте блок і додайте його до рядка виведення

            # Зсуньте останні чотири біти другого байту на початок наступного 6-бітного блоку
            b = (bytes[i + 1] & 0x0f) << 2

            if i + 2 < len(bytes):
                # Візьміть останні два біти третього байту, зсуньте їх на 6 бітів і додайте до поточного 6-бітного блоку
                b |= (bytes[i + 2] & 0xc0) >> 6
                output += alphabet[b]  # закодуйте блок і додайте його до рядка виведення

                # Візьміть останні 6 бітів третього байту і додайте їх до наступного 6-бітного блоку
                b = bytes[i + 2] & 0x3f
                output += alphabet[b]
            else:
                # Якщо в кінці залишилося тільки 2 байти, а не 3
                output += alphabet[b]
                output += "="
        else:
            # Якщо в кінці залишився тільки 1 байт, а не 3
            output += alphabet[b]
            output += "=="
    return output

file_path = input("Назва файлу: ") + ".txt"
file_size = os.path.getsize(file_path)



if(input("Введіть режим роботи: ") == "1"):

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    print(text)

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
else:

    with open(file_path, 'rb') as file:
        text = file.read()
    print(encode_to_base64(text))

    with open(file_path.split(".")[0] + "base64." + file_path.split(".")[1], 'w', encoding='utf-8') as file:
        file.write(encode_to_base64(text))