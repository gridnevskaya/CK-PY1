import doctest


class Rhombus:
    def __init__(self, height: int, base: int):
        """
        Создание и подготовка к работе объекта "Ромб"
        :param height: Высота ромба
        :param base: Основание ромба
        Примеры:
        >>> form_rhombus = Rhombus(5, 6) # инициализация экземпляра класса
        """
        if not isinstance(height, int):
            raise TypeError("Высота ромба должена быть типа int")
        if height <= 0:
            raise ValueError("Высота ромба должна быть положительным числом и больше нуля")
        self.height = height

        if not isinstance(base, int):
            raise TypeError("Основание ромба должно быть типа int")
        if base <= 0:
            raise ValueError("Основание ромба должно быть положительным числом и больше нуля")
        self.base = base

    def area(self):
        """
        Функция поиска площади ромба.
        :return: Площадь ромба
        >>> form_rhombus = Rhombus(5, 6)
        >>> form_rhombus.area()
        30
        """
        return self.height * self.base

    def perimetr(self):
        """
        Функция поиска периметра ромба.
        :return: Периметр ромба
        >>> form_rhombus = Rhombus(5, 6)
        >>> form_rhombus.perimetr()
        24
        """
        return 4 * self.base


class Fridge:
    def __init__(self, count_shelves: int, occupied_shelves: int):
        """
        Создание и подготовка к работе объекта "Холодильник"
        :param count_shelves: Количество полок
        :param occupied_shelves: Количество занятых полок
        Примеры:
        >>> fridge = Fridge(10, 0) # инициализация экземпляра класса
        """
        if not isinstance(count_shelves, int):
            raise TypeError("Количество полок должно быть типа int")
        if count_shelves <= 0:
            raise ValueError("Количество полок должно быть положительным числом и больше нуля")
        self.count_shelves = count_shelves

        if not isinstance(occupied_shelves, int):
            raise TypeError("Количество занятых полок должны быть типа int")
        if occupied_shelves < 0:
            raise ValueError("Количество занятых полок не может быть отрицательным числом")
        if occupied_shelves > count_shelves:
            raise ValueError("Количество занятых полок не должно быть больше общего количества полок")
        self.occupied_shelves = occupied_shelves

    def is_empty_fridge_shelves(self):
        """
        Функция вычесления свободных полок.
        :return: Количество свободных полок
        >>> fridge = Fridge(10,6)
        >>> fridge.is_empty_fridge_shelves()
        4
        """
        return self.count_shelves - self.occupied_shelves

    def filling_shelves_to_fridge(self, shelves: int) -> None:
        """
        Заполнение полок в холодильнике.
        :param shelves: Количество заполняемых полок
        :raise ValueError: Если количество необходимых к заполнению полок превышает свободное место в холодильнике, то вызываем ошибку
        Примеры:
        >>> fridge = Fridge(10, 0)
        >>> fridge.filling_shelves_to_fridge(2)
        """
        if not isinstance(shelves, int):
            raise TypeError("Количество заполняемых полок должно быть типа int ")
        if shelves < 0:
            raise ValueError("Количество заполняемых полок должно быть положительным числом")
        ...


class CatBowl:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Миска для кота"
        :param capacity_volume: Объем миски
        :param occupied_volume: Объем корма
        Примеры:
        >>> cat_bowl = CatBowl(200, 0) # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем миски должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем миски должен быть положительным числом и больше нуля")
        self.count_shelves = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Объем корма должен быть типа int или float")
        if occupied_volume <= 0:
            raise ValueError("Объем корма должен быть положительным числом и больше нуля")
        self.occupied_shelves = occupied_volume

    def bowl_filling(self, feed: float):
        """
        Функция добавления корма в миску.
        :param feed: Количество корма насыпаемого в миску
        :raise ValueError: Если количество насыпаемого корма превышает количество доступного объема в миске,
        то возвращается ошибка.
        >>> cat_bowl = CatBowl(200, 0)
        >>> cat_bowl.bowl_filling(50)
        """
        ...

    def dirty_bowl(self, day: int):
        """
        Функция по чистке миски.
        :param day: Количество дней с последней чистки миски
        >>> cat_bowl = CatBowl(200, 0)
        >>> cat_bowl.dirty_bowl(3)
        """
        if not isinstance(day, int):
            raise TypeError("Количество дней должно быть типа int ")
        if day < 0:
            raise ValueError("Количество дней должно быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
# Пустая строка