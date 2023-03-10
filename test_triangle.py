# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    """define multiple sets of tests as functions to test the triangle testcase"""

    def test_invalid_input1(self):
        """TestCase that involves a decimal input"""
        self.assertEqual(classify_triangle(1.5, 0.5, 1),
                         'InvalidInput',
                         'Invalid Input')

    def test_invalid_input2(self):
        """TestCase that involves a negative input"""
        self.assertEqual(classify_triangle(-1, 5, 8),
                         'InvalidInput',
                         'Invalid Input')

    def test_invalid_input3(self):
        """TestCase that involves an overflow input"""
        self.assertEqual(classify_triangle(201, 100, 150),
                         'InvalidInput',
                         'Invalid Input')

    def test_is_triangle(self):
        """TestCase of an invalid triangle"""
        self.assertEqual(classify_triangle(10, 5, 16),
                         'NotATriangle',
                         '16, 10, 5 is not a triangle')

    def test_right_triangle1(self):
        """TestCase of a right triangle"""
        self.assertEqual(classify_triangle(3, 4, 5),
                         'Right',
                         '3, 4, 5 is a Right triangle')

    def test_right_triangle2(self):
        """TestCase of a right triangle"""
        self.assertEqual(classify_triangle(5, 3, 4),
                         'Right',
                         '5, 3, 4 is a Right triangle')

    def test_equilateral_triangle1(self):
        """TestCase of an equilateral triangle"""
        self.assertEqual(classify_triangle(1, 1, 1),
                         'Equilateral',
                         '1, 1, 1 should be equilateral')

    def test_equilateral_triangle2(self):
        """TestCase of an equilateral triangle"""
        self.assertEqual(classify_triangle(10, 10, 10),
                         'Equilateral',
                         '10, 10, 10 should be equilateral')

    def test_scalene_triangle1(self):
        """TestCase of a scalene triangle"""
        self.assertEqual(classify_triangle(6, 7, 8),
                         'Scalene',
                         '6, 7, 8 should be scalene')

    def test_scalene_triangle2(self):
        """TestCase of a scalene triangle"""
        self.assertEqual(classify_triangle(10, 11, 12),
                         'Scalene',
                         '10, 11, 12 should be scalene')

    def test_isosceles_triangle1(self):
        """TestCase of an isosceles triangle"""
        self.assertEqual(classify_triangle(4, 4, 5),
                         'Isosceles',
                         '4, 4, 5 should be isosceles')

    def test_isosceles_triangle2(self):
        """TestCase of an isosceles triangle"""
        self.assertEqual(classify_triangle(10, 10, 15),
                         'Isosceles',
                         '10, 10, 15 should be isosceles')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
