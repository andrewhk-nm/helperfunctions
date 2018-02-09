# -*- coding: utf-8 -*-
""" This module contains the helper functions I create to help solve puzzles.
"""
import operator
import functools
from functools import namedtuple
import math

def lookup_bodyguards(grid, center, guards=3):
    """ takes a list of text strings representing a 'grid'. 
    Given a 'center' (row, col), returns 'guards' number of adjacent letters.

               
    e.g. guards=3, center=(3, 3)
           A
           B
           C
        JKLxDEF
           G
           H
           I

    returns [A, B, C, D, E, F, G, H, I, J, K, L]
    """
    # Originally for Python Challenge problem 3


def process_text(filename):
    """ Takes a filename that holds a rectangular block of text.
    Return a list strings from that block.
        



    """
    # Originally for Python Challenge problem 3
        
    # Create a list of lists. Each member list is a line of text.
    a_list = list()
    with open(filename, encoding='utf-8') as a_file:
        for a_line in a_file:
            a_list.append(a_line.strip())          

    return a_list

def next_collatz_number(n):
    """ The following iterative sequence is defined for the set of positive integers:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)
    """
    # originally for problem13
    if n % 2:
        # Odd numbers
        return 3 * n + 1
    return n // 2

def get_grid_posititions_from_shape(grid, shape, x, y, n=4):
    """ given a grid (A list of lists of integers), starting positions x and y, and a shape,
    returns a list of n (default 4) integers.
    assumes grid's index starts at 0

    raises IndexError if you try to get a location off of the grid.
    """
    
    # originally for problem11
    return [int(grid[here_x][here_y]) for here_x, here_y in gen_grid_positions((x, y), shape, n)]
        
def prod(factors):
    """ Quick prod function from StackExchange.
    """
    # Not TDD
    return functools.reduce(operator.mul, factors, 1)
    
