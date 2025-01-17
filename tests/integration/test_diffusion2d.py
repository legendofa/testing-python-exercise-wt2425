"""
Tests for functionality checks in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import pytest

@pytest.fixture
def solver():
    return SolveDiffusion2D()

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
    assert solver.dt == pytest.approx(0.015, abs=0.001)
    solver.dx * solver.dy / (4 * solver.D)
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
    for x in range(40):
        for y in range(60):
            assert u[x, y] == pytest.approx(300., abs=0.01)
