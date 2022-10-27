# Задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

try:
    def encode(s):
        encoding = ''
        i = 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
                i += 1
            encoding += str(count) + s[i]
            i += 1
        return encoding

    def decode(s):
        number = ''
        decoding = ''
        for i in range(len(s)):
            if not s[i].isalpha():
                number += s[i]
            else:
                decoding = decoding + s[i] * int(number)
                number = ''
        return decoding

    def write_result():
        with open('Ds002/text_encode_RLE.txt', 'w') as data:
            data.write(input('Напишите текст необходимый для сжатия: '))

        with open('Ds002/text_encode_RLE.txt', 'r') as file:
            decoding = file.read()

        with open('Ds002/text_decode_RLE.txt', 'w') as file:
            encoding = encode(decoding)
            file.write(encoding)

    write_result()
except:
    print('!! Введите корректный текст !!')