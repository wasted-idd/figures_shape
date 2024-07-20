import pytest

from src.exceptions import NoSuchShapeException
from src.calc_area import calc_area

def test_calc_area():
    with pytest.raises(NoSuchShapeException):
        calc_area('rectangle', a=0)