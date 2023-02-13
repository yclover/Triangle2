# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(1.5, 0.5, 1), 'InvalidInput', 'Invalid Input')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(-1, 5, 8), 'InvalidInput', 'Invalid Input')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(201, 100, 150), 'InvalidInput', 'Invalid Input')

    def testIsTriangle(self):
        self.assertEqual(classifyTriangle(16, 10, 5), 'NotATriangle', '16, 10, 5 is not a triangle')

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3, 4, 5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5, 3, 4 is a Right triangle')

    def testEquilateralTriangleA(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1, 1, 1 should be equilateral')

    def testEquilateralTriangleB(self):
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral', '10, 10, 10 should be equilateral')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(6, 7, 8), 'Scalene', '6, 7, 8 should be scalene')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(10, 11, 12), 'Scalene', '10, 11, 12 should be scalene')

    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(4, 4, 5), 'Isosceles', '4, 4, 5 should be isosceles')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(10, 10, 15), 'Isosceles', '10, 10, 15 should be isosceles')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

