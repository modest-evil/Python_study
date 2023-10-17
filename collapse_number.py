# Дано число. Функция должна вернуть сумму всех разрядов до тех пор, пока число не станет одноразрядным.
# 723 -> 7+2+3 = 12 -> 1+2 = 3


def collapse(number):
    text = str(number)
    count = len(text)
    print(number, "has ", count, " digits")

    res = 0
    i = 1
    for letter in text:
        res += int(letter)
        t = str(i) + ") digit is "
        print(t, letter)
        print("res is ", res)
        i += 1

    if len(str(res)) == 1:
        print(res)
        return res
    else:
        collapse(res)


collapse(51278)
