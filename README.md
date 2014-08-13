pytest-autoscenarios
====================

Requirements
============
A recent version of pytest is required (>= 2.3.4).

Quick start
===========
1. ``pip install pytest-autoscenarios``
2. Execute a test with different parameters by adding the params in docstring

Example
-------

```
  def test_foo(self, input_data, expected):
    """ scenarios:
    [10, 20]
    ["xyz", "xyzxyz"]
    [[1, 2, 3], [1, 2, 3, 1, 2, 3]]
    """
    assert input_data * 2 == expected
```

... in terminal:

```
  collected 3 items 

  test.py::TestScenario::test_foo[10-20] PASSED
  test.py::TestScenario::test_foo[input_data1-expected1] PASSED
  test.py::TestScenario::test_foo[input_data2-expected2] PASSED

```

... or use the @autoscenarios decorator:

```
  @autoscenarios
  class TestScenario():

    def foo(self, test_input, expected):
        """ scenarios:
        [10, 20]
        ["xyz", "xyzxyz"]
        [[1, 2, 3], [1, 2, 3, 1, 2, 3]]
        """
        assert test_input * 2 == expected
```

```
  collected 3 items 

  doctests.py::TestScenario::test_foo_2 PASSED
  doctests.py::TestScenario::test_foo_0 PASSED
  doctests.py::TestScenario::test_foo_1 PASSED
```

