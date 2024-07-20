from src.shapes import Circle

def test_calculate_area():
    circle = Circle(1)
    assert circle.calculate_area() == 3.14159