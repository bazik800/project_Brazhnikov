#Создание базового класса "Фигура" и его наследование для создания классов
#"Квадрат", "Прямоугольник" и "Круг". Класс "Фигура" будет иметь общие методы,
#такие как вычисление площади и периметра, а классы-наследники будут иметь
#специфичные методы и свойства. 
class Figura:
    def area(self):
        raise NotImplementedError("Этот метод должен быть реализован в наследнике")
    def perimeter(self):
        raise NotImplementedError("Этот метод должен быть реализован в наследнике")


class Kvadrat(Figura):
    def __init__(self, storona):
        self.storona = storona
    def area(self):
        return self.storona * self.storona
    def perimeter(self):
        return 4 * self.storona

class Pryamougolnik(Figura):
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy
    def area(self):
        return self.dx * self.dy
    def perimeter(self):
        return 2 * (self.dx + self.dy)


class Krug(Figura):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        # Поскольку math.pi не используем, можно например взять 3.14
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius


if __name__ == "__main__":
    square = Kvadrat(4)
    rectangle = Pryamougolnik(3, 6)
    circle = Krug(5)

    print(f"Квадрат: площадь = {square.area()}, периметр = {square.perimeter()}")
    print(f"Прямоугольник: площадь = {rectangle.area()}, периметр = {rectangle.perimeter()}")
    print(f"Круг: площадь = {circle.area()}, периметр = {circle.perimeter()}")
