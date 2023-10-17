# Дано три числа. Функция должна вернуть сумму квадратов больших из них.

def square_sum(a, b, c):
    temp = [a, b, c]
    print(temp)
    temp.sort()
    print(temp)
    temp.remove(temp[0])
    print(temp)

    res = temp[0] ** 2 + temp[1] ** 2
    #  print(res)

    return res


#print(square_sum(4, 7, 1))
