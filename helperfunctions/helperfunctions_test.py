# -*- coding: utf-8 -*-
"""
This is the unit test module for my Project Euler python solutions.
"""

import unittest
from functools import namedtuple

import helperfunctions as hf

## This should go in the python challenge test module
##class Test_PythonChallenge_test1(unittest.TestCase):
##    known_answers_gen_char_neighbor = [('U', 'kAeMKENi'),
##                                       ('K', 'AewULNih'),
##                                       ('L', 'ewtKEihr')
##                                       ]
##    
##    def test_HelperFunctions_gen_char_neighbor_known_answers(self):
##        """ Test some known answers of the generator.
##        """
##        test_gen = hf.gen_char_neighbor('problem3_source_mess.txt')
##        for center, neighbors in self.known_answers_gen_char_neighbor:
##            print('center={}, neighbors={}'.format(center, neighbors))
##            test_ans = next(test_gen)
##            print('test_ans={}'.format(test_ans))
##            self.assertEqual((center, neighbors), test_ans)

class Test_testtest(unittest.TestCase):
    def test_A(self):
        print(hf.factors(12))
        self.assertTrue(True)
        
class Test_PythonProjectEuler_problem11_and_Helper(unittest.TestCase):
    """ Collection of Tests focusing on problem11 and the HelperFunctions 
    functions that I may create there.
    """

    SHAPE = hf.EnumGenGridPositionsShapes()
    
    known_answers_Enum_gen_grid_positions_shapes_in_order = ['horizontal',
                                                             'diagonal_se',
                                                             'vertical',
                                                             'diagonal_sw',
                                                            ]

    def test_get_grid_posititions_from_shape(self):
        
        grid_str = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
        49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
        81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
        52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
        22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
        24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
        32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
        67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
        24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
        21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
       78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
        16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
        86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
        19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
        04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
        88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
        04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
        20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
        20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
        01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""
        grid = [s.split() for s in grid_str.splitlines()]
        Input = namedtuple('Input', ['shape', 'row', 'col', 'n'])
        known_answers = [
            (Input(self.SHAPE.HORIZONTAL, 1, 1, 4), [49, 99, 40, 17]),
            (Input(self.SHAPE.HORIZONTAL, 2, 2, 4), [31, 73, 55, 79]),
            (Input(self.SHAPE.VERTICAL, 2, 2, 4), [31, 95, 16, 32]),
            (Input(self.SHAPE.DIAGONAL_SE, 2, 2, 4), [31, 23, 51, 3]),
            (Input(self.SHAPE.VERTICAL, 2, 0, 4), [81, 52, 22, 24]),
            (Input(self.SHAPE.VERTICAL, 2, 19, 4), [65, 91, 80, 50]),
            ]
        for input_, output in known_answers:
            self.assertListEqual(output, hf.get_grid_posititions_from_shape(grid, input_.shape, input_.row, input_.col, input_.n))
    
    def test_get_grid_posititions_from_shape_exceptions(self):
        
        grid_str = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
        49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
        81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
        52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
        22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
        24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
        32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
        67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
        24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
        21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
        78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
        16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
        86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
        19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
        04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
        88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
        04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
        20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
        20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
        01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""
        grid = [s.split() for s in grid_str.splitlines()]
        Input = namedtuple('Input', ['shape', 'row', 'col', 'n'])
        known_exceptions = [
            (Input(self.SHAPE.VERTICAL, 19, 0, 4), IndexError),
            (Input(self.SHAPE.HORIZONTAL, 19, 19, 4), IndexError),
            (Input(self.SHAPE.HORIZONTAL, 19, 19, 4), IndexError),
            ]
        for input_, output in known_exceptions:
            #self.assertRaises(IndexError, IndexError)
            self.assertRaises(output, hf.get_grid_posititions_from_shape, grid, input_.shape, input_.row, input_.col, input_.n)
            


    def test_Enum_gen_grid_positions_shapes(self):
        
        SHAPES = hf.EnumGenGridPositionsShapes()
        self.assertListEqual([shape for shape in SHAPES], self.known_answers_Enum_gen_grid_positions_shapes_in_order)


    def test_gen_grid_positions_known_answers(self):
        
        known_answers_gen_grid_positions = [
            (((1, 1), self.SHAPE.VERTICAL, 4), [(1, 1), (2, 1), (3, 1), (4, 1)]),
            (((1, 1), self.SHAPE.HORIZONTAL, 4), [(1, 1), (1, 2), (1, 3), (1, 4)]),
            (((1, 1), self.SHAPE.DIAGONAL_SE, 4), [(1, 1), (2, 2), (3, 3), (4, 4)]),
            (((1, 1), self.SHAPE.DIAGONAL_SW, 4), [(1, 1), (2, 0), (3, -1), (4, -2)]),
            (((2, 2), self.SHAPE.HORIZONTAL, 4), [(2, 2), (2, 3), (2, 4), (2, 5)]),
            (((2, 2), self.SHAPE.DIAGONAL_SE, 4), [(2, 2), (3, 3), (4, 4), (5, 5)]),
            ]
        for test, answer in known_answers_gen_grid_positions:
            ans = hf.gen_grid_positions(start=test[0], shape=test[1], n=test[2])
            self.assertListEqual(list(ans), answer)

