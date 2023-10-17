# Дан массив, состоящий из последовательности букв и чисел.
# Функция должна трансформировать исходную строку в новую,
# состоящую из букв исходной продублированных соответственно числу.
# "a1b3" -> "abbb"
# "s4k2" -> "sssskk"

def transform(text):
    output = ""
    size = len(text)
    for s in range(0, size, 2):
        output += text[s] * int(text[s + 1])
    return output


#print(transform("g3i2n6"))
