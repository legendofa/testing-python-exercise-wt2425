"""
Tests for functions in class SolveDiffusion2D using unittest
"""

import unittest
from diffusion2d import SolveDiffusion2D
import numpy
import sys

# Append parent directory path to allow SolveDiffusion2D import.
sys.path.append('../..')

numpy.set_printoptions(threshold=sys.maxsize)

class TestDiffusion2D(unittest.TestCase):

    def setUp(self):
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        w = 20.
        h = 30.
        dx = 0.5
        dy = 0.5
        self.solver.initialize_domain(w, h, dx, dy)
        self.assertAlmostEqual(self.solver.nx, 40, places=2)
        self.assertAlmostEqual(self.solver.ny, 60, places=2)
        self.assertEqual(self.solver.dx, dx)
        self.assertEqual(self.solver.dy, dy)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_physical_parameters
        """
        d = 4.
        T_cold = 300.
        T_hot = 700.
        self.solver.w = 20.
        self.solver.h = 30.
        self.solver.dx = 0.5
        self.solver.dy = 0.5
        self.solver.nx = 40.
        self.solver.ny = 60.
        self.solver.initialize_physical_parameters(d, T_cold, T_hot)
        self.assertAlmostEqual(self.solver.D, d, places=2)
        self.assertAlmostEqual(self.solver.T_cold, T_cold, places=2)
        self.assertAlmostEqual(self.solver.T_hot, T_hot, places=2)
        self.assertAlmostEqual(self.solver.dt, 0.015, places=2)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.set_initial_condition
        """
        self.solver.D = 4.
        self.solver.T_cold = 300.
        self.solver.T_hot = 700.
        self.solver.w = 2.
        self.solver.h = 3.
        self.solver.dx = 0.5
        self.solver.dy = 0.5
        self.solver.nx = 4
        self.solver.ny = 6
        self.solver.dt = 0.015625
        u = self.solver.set_initial_condition()
        self.assertEqual(u.shape, (4, 6))
        self.assertTrue(numpy.array_equal(u,
            numpy.array(
                [
                    [300., 300., 300., 300., 300., 300.],
                    [300., 300., 300., 300., 300., 300.],
                    [300., 300., 300., 300., 300., 300.],
                    [300., 300., 300., 300., 300., 300.]
                ]
            )
        ))

if __name__ == '__main__':
    unittest.main()
