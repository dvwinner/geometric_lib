
# Документация #
## Общее описание проекта ##
### Файл circle.py ###
Содержит функции нахождения площади и периметра круга
```
def area(r: int) -> float
def perimeter(r: int) -> float
```

### Файл rectangle.py ###
Содержит функции нахождения площади и периметра прямоугольника
```
def area(a: int, b: int) -> int
def perimeter(a: int, b: int) -> int
```

### Файл square.py ###
Содержит функции нахождения площади и периметра квадрата
```
def area(a: int) -> int
def perimeter(a: int) -> int
```

### Файл triangle.py ###
Содержит функции нахождения площади и периметра треугольника
```
def area(a: int, h: int) -> float
def perimeter(a: int, b: int, c: int) -> int
```

### Файл segment.py ###
Содержит функцию нахождения длины отрезка
```
def distance(x: int, y: int, x1: int, y1: int) -> float
```

## Примеры использования ##
### Примеры использования circle.py
```
import circle

r = int(input())

print(circle.area(r), circle.perimeter(r))
```

### Примеры использования rectangle.py
```
import rectangle

a, b = map(int, input().split())

print(rectangle.area(a, b), rectangle.perimeter(a, b))
```

### Пример использования square.py ###
```
import square

a = int(input())

print(square.area(a), square.perimeter(a))
```

### Примеры использования triangle.py
```
import triangle

a, b, c, h_to_a = map(int, input().split())

print(triangle.area(a, h_to_a), triangle.perimeter(a, b, c))
```

### Примеры использования segment.py
```
import segment

x, y, x1, y1 = map(int, input().split())

print(segment.distance(x, y, x1, y1))
```

### Тесты (unittest)
Были добавлены тесты для функции distance(x, y, x1, y1) в файле библиотеки segment.py

## История коммитов ##
```
4ca8adf (HEAD -> main, origin/main, origin/HEAD) Merge branch 'main' of https://github.com/dvwinner/geometric_lib                                                                                   
dd9f864 Added tests
cdd23cf Update README.md
1d249cc Segment length support
285de64 Update README.md
8b28554 Merge pull request #2 from dvwinner/new_features_465420
f8195b7 (origin/new_features_465420) Added comments in triangle.py funcs
a42e409 Added comments in square.py funcs
da542bf Added comms to rectangle.py funcs | Changed comms to circle.py
7d1cede Added comments in circle.py funcs
bb4e57f Merge pull request #1 from dvwinner/new_features_465420
1992cbe Added triangle.py | Fixed perimeter formula bug in rectangle.py
761ccfe Added rectangle.py
d078c8d L-03: Docs added
8ba9aeb L-03: Circle and square added
```
