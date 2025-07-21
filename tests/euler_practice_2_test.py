import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from EulerProblem2 import euler_problem_2

def test_fibonacci_even_sum():
    obj = euler_problem_2()
    # Basic Cases
    assert obj.fibonacci_even_sum(10) == 10  # 2 + 8 = 10
    assert obj.fibonacci_even_sum(100) == 44  # 2 + 8 + 34 = 44
    assert obj.fibonacci_even_sum(4000000) == 4613732  # Original Problem

def test_fibonacci_even_sum_2():
    obj = euler_problem_2()
    # ChatGPT implementation
    assert obj.fibonacci_even_sum_ChatGPT(10) == obj.fibonacci_even_sum(10)
    assert obj.fibonacci_even_sum_ChatGPT(100) == obj.fibonacci_even_sum(100)
    assert obj.fibonacci_even_sum_ChatGPT(4000000) == obj.fibonacci_even_sum(4000000)
