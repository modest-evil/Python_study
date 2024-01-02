# Дан массив целых чисел и целевое число.
# Функция должна вернуть индексы чисел, сумма которых даст целевое число.

def search_pairs(income, target):
    size = len(income)

    for i in range(size - 1):
        for j in range(i + 1, size):
            #        print(Input[i],Input[j])
            if income[i] + income[j] == target:
                return [i, j]


#print(search_pairs([1, 4, 6, 3, 2], 8))
#print(search_pairs(["abc"], 8))
