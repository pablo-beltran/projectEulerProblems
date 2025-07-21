import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from EulerProblem1 import euler_problem_1

def test_get_sum():
    obj = euler_problem_1()
    assert obj.get_sum(10) == 23
    assert obj.get_sum(1000) == 233168
    assert obj.get_sum(1) == 0
    assert obj.get_sum(16) == 60