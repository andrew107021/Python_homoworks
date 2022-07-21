# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def rle_mtd(string: str) -> str:
    """
    Basic logic for encoding
    :param string: str
    :return: string_out: str
    """
    string_out = ''
    count = 1
    while string:
        if len(string) > 1:
            if string[0] == string[1]:
                count += 1
                string = string[1:]
            else:
                string_out += str(count) + string[0]
                string = string[1:]
                count = 1
        else:
            string_out += str(count) + string[0]
            string = ''

    return string_out


def rle_bck(string: str) -> str:
    """
    Basic logic for decoding
    :param string: str
    :return: string_out: str
    """
    string_out = ''
    count = ''
    while string:
        if len(string):
            if string[0].isdigit():
                count += string[0]
                string = string[1:]
            else:
                count = int(count)
                string_out += string[0]*int(count)
                string = string[1:]
                count = ''
        else:
            break
    return string_out


print(rle_mtd('ABCABCABCDDDFFFFFF'))    # from wikipedia 1A1B1C1A1B1C1A1B1C3D6F
print(rle_mtd('WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'))   # 9W3B24W1B14W
print(rle_bck(rle_mtd('WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')))
print(rle_bck(rle_mtd('ABCABCABCDDDFFFFFF')))
