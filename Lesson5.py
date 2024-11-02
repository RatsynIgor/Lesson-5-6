import inspect
print('Lesson 5: Class Introinspection\n')


class Marker:
    color: str
    weight: float
    price: int
    isPresent: bool

    def __init__(self, color='black'):
        self.color = color
        self.weight = 1.22
        self.price = 3
        self.isPresent = True

    def __str__(self):
        if self.isPresent:
            return f'color:{self.color}\nprice:{self.price}UAH'
        else:
            return 'marker is absent'

    def set_price(self, price: int):
        self.price = price


red_marker = Marker()
print(red_marker)

check_module = inspect.ismodule(red_marker)
print(check_module)
check_class = inspect.isclass(Marker)

print(inspect.isclass(Marker))
print(inspect.isclass(red_marker))

red_marker.set_price(10)
print(red_marker)

print(inspect.ismethod(red_marker.set_price))
print(inspect.isfunction(red_marker.set_price))




blue_marker = Marker()
print(blue_marker)

blue_marker.set_price(12) #Встановлення нової ціни
print(blue_marker)

print(inspect.isclass(blue_marker)) #Перевірка чи є синій маркер классом
print(inspect.ismethod(blue_marker.set_price)) #Перевірка чи є ціна синього маркера методом
print(inspect.isfunction(blue_marker.set_price)) #Перевірка чи є ціна синього маркера функцією

