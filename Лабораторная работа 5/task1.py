# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

list_dict = [
    {
        "bin": bin(number),
        "dec": number,
        "hex": hex(number),
        "oct": oct(number)
    }
    for number in range(16)
]

pprint(list_dict)
# Пустая строка