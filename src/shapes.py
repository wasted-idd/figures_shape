from abc import ABC, abstractmethod
import math

class BaseShapeAbstract(ABC):    
    @abstractmethod
    def calculate_area(self) -> float:
        pass

class BaseShape(BaseShapeAbstract):
    def __init__(self, params: tuple) -> None:
        self.__validate_params(params)
        
    def __validate_params(self, params : tuple):
        for param in params:
            if not any([isinstance(param, float), isinstance(param, int)]):
                raise TypeError(f"Provide float or int type value, not '{type(param)}'")    
            
            if param <= 0:
                raise ValueError(f"Provide correct param value, not '{param}'")
            
    def calculate_area(self) -> float:
        pass

class Circle(BaseShape):
    def __init__(self, radius : float | int) -> None:
        super().__init__((radius,))
        self.radius = radius
        
    def calculate_area(self) -> float:
        self.area = round(math.pow(self.radius, 2) * math.pi, 5)

        return self.area

class Triangle(BaseShape):
    def __init__(self, a : float | int, b : float | int, c : float | int) -> None:
        super().__init__((a, b, c))
        self.a = a
        self.b = b
        self.c = c
        self.is_rectangular = self.__is_rectangular()

    def calculate_area(self) -> float:
        p = (self.a + self.b + self.c) / 2
        self.area = round(
            math.sqrt(
                p * (p - self.a) * (p - self.b) * (p - self.c)
            ),
            5
        )
    
        return self.area
    
    def __is_rectangular(self) -> bool:
        h, c1, c2 = sorted([self.a, self.b, self.c], reverse=True)

        return math.pow(h, 2) == math.pow(c1, 2) + math.pow(c2, 2)


SHAPES = {
    'triangle' : Triangle,
    'circle' : Circle
}