class EnumGenGridPositionsShapes():
    """ Holds the contants for the shapes accepted by gen_grid_positions
    This should be an iterable, but isn't yet!
    This should be an iterable now... which means tests!
    """
    # TDD
    # Originally for problem11
    HORIZONTAL = 'horizontal'
    DIAGONAL_SE = 'diagonal_se'
    VERTICAL = 'vertical'
    DIAGONAL_SW = 'diagonal_sw'
        
    def __init__(self):
        self.shapes = [
            self.HORIZONTAL,
            self.DIAGONAL_SE,
            self.VERTICAL, 
            self.DIAGONAL_SW,
            ]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        try:
            next_shape = self.shapes[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return next_shape

        


def gen_grid_positions(start, shape, n):
    """ Generates the next position to go to in a grid based on the shape.
    returns n items, starting at start. 
        
    valid shape entries are contained in class 'Enum_gen_grid_positions_shapes':
    'horizontal'
    'diagonal_se'
    'vertical'
    'diagonal_sw'
    """
    #e.g.
    #2 3 1 4 7
    #3 1 3 5 2
    #5 6 3 2 5
    #6 4 6 3 2
        
    #(1, 1), 'horizontal', 4 yields:
    #    2 (1, 1)
    #    3 (1, 2)
    #    1 (1, 3)
    #    4 (1, 4)
    #(2, 1), 'diagonal_se', 3 yields:
    #    3 (2, 1)
    #    3 (3, 3)
    #    2
    #(3, 2), 'vertical', 4 yields:
    #    2
    #    3
    #    1
    #    default
    #(4, -1), 'diagonal_sw', 4 yields:
    #    default
    #    1
    #    1
    #    5
    #"""
    # TDD
    # Originally for problem11
    
        
    SHAPE = EnumGenGridPositionsShapes
    if shape == SHAPE.HORIZONTAL:
        d_row_d_col = (0, 1)
    elif shape == SHAPE.DIAGONAL_SE:
        d_row_d_col = (1, 1)
    elif shape == SHAPE.VERTICAL:
        d_row_d_col = (1, 0)
    elif shape == SHAPE.DIAGONAL_SW:
        d_row_d_col = (1, -1)
    else:
        raise TypeError('shape argument does not accept shape={}.'.format(shape))

    row, col = start
    for n_ in range(0, n):
        yield (row + (n_ * d_row_d_col[0]), col + (n_ * d_row_d_col[1]))

def gen_primes(start=2, stop=None):
    """ Returns the next prime number, 
    optionally start searching at start,
    optionally end searching at stop.

    yields the next prime int.
    """
    
    # Originally for problem 10
    # TDD
    for p in range(start, stop):
        if isprime(p):
            yield p
            
def gen_pythagorean_triplet(min_c=5, max_c=100):
    """ Returns the next set of Pythagorean triplets as a tuple (a, b, c).
    Up to max_c
    for a**2 + b**2 == c**2 and a < b
    Generator
    """
    # Originally for problem 9
    # TDD
    Pythag = namedtuple('Pythag', 'a b c')
    return_tuple = Pythag(3, 4, 5)
        
    for c in range(min_c, max_c):
        for a in range(1, c):
            for b in range(a + 1, c):
                if a**2 + b**2 == c**2 and a < b:
                    return_tuple = Pythag(a, b, c)
                    yield return_tuple

    
def prime_factorization_mark2(n):
    """ Returns a dictionary of the prime factors of n.
    key=prime factor
    value=count of occurances of that prime factor
    """
    
    # Start pulling out prime factors of n
    # e.g.
    # n = 12
    # p = {2: 1}, n = 6
    # p = {2: 2}, n = 3
    # p = {2: 2, 3: 1}, n = 1
    # exit loop
    # return p

    p = dict()
    while n > 1:
        # print('p={}'.format(p))
        # print('n={} at while'.format(n))
        for x in range(2, n + 1):
            # print('x={}'.format(x))
            # print('n={} at while.for'.format(n))
            while True:
                #input('Loop paused. <ENTER> to continue.')
                if n % x == 0:
                    if isprime(x):
                        n /= x
                        try:
                            p[x] += 1
                        except KeyError:
                            p[x] = 1
                        # print('p, right after try: {}'.format(p))
                        # print('n, right after try: {}'.format(n))

                    else:
                        # print('breaking because {} is not prime.'.format(x))
                        break
                else:
                    # print('breaking because {} is not divisible by {}.'.format(n, x))
                    break
            if n == 1:
                break
    return p


    
def prime_factorization(n):
    """ DEPRECIATED. Sends input n to 'prime_factorization_mark2(n)'
        
    Returns a dictionary of the prime factors of n.
    key=prime factor 
    value=count of occurances of that prime factor
    """
    # Send input to the new method
    
    return prime_factorization_mark2(n)
        

        
def isprime(n, treat_1_as_prime=False):
    """
    n must be >= 2 unless the flag treat_1_as_prime is set to True. Then an n of 1 will return "prime"
    returns True if n is prime, False if not prime.
    Returns False for all values < 2
    """
    
    if treat_1_as_prime and n == 1:
        return True
    else:
        if n < 2:
            return False
    # if the only factors of a number are 1 and itself, it's prime.
    #g_f = gen_factors(n)
    gen_some_factors = gen_factors(n)
    for a in gen_some_factors:
        if a != 1 and a != n:
            # A non-1 or n factor has been found. It is not prime.
            #print('{} is not prime because of this factor {}'.format(n,a))
            return False
    return True


def factors(n):
    """ Return a set of all factors of n
    """
    #s = {f for f in range(1, math.trunc(n / 2) + 1) if n % f == 0}
    s = {f for f in range(1, int(math.sqrt(n)) + 1) if n % f == 0}
    # create a union of the lower half of the factors with the upper half.
    s = s.union({n // m for m in s})
    return s

def primes_from_a_set(s, return_composites_too=False):
    """ Takes a set of numbers and returns a set of the prime members,
        discarding the composites. Returns as a tuple (primes, )
        If get_composites_too is True, returns a tuple ({primes}, {composites})
    """
    
    primes = {p_f for p_f in s if len(factors(p_f)) == 2}
    if return_composites_too:
        composites = s.difference(primes)
        return (primes, composites)
    return (primes, set())

def who_am_i(self):
    """ Returns the name of the function that is currently running.
    """
    stack = traceback.extract_stack()
    filename, codeline, funcName, text = stack[-2]
    # print('filename={}, codeline={}, funcName={}, text ={}'.format(filename, codeline, funcName, text))
    return funcName

def generate_crossproduct(start, end, step):
    """
    Creates a cross product generator. begins the multiplication at 'start', 
    and goes to 'end' (not including 'end'). It changes by 'step'.
    The second loop only goes from 'start' to the current spot, so that 
    only a trangle is gone through (instead of a square)
    yields a cross_product number.
    """
    #This can be faster.
    #If I make the For loops go 
    #for c in range(100 to 999)
    #    for d in range(100 to c)
    #That'll cut off the mirrored side of the times tables!
    #Changes like this would really benefit from TDD!
    for n1 in range(start, end, step):
        for n2 in range(start, n1, step):
            yield n1 * n2

def ispalindrome(n):
    """ Takes a number, and returns true if it is a palindrome,
    false otherwise.
    """
    # Written for project Euler problem 4
    m = str(n)
    m_list = [c for c in m]
    for d in range(1, len(m_list) // 2 + 1):
        #print('d = {}, m_list[d-1] = {}, m_list[-d] = {}, m_list[d-1] != m_list[-d] = {}'.format(d, m_list[d-1], m_list[-d], m_list[d-1] != m_list[-d]))
        if m_list[d - 1] != m_list[-d]:
            return False
    return True

def gen_factors(n):
    """
    generator
    return the factors of n.
    """
    # Hold the generated factors in a list so that the generator can return the other half easier.
    cache = list()
    for a in range(1, int(math.sqrt(n)) + 1):
        if n % a == 0:
            if a != math.sqrt(n):
                # only add to the cache if it's not the square root factor. 
                # Otherwise the square root factor gets generated twice, 
                # once on the forward run, and again on the back end.
                cache = [a] + cache
            yield a
    for a in cache:
        yield n // a

def gen_factors_poorly(n):
    """
    generator
    return the factors of n, starting with n and going to 2. or something
    for problem 3.
    DEPRECIATED. use "gen_factors" instead.
    """
    # TODO: Rewrite the reverse section to use sqrt instead of n/2
    for a in range((n + 1) // 2, 2, -1):
        if n % a == 0:
            yield a
