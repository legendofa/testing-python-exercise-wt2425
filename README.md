# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

```
============================= test session starts ==============================
platform linux -- Python 3.12.8, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/julian/Documents/git/testing-python-exercise-wt2425
collected 5 items

tests/integration/test_diffusion2d.py ..                                 [ 40%]
tests/unit/test_diffusion2d_functions.py F.F                             [100%]

=================================== FAILURES ===================================
____________________________ test_initialize_domain ____________________________

solver = <diffusion2d.SolveDiffusion2D object at 0x7f48baf5aae0>

    def test_initialize_domain(solver):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        w = 20.
        h = 30.
        dx = 0.5
        dy = 0.5
        solver.initialize_domain(w, h, dx, dy)
>       assert solver.nx == pytest.approx(40, abs=0.01)
E       assert 60 == 40 ± 1.0e-02
E
E         comparison failed
E         Obtained: 60
E         Expected: 40 ± 1.0e-02

tests/unit/test_diffusion2d_functions.py:22: AssertionError
__________________________ test_set_initial_condition __________________________

solver = <diffusion2d.SolveDiffusion2D object at 0x7f48baf5a960>

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
>       assert u.shape == (40, 60)
E       assert (60, 60) == (40, 60)
E
E         At index 0 diff: 60 != 40
E         Use -v to get more diff

tests/unit/test_diffusion2d_functions.py:61: AssertionError
----------------------------- Captured stdout call -----------------------------
dt = 0.015625
=========================== short test summary info ============================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - ass...
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition
========================= 2 failed, 3 passed in 0.73s ==========================
```

Changed factor `2` to `4` in formula: `self.dt = dx2 * dy2 / (4 * self.D * (dx2 + dy2))`

```
============================= test session starts ==============================
platform linux -- Python 3.12.8, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/julian/Documents/git/testing-python-exercise-wt2425
collected 5 items

tests/integration/test_diffusion2d.py ..                                 [ 40%]
tests/unit/test_diffusion2d_functions.py .F.                             [100%]

=================================== FAILURES ===================================
_____________________ test_initialize_physical_parameters ______________________

solver = <diffusion2d.SolveDiffusion2D object at 0x7f68172d28a0>

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
>       assert solver.dt == pytest.approx(0.015, abs=0.001)
E       assert 0.0078125 == 0.015 ± 1.0e-03
E
E         comparison failed
E         Obtained: 0.0078125
E         Expected: 0.015 ± 1.0e-03

tests/unit/test_diffusion2d_functions.py:44: AssertionError
----------------------------- Captured stdout call -----------------------------
dt = 0.0078125
=========================== short test summary info ============================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters
========================= 1 failed, 4 passed in 0.75s ==========================
```

Initialization with T_hot instead of T_cold:

```
============================= test session starts ==============================
platform linux -- Python 3.12.8, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/julian/Documents/git/testing-python-exercise-wt2425
collected 3 items

tests/unit/test_diffusion2d_functions.py .dt = 0.015625
.[[700. 700. 700. 700. 700. 700.]
 [700. 700. 700. 700. 700. 700.]
 [700. 700. 700. 700. 700. 700.]
 [700. 700. 700. 700. 700. 700.]]
F

=================================== FAILURES ===================================
__________________________ test_set_initial_condition __________________________

solver = <diffusion2d.SolveDiffusion2D object at 0x7efd126da810>

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
>       assert numpy.array_equal(u,
            numpy.array(
                [
                    [300., 300., 300., 300., 300., 300.],
                    [300., 300., 300., 300., 300., 300.],
                    [300., 300., 300., 300., 300., 300.],
                    [300., 300., 300., 300., 300., 300.]
                ]
            )
        )
E       assert False
E        +  where False = <function array_equal at 0x7efd1481fd30>(array([[700., 700., 700., 700., 700., 700.],\n       [700., 700., 700., 700., 700., 700.],\n       [700., 700., 700., 700., 700., 700.],\n       [700., 700., 700., 700., 700., 700.]]), array([[300., 300., 300., 300., 300., 300.],\n       [300., 300., 300., 300., 300., 300.],\n       [300., 300., 300., 300., 300., 300.],\n       [300., 300., 300., 300., 300., 300.]]))
E        +    where <function array_equal at 0x7efd1481fd30> = numpy.array_equal
E        +    and   array([[300., 300., 300., 300., 300., 300.],\n       [300., 300., 300., 300., 300., 300.],\n       [300., 300., 300., 300., 300., 300.],\n       [300., 300., 300., 300., 300., 300.]]) = <built-in function array>([[300.0, 300.0, 300.0, 300.0, 300.0, 300.0], [300.0, 300.0, 300.0, 300.0, 300.0, 300.0], [300.0, 300.0, 300.0, 300.0, 300.0, 300.0], [300.0, 300.0, 300.0, 300.0, 300.0, 300.0]])
E        +      where <built-in function array> = numpy.array

tests/unit/test_diffusion2d_functions.py:70: AssertionError
=========================== short test summary info ============================
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition
========================= 1 failed, 2 passed in 0.70s ==========================
```

### unittest log

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
