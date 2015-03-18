from __future__ import division
from random import random
from math import pi
import matplotlib.pyplot as plt
import unittest

class TestFunctions(unittest.TestCase):
	def test_negative_large(self):
        simulate = MonteCarloSimulation()
        self.assertRaises(AssertionError, lambda: simulate.rain(-259712))

    def test_negative_small(self):
        simulate = MonteCarloSimulation()
        self.assertRaises(AssertionError, lambda: simulate.rain(-8))

    def test_negative_one(self):
        simulate = MonteCarloSimulation()
        self.assertRaises(AssertionError, lambda: simulate.rain(-1))

    def test_zero(self):
        simulate = MonteCarloSimulation()
        self.assertRaises(AssertionError, lambda: simulate.rain(0))

    def test_positive_one(self):
        simulate = MonteCarloSimulation()
        self.assertRaises(AssertionError, lambda: simulate.rain(1))

    def test_negative_decimal(self):
        simulate = MonteCarloSimulation()
        self.assertRaises(AssertionError, lambda: simulate.rain(-3.31))

    def test_positive_decimal(self):
        simulate = MonteCarloSimulation()
        self.assertRaises(AssertionError, lambda: simulate.rain(12.5003))

if __name__ == '__main__':
   unittest.main()
   
   
   