class Animal:
    __slots__ = ('type', 'weight')
a = Animal()
a.type = "Собака"
a.weight = 10
a.color = "Красный"  # Ошибка! __slots__ запрещает новые атрибуты