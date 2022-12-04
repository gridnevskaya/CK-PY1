# TODO реализовать функцию удаления элемента из списка по индексу
def delete(list_, index=None):
    if (index is None) or (index == -1):
        new_list_ = list_[:-1]
    else:
        new_list_ = list_[:index] + list_[index + 1:]
    return new_list_

print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
# Пустая строка