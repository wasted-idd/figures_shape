from src.shapes import BaseShape, SHAPES
from src.exceptions import NoSuchShapeException

def calc_area(shape_name: str, **kwargs) -> float:
    """
    Function evaluates area of the given in shape_name shape area.
    Add shapes parameters (in cm) as keyword arguments in function.
    Returned value will be area of the shape in cm2\n
    Args (all int or float) in dependency of shape:
    - circle: radius;
    - triangle: a, b, c.
    """
    try:
        shape : BaseShape = SHAPES[shape_name](**kwargs)
    except KeyError:
        raise NoSuchShapeException(f"Area cannot be calculated: no such shape '{shape_name}'")
    
    return shape.calculate_area()