class Test_PythonProjectEuler_problem10_and_Helper(unittest.TestCase):
    """ Collection of Tests focusing on problem10 and the HelperFunctions 
    functions that I may create there.
    """
    # Format is a list of tuples. Each tuple contains a tuple (start, stop) and a list [expected, primes, in, order].
    # [(, ), [],
    # ]
    known_answers_gen_primes = [((2, 5), [2, 3]),
                                ((2, 8), [2, 3, 5, 7]),
                                ((5, 23), [5, 7, 11, 13, 17, 19]),
                                ((5, 24), [5, 7, 11, 13, 17, 19, 23]),
                               ]
    
    def test_gen_primes_known_answers(self):
        
        for packed_answer in self.known_answers_gen_primes:
            ans_tuple, ans_list = packed_answer
            start, stop = ans_tuple
            test_gen = hf.gen_primes(start, stop)
            self.assertListEqual(ans_list, list(test_gen))
            
    def test_gen_primes_are_primes(self):
        
        primes = hf.gen_primes(2, 9)
        self.assertTrue(hf.isprime(next(primes)))



class Test_PythonProjectEuler_problem9_and_Helper(unittest.TestCase):
    """ Collection of Tests focusing on problem9 and the HelperFunctions 
    functions that I may create there.
    """
    
    def test_gen_pythagorean_triplet(self):
        # hf.gen_pythagorean_triplet
        # does a**2 + b**2 == c**2?
        
        pythag = hf.gen_pythagorean_triplet(min_c=5, max_c=100)
        loop_counter = 0
        for r in pythag:
            loop_counter += 1
            print('Testing triplet: a={}, b={}, c={}'.format(r.a, r.b, r.c))
            self.assertEqual(r.a ** 2 + r.b ** 2, r.c ** 2)
        print('{} triplets tested.'.format(loop_counter))



class Test_PythonProjectEuler_HelperFunctions(unittest.TestCase):
    """ Collection of Tests for the helper functions I create for Project Euler puzzles.
    """

    known_answers_prime_factorization = {2: {2: 1}, 
                                         3: {3: 1}, 
                                         4: {2: 2}, 
                                         5: {5: 1}, 
                                         6: {2: 1, 3: 1}, 
                                         7: {7: 1}, 
                                         8: {2: 3}, 
                                         9: {3: 2},
                                         10: {2: 1, 5: 1},
                                         11: {11: 1},
                                         12: {2: 2, 3: 1},
                                         13: {13: 1},
                                         14: {2: 1, 7: 1},
                                        }

    known_answers_gen_factors = {1: [1],
                                 2: [1, 2],
                                 3: [1, 3],
                                 4: [1, 2, 4],
                                 5: [1, 5],
                                 6: [1, 2, 3, 6],
                                 7: [1, 7],
                                 8: [1, 2, 4, 8],
                                 9: [1, 3, 9],
                                }
   
    known_answers_isprime = {1: False,
                             2: True,
                             3: True,
                             4: False,
                             5: True,
                            }

    def test_isprime_known_answers(self):
        
        for n, result in self.known_answers_isprime.items():
            self.assertEqual(hf.isprime(n), result)

    def test_prime_factorization_returns_dict(self):
        
        result = hf.prime_factorization(2)
        self.assertIsInstance(obj=result, cls=dict)

    def test_prime_factoriation_known_answers(self):
        
        for n, result in self.known_answers_prime_factorization.items():
            self.assertDictEqual(hf.prime_factorization(n), result)

    def test_prime_factorization_12(self):
        
        self.assertDictEqual(hf.prime_factorization(12), {2: 2, 3: 1})

    def test_gen_factors_known_answers(self):
        """ Test for the function 'gen_factors(n)'
        """
        
        for n, result_list in self.known_answers_gen_factors.items():
            factor_generator = hf.gen_factors(n)
            for f in result_list:
                next_factor = next(factor_generator)
                self.assertEqual(f, next_factor, "'gen_factors' generator did not give expected factor.\nFor n={}, Expected Factor={}, Generated Factor={}".format(n, f, next_factor))
    



##class Test_PythonProjectEuler_problem3_mark2_test(unittest.TestCase):
##    """
##    Test set for Project Euler problem3_mark2
##
##    Goal for problem3:
##        The prime factors of 13195 are 5, 7, 13 and 29.
##        What is the largest prime factor of the number 600851475143 ?
##
##    """
##    
##    # known_answers dictionary in the form of {number: largest_prime_factor, }
##    known_answers = {13195: 29, 10: 5}
##    known_factor_sets = {10: {1, 2, 5}}
##
##    def test_p3m2_isprime(self):
##        self.fail("problem3_mark2 'isprime' test not yet implemented")
##    
##    def test_p3m2_isfactor(self):
##        self.fail("problem3_mark2 'isfactor' test not yet implemented")
##
##    def test_p3m2_is_largest_factor(self):
##        for n in self.known_answers:
##            self.assertEqual(problem3_mark2(n), self.known_answers[n])
##
##    def test_p3m2_factors_returns_a_set(self):
##        # This function, factors(n), should always return a set of factors given any n.
##        # This test will check the returned type.
##        # TODO: what is this test supposed to do?
##        for n in self.known_factor_sets:
##            self.assertEqual(problem3_mark2)
##
##
##
##
##
##class Test_PythonProjectEuler_generic_test(unittest.TestCase):
##    """
##    Test set for Project Euler problems.
##    Copy this test class for different problem sets.
##    """
##    #from PythonProjectEuler import choose_problem  # Replace 'choose_problem' with the actual problem to test
##    def test_generic_not_implemented(self):
##        self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()
