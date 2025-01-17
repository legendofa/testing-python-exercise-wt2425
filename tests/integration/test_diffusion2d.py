"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy
import pytest


@pytest.fixture
def solver():
    return SolveDiffusion2D()


def test_initialize_physical_parameters(solver):
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    d = 4.0
    T_cold = 300.0
    T_hot = 700.0
    w = 20.0
    h = 30.0
    dx = 0.5
    dy = 0.5
    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)
    assert solver.D == pytest.approx(d, abs=0.001)
    assert solver.T_cold == pytest.approx(T_cold, abs=0.001)
    assert solver.T_hot == pytest.approx(T_hot, abs=0.001)
    assert solver.dt == pytest.approx(0.015, abs=0.001)
    solver.dx * solver.dy / (4 * solver.D)
    solver = SolveDiffusion2D()


def test_set_initial_condition(solver):
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    d = 4.0
    T_cold = 300.0
    T_hot = 700.0
    w = 2.0
    h = 3.0
    dx = 0.5
    dy = 0.5
    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)
    u = solver.set_initial_condition()
    assert u.shape == (4, 6)
    # numpy.allclose allows an absolute tolerance of 1e-03, 3 places in this configuration.
    assert numpy.allclose(
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
