class WithSlots:
    __slots__ = ('name',)
class WithoutSlots:
    pass

w = WithSlots()
wo = WithoutSlots()
wo.new = "OK"      # Работает
# w.new = "Ошибка" # Не работает
print("Без слотов - можно добавлять атрибуты, со слотами - нельзя")