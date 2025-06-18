"""
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
"""

class euler_problem_1:
    def __init__(self):
        pass

    def get_sum(self, top_num: int):
        sum = 0
        count = 2
        while count < top_num:
            if count % 3 == 0 or count % 5 == 0:
                sum += count  
            count += 1

        return sum
    

obj = euler_problem_1()

test_1 = obj.get_sum(10)
test_2 = obj.get_sum(1000)
test_3 = obj.get_sum(100000)
test_4 = obj.get_sum(22065)
test_5 = obj.get_sum(92065)

print(test_1)
print(test_2)
print(test_3)
print(test_4)
print(test_5)

