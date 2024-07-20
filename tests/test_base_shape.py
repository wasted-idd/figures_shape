import pytest

from src.shapes import BaseShape

def test_wrong_param_type():
    with pytest.raises(TypeError):
        shape = BaseShape(('a',))
        
def test_wrong_param_value():
    with pytest.raises(TypeError):
        shape = BaseShape(-1,)
