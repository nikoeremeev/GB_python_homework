# Задача №10: Найти расстояние между двумя точками пространства

firstPoint = list(map(int, input(
    "Введите координаты первой точки x y z через пробел (например:  2 3 4):")
    .split()))
secondPoint = list(map(int, input(
    "Введите координаты второй точки x y z через пробел (например:  2 3 4):")
    .split()))
result = (((secondPoint[0] - firstPoint[0])**2) + ((secondPoint[1] -
          firstPoint[1])**2) + ((secondPoint[2] - firstPoint[2])**2))**(1/2)
print(f"Расстояние между двумя точками пространства = {round(result, 2)}.")
