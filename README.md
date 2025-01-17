# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

```
======================= test session starts =======================
platform linux -- Python 3.12.8, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/julian/Documents/git/testing-python-exercise-wt2425
collected 3 items

tests/unit/test_diffusion2d_functions.py F..                [100%]

============================ FAILURES =============================
_____________________ test_initialize_domain ______________________

solver = <diffusion2d.SolveDiffusion2D object at 0x7fb625562900>

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

tests/unit/test_diffusion2d_functions.py:25: AssertionError
===================== short test summary info =====================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 60 == 40 ± 1.0e-02
=================== 1 failed, 2 passed in 0.41s ===================
```

Changed factor `2` to `4` in formula: `self.dt = dx2 * dy2 / (4 * self.D * (dx2 + dy2))`:

```
============================= test session starts ==============================
platform linux -- Python 3.12.8, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/julian/Documents/git/testing-python-exercise-wt2425
collected 3 items

tests/unit/test_diffusion2d_functions.py .F.                             [100%]

=================================== FAILURES ===================================
_____________________ test_initialize_physical_parameters ______________________

solver = <diffusion2d.SolveDiffusion2D object at 0x7f330e6329c0>

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
>       assert solver.dt == pytest.approx(0.015, abs=0.001)
E       assert 0.0078125 == 0.015 ± 1.0e-03
E
E         comparison failed
E         Obtained: 0.0078125
E         Expected: 0.015 ± 1.0e-03

tests/unit/test_diffusion2d_functions.py:48: AssertionError
----------------------------- Captured stdout call -----------------------------
dt = 0.0078125
=========================== short test summary info ============================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.0078125 == 0.015 ± 1.0e-03
========================= 1 failed, 2 passed in 0.41s ==========================
```

Initialization with T_hot instead of T_cold:

```
=================== test session starts ===================
platform linux -- Python 3.12.8, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/julian/Documents/git/testing-python-exercise-wt2425
collected 3 items

tests/unit/test_diffusion2d_functions.py ..F        [100%]

======================== FAILURES =========================
_______________ test_set_initial_condition ________________

solver = <diffusion2d.SolveDiffusion2D object at 0x7f7c3aecdc40>

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
>       assert numpy.allclose(a=u,
            b=numpy.array(
                [
                    [300., 300., 300., 300., 300., 300.],
                    [300., 300., 300., 300., 300., 300.],
                    [300., 300., 300., 300., 300., 300.],
                    [300., 300., 300., 300., 300., 300.]
                ]
            ),
            atol=1e-3,
            rtol=0,
        )
E       assert False
E        +  where False = <function allclose at 0x7f7c08620070>(a=array([[700., 700., 700., 700., 700., 700.],\n       [700., 700., 700., 700., 700., 700.],\n       [700., 700., 700., 700., 700., 700.],\n       [700., 700., 700., 700., 700., 700.]]), b=array([[300., 300., 300., 300., 300., 300.],\n       [300., 300., 300., 300., 300., 300.],\n       [300., 300., 300., 300., 300., 300.],\n       [300., 300., 300., 300., 300., 300.]]), atol=0.001, rtol=0)
E        +    where <function allclose at 0x7f7c08620070> = numpy.allclose
E        +    and   array([[300., 300., 300., 300., 300., 300.],\n       [300., 300., 300., 300., 300., 300.],\n       [300., 300., 300., 300., 300., 300.],\n       [300., 300., 300., 300., 300., 300.]]) = <built-in function array>([[300.0, 300.0, 300.0, 300.0, 300.0, 300.0], [300.0, 300.0, 300.0, 300.0, 300.0, 300.0], [300.0, 300.0, 300.0, 300.0, 300.0, 300.0], [300.0, 300.0, 300.0, 300.0, 300.0, 300.0]])
E        +      where <built-in function array> = numpy.array

tests/unit/test_diffusion2d_functions.py:70: AssertionError
------------------ Captured stdout call -------------------
[[700. 700. 700. 700. 700. 700.]
 [700. 700. 700. 700. 700. 700.]
 [700. 700. 700. 700. 700. 700.]
 [700. 700. 700. 700. 700. 700.]]
================= short test summary info =================
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert False
=============== 1 failed, 2 passed in 0.41s ===============
```

