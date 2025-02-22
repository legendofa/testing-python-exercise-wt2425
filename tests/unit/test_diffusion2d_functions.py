"""
Tests for functions in class SolveDiffusion2D using unittest
"""

import unittest
from diffusion2d import SolveDiffusion2D
import numpy
import sys

# Append parent directory path to system paths to allow SolveDiffusion2D import.
sys.path.append("../..")

numpy.set_printoptions(threshold=sys.maxsize)


class TestDiffusion2D(unittest.TestCase):

    def setUp(self):
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        w = 20.0
        h = 30.0
        dx = 0.5
        dy = 0.5
        self.solver.initialize_domain(w, h, dx, dy)
        self.assertAlmostEqual(self.solver.nx, 40, places=3)
        self.assertAlmostEqual(self.solver.ny, 60, places=3)
        self.assertEqual(self.solver.dx, dx)
        self.assertEqual(self.solver.dy, dy)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_physical_parameters
        """
        d = 4.0
        T_cold = 300.0
        T_hot = 700.0
        self.solver.w = 20.0
        self.solver.h = 30.0
        self.solver.dx = 0.5
        self.solver.dy = 0.5
        self.solver.nx = 40.0
        self.solver.ny = 60.0
        self.solver.initialize_physical_parameters(d, T_cold, T_hot)
        self.assertAlmostEqual(self.solver.D, d, places=3)
        self.assertAlmostEqual(self.solver.T_cold, T_cold, places=3)
        self.assertAlmostEqual(self.solver.T_hot, T_hot, places=3)
        self.assertAlmostEqual(self.solver.dt, 0.016, places=3)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.set_initial_condition
        """
        self.solver.D = 4.0
        self.solver.T_cold = 300.0
        self.solver.T_hot = 700.0
        self.solver.w = 2.0
        self.solver.h = 3.0
        self.solver.dx = 0.5
        self.solver.dy = 0.5
        self.solver.nx = 4
        self.solver.ny = 6
        self.solver.dt = 0.015625
        u = self.solver.set_initial_condition()
        self.assertEqual(u.shape, (4, 6))
        # numpy.allclose allows an absolute tolerance of 1e-03, 3 places in this configuration.
        self.assertTrue(
            numpy.allclose(
                a=u,
                b=numpy.array(
                    [
                        [300.0, 300.0, 300.0, 300.0, 300.0, 300.0],
                        [300.0, 300.0, 300.0, 300.0, 300.0, 300.0],
                        [300.0, 300.0, 300.0, 300.0, 300.0, 300.0],
                        [300.0, 300.0, 300.0, 300.0, 300.0, 300.0],
                    ]
                ),
                atol=1e-03,
                rtol=0,
            )
        )


if __name__ == "__main__":
    unittest.main()
