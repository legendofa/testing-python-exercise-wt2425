"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

@pytest.fixture
def solver():
    return SolveDiffusion2D()


def test_initialize_domain(solver):
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    w = 20.
    h = 30.
    dx = 0.5
    dy = 0.5
    solver.initialize_domain(w, h, dx, dy)
    assert solver.nx == pytest.approx(40, abs=0.01)
    assert solver.ny == pytest.approx(60, abs=0.01)
    assert solver.dx == dx
    assert solver.dy == dy


def test_initialize_physical_parameters(solver):
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    d = 4.
    T_cold = 300.
    T_hot = 700.
    solver.w = 20.
    solver.h = 30.
    solver.dx = 0.5
    solver.dy = 0.5
    solver.nx = 40.
    solver.ny = 60.
    solver.initialize_physical_parameters(d, T_cold, T_hot)
    assert solver.D == pytest.approx(d, abs=0.01)
    assert solver.T_cold == pytest.approx(T_cold, abs=0.01)
    assert solver.T_hot == pytest.approx(T_hot, abs=0.01)
    assert solver.dt == pytest.approx(0.015, abs=0.001)
    solver.dx * solver.dy / (4 * solver.D)
    solver = SolveDiffusion2D()


def test_set_initial_condition(solver):
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver.D = 4.
    solver.T_cold = 300.
    solver.T_hot = 700.
    solver.w = 2.
    solver.h = 3.
    solver.dx = 0.5
    solver.dy = 0.5
    solver.nx = 4
    solver.ny = 6
    solver.dt = 0.015625
    u = solver.set_initial_condition()
    print(u)
    assert u.shape == (4, 6)
    assert numpy.array_equal(u,
        numpy.array(
            [
                [300., 300., 300., 300., 300., 300.],
                [300., 300., 300., 300., 300., 300.],
                [300., 300., 300., 300., 300., 300.],
                [300., 300., 300., 300., 300., 300.]
            ]
        )
    )
