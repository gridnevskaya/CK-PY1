from random import randint

def get_unique_list_numbers(length_list=15, first_border=-10, second_border=10) -> list[int]:
    # TODO написать функцию для получения списка уникальных целых чисел
    list_ = []
    while len(list_) < length_list:  #Проверяем, имеет ли список нужную длину
        number = randint(first_border, second_border + 1)
        if number not in list_:  #Проверяем, уникально ли данное число
            list_.append(number)
    return list_

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
# Пустая строка