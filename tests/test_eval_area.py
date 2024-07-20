import pytest

from src.exceptions import NoSuchShapeException
from src.eval_area import eval_area

def test_eval_area():
    with pytest.raises(NoSuchShapeException):
        eval_area('rectangle', a=0)