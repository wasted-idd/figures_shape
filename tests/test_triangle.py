import pytest

from src.shapes import Triangle

@pytest.fixture
def not_rect_triangle():
    return Triangle(17, 2, 5)

@pytest.fixture
def rect_triangle():
    return Triangle(5, 4, 3)


def test_calculate_area(rect_triangle : Triangle):
    assert rect_triangle.calculate_area() == 6

def test_triangle_is_rect(rect_triangle: Triangle):
    assert rect_triangle.is_rectangular == True

def test_triangle_is_not_rect(not_rect_triangle: Triangle):
    assert not_rect_triangle.is_rectangular == False