#### Integration tests

Changed factor `2` to `4` in formula: `self.dt = dx2 * dy2 / (4 * self.D * (dx2 + dy2))`

```
======================= test session starts =======================
platform linux -- Python 3.12.8, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/julian/Documents/git/testing-python-exercise-wt2425
collected 2 items

tests/integration/test_diffusion2d.py F.                    [100%]

============================ FAILURES =============================
_______________ test_initialize_physical_parameters _______________

solver = <diffusion2d.SolveDiffusion2D object at 0x7effe4712270>

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
>       assert solver.dt == pytest.approx(0.015, abs=0.001)
E       assert 0.0078125 == 0.015 ± 1.0e-03
E
E         comparison failed
E         Obtained: 0.0078125
E         Expected: 0.015 ± 1.0e-03

tests/integration/test_diffusion2d.py:31: AssertionError
---------------------- Captured stdout call -----------------------
dt = 0.0078125
===================== short test summary info =====================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - assert 0.0078125 == 0.015 ± 1.0e-03
=================== 1 failed, 1 passed in 0.42s ===================
```

Initialization with T_hot instead of T_cold:

```
======================= test session starts =======================
platform linux -- Python 3.12.8, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/julian/Documents/git/testing-python-exercise-wt2425
collected 2 items

tests/integration/test_diffusion2d.py .F                    [100%]

============================ FAILURES =============================
___________________ test_set_initial_condition ____________________

solver = <diffusion2d.SolveDiffusion2D object at 0x7f60be3edf40>

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
>       assert numpy.allclose(
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
E       assert False
E        +  where False = <function allclose at 0x7f608bb301f0>(a=array([[700., 700., 700., 700., 700., 700.],\n       [700., 700., 700., 700., 700., 700.],\n       [700., 700., 700., 700., 700., 700.],\n       [700., 700., 700., 700., 700., 700.]]), b=array([[300., 300., 300., 300., 300., 300.],\n       [300., 300., 300., 300., 300., 300.],\n       [300., 300., 300., 300., 300., 300.],\n       [300., 300., 300., 300., 300., 300.]]), atol=0.001, rtol=0)
E        +    where <function allclose at 0x7f608bb301f0> = numpy.allclose
E        +    and   array([[300., 300., 300., 300., 300., 300.],\n       [300., 300., 300., 300., 300., 300.],\n       [300., 300., 300., 300., 300., 300.],\n       [300., 300., 300., 300., 300., 300.]]) = <built-in function array>([[300.0, 300.0, 300.0, 300.0, 300.0, 300.0], [300.0, 300.0, 300.0, 300.0, 300.0, 300.0], [300.0, 300.0, 300.0, 300.0, 300.0, 300.0], [300.0, 300.0, 300.0, 300.0, 300.0, 300.0]])
E        +      where <built-in function array> = numpy.array

tests/integration/test_diffusion2d.py:52: AssertionError
---------------------- Captured stdout call -----------------------
dt = 0.015625
===================== short test summary info =====================
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - assert False
=================== 1 failed, 1 passed in 0.41s ===================
```

### unittest log

Modifications similar to pytest logs.

```
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D.test_initialize_domain)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/julian/Documents/git/testing-python-exercise-wt2425/tests/unit/test_diffusion2d_functions.py", line 29, in test_initialize_domain
    self.assertAlmostEqual(self.solver.nx, 40, places=3)
AssertionError: 60 != 40 within 3 places (20 difference)

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
```

```
======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D.test_initialize_physical_parameters)
Checks function SolveDiffusion2D.initialize_physical_parameters
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/julian/Documents/git/testing-python-exercise-wt2425/tests/unit/test_diffusion2d_functions.py", line 51, in test_initialize_physical_parameters
    self.assertAlmostEqual(self.solver.dt, 0.016, places=3)
AssertionError: 0.0078125 != 0.016 within 3 places (0.0081875 difference)

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
```

```
======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D.test_set_initial_condition)
Checks function SolveDiffusion2D.set_initial_condition
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/julian/Documents/git/testing-python-exercise-wt2425/tests/unit/test_diffusion2d_functions.py", line 70, in test_set_initial_condition
    self.assertTrue(numpy.allclose(a=u,
AssertionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
```

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

```

```
