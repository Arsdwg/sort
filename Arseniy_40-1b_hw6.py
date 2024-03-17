from random import randint,choice
listik = [1, 2, 3, 4, 1, 6, 7, 8, 9, 10]
number = 10
# number = randint(10,15)
# for i in range(number):
#     b = randint(1,100)
#     listik.append(b)
# print(listik, '\n')


def bubble_sort(list):
    steps = 0
    for i in range(number-1):
        for j in range(number - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                steps += 1
    print(list)
    print(f'Steps {steps} done')

bubble_sort(listik)



def binary_sort(self, list):
    number = 10
    resultOK = False
    first = 0
    last = number - 1

    while first < last:
        middle = (last + first) // 2
        if self == list[middle]:
            first = middle
            last = middle
            resultOK = True
            pos = middle
        else:
            if self > listik[middle]:
                first = middle + 1
            else:
                last = middle - 1

    if resultOK == True:
        return print(f'Элемент найден, {self} на позиции {pos} (счет начинается с 0)')
    else:
        return print('Элемент не найден')

binary_sort(8, listik)














