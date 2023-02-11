class Coffee:
    def __init__(self, size: str, roast_degree: str, sugar: int):
        """
        Подготовка объекта "Кофе"
        :param size: Размер кружки
        :param roast_degree: Степень обжарки зерен
        :param sugar: Количество ложек сахара
        """
        self._size_options = ["S", "M", "L", "XL"]
        self._roast_options = ["blonde", "medium", "dark"]

        if not isinstance(size, str):
            raise TypeError("Размер кружки должен быть типа str")
        if size in self._size_options:
            self._size = size
        else:
            raise ValueError("Размер кружки должен быть: S, M, L или XL")

        if not isinstance(roast_degree, str):
            raise TypeError("Степень обжарки зерен должна быть типа str")
        if roast_degree in self._roast_options:
            self._roast_degree = roast_degree
        else:
            raise ValueError("Степень обжарки зерен должна быть: blonde, medium или dark")

        if not isinstance(sugar, int):
            raise TypeError("Количество ложек сахара должно быть типа int")
        if sugar < 0:
            raise ValueError("Количество ложек сахара должно быть положительным числом")
        self._sugar = sugar

    def __str__(self):
        return f"Размер кружки: {self._size}, степень обжарки: {self._roast_degree}, количество ложек сахара: {self._sugar}"

    def __repr__(self):
        return f"{self.__class__.__name__}(size={self._size!r}, roast_degree={self._roast_degree!r}, sugar={self._sugar!r})"

    def my_cup(self, cup: str) -> None:
        """
        Функция для выбора кружки: своя кружка или одноразовый стакан.
        """

    def price(self) -> int:
        """
        Функция, которая возвращает стоимость кофе в зависимости от выбранных параметров.
        :return: Стоимость кофе
        """


class Cappuccino(Coffee):
    def __init__(self, size: str, roast_degree: str, sugar: int, milk: str):
        """
        Подготовка объекта "Капучино"
        :param size: Размер кружки
        :param roast_degree: Степень обжарки зерен
        :param sugar: Количество ложек сахара
        :param milk: Вид молока
        """
        super().__init__(size, roast_degree, sugar)

        self._milk_options = ["коровье", "миндальное", "соевое", "кокосовое"]

        if not isinstance(milk, str):
            raise TypeError("Вид молока должен быть типа str")
        if milk in self._milk_options:
            self._milk = milk
        else:
            raise ValueError("Вид молока должен быть: коровье, миндальное, соевое или кокосовое")

    def __str__(self):
        return f"Размер кружки: {self._size}, степень обжарки: {self._roast_degree}, количество ложек саха: {self._sugar}, молоко: {self._milk}"

    def __repr__(self):
        return f"{self.__class__.__name__}(size={self._size!r}, roast_degree={self._roast_degree!r}, sugar={self._sugar!r}), milk={self._milk!r}"

    def price(self) -> int:
        """
        Перезагружаем функцию, которая возвращает стоимость кофе с учетом молока.
        :return: Стоимость кофе
        """


class Raf(Coffee):
    def __init__(self, size: str, roast_degree: str, sugar: int, topping: str):
        """
        Подготовка объекта "Раф"
        :param size: Размер кружки
        :param roast_degree: Степень обжарки зерен
        :param sugar: Количество ложек сахара
        :param topping: Топпинг
        """
        super().__init__(size, roast_degree, sugar)

        self._topping_options = ["малина", "лаванда", "карамель", "шоколад"]

        if not isinstance(topping, str):
            raise TypeError("Топпинг должен быть типа str")
        if topping in self._topping_options:
            self._topping = topping
        else:
            raise ValueError("Топпинг должен быть: малина, лаванда, карамель или шоколад")

    def __str__(self):
        return f"Размер кружки: {self._size}, степень обжарки: {self._roast_degree}, количество ложек сахара: {self._sugar}, топпинг: {self._milk}"

    def __repr__(self):
        return f"{self.__class__.__name__}(size={self._size!r}, roast_degree={self._roast_degree!r}, sugar={self._sugar!r}), topping={self._topping!r}"

    def price(self) -> int:
        """
        Перезагружаем функцию, которая возвращает стоимость кофе с учетом топпинга.
        :return: Стоимость кофе
        """


if __name__ == "__main__":
    pass
#Пустая строка