from random import sample
from string import ascii_uppercase, ascii_lowercase, digits

def get_random_password(length_password=8) -> str:
    # TODO написать функцию генерации случайных паролей
    return "".join(sample(ascii_uppercase + ascii_lowercase + digits, length_password))

print(get_random_password())
# Пустая строка