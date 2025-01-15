"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest

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
    w = 20.
    h = 30.
    dx = 0.5
    dy = 0.5
    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)
    assert solver.D == pytest.approx(d, abs=0.01)
    assert solver.T_cold == pytest.approx(T_cold, abs=0.01)
    assert solver.T_hot == pytest.approx(T_hot, abs=0.01)
    solver = SolveDiffusion2D()


def test_set_initial_condition(solver):
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    d = 4.
    T_cold = 300.
    T_hot = 700.
    w = 20.
    h = 30.
    dx = 0.5
    dy = 0.5
    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)
    u = solver.set_initial_condition()
    assert u.shape == (40, 60)
    assert u[0, 0] == pytest.approx(300., abs=0.01)
    assert u[20, 30] == pytest.approx(300., abs=0.01)
    assert u[39, 49] == pytest.approx(300., abs=0.01)
