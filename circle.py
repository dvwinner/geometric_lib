import math


def area(r):
    '''
    Возвращает площадь круга, по его радиусу.
    
            Параметры:
                    r (int): Радиус круга
                    
            Возвращаемое значение: 
                    circle_area (float): Площадь круга
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга, по его радиусу.
    
            Параметры:
                    r (int): Радиус круга
                    
            Возвращаемое значение: 
                    circle_length (float): Периметр круга
    '''
    return 2 * math.pi * r

