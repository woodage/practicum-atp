from unittest import *    
import doctest
import io
from contextlib import redirect_stdout

def function_to_unittest(list):
    ordered = []
    for item in list:
        if item < 0:
            item *= -1
            item += 1
            
        if item % 2 == 1:
            if not is_prime(item):
                continue
        ordered = insert(item, ordered)
    return ordered


def insert(item, list):
    for index in range(0, len(list)):
        if list[index] > item:
            list.insert(index, item)
            break
    else:
        list.append(item)

    return list


def is_prime(n):
    if n < 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True
	
class ExerciseTest(TestCase):

    def test_1(self):
        test_list = [1, -9, 6, 9, 3]
        function_test_list = function_to_unittest(test_list) 
        negative_number = -9
        odd_non_prime = 9
        self.assertNotIn(negative_number, function_test_list)
        self.assertNotIn(odd_non_prime, function_test_list)
        self.assertTrue(sorted(function_test_list) == function_test_list)     
        
test = ExerciseTest()
suite = TestLoader().loadTestsFromModule(test)
TextTestRunner().run(suite)