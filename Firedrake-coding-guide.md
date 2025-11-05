## Coding style

* [PEP 8](https://peps.python.org/pep-0008/) should be followed.
* f-strings should be preferred to the older style `%` and `.format()` string formatting methods. A possible exception to this is with large multi-line strings where `.format()` may be more readable.
* Excessively long functions (50 lines+) should ideally be broken apart into more readable pieces.
* `*` imports should be avoided inside the `__init__.py` files inside Firedrake. This is so that we have explicit control over what goes into the `firedrake` namespace.

### Type hinting

* [Type hinting](https://docs.python.org/3/library/typing.html) should be used throughout. It is not necessary in the test suite.

#### Type hinting tips + tricks

* To avoid issues with forward references (until Python 3.14) you should add the line `from __future__ import annotations` to the top of the file.
* To avoid issues with circular imports you should do
```py
if typing.TYPE_CHECKING:
    from firedrake import Function  # assuming that this is a circular dependency
```

### Docstrings

* [PEP 257](https://peps.python.org/pep-0257/) (docstrings) should be followed.
* Docstrings should be written in [numpydoc format](https://numpydoc.readthedocs.io/en/latest/format.html). Since type hinting is used it is not necessary to specify the type of function arguments in the docstring (unfortunately the return type still needs to be documented, [ref](https://github.com/sphinx-doc/sphinx/issues/5887)). Occasionally it is fine to have a different type description in the numpydoc if it would otherwise expose a complicated internal detail (e.g. `WithGeometry` vs `FunctionSpace`).

### Existing code

If changes are made to existing code that does not already conform to this guide, then the code should be rewritten to be conforming as part of the change.

## Other policies

* Untaped parts of the interface should raise an exception if taping is enabled ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2025-09-24#lc-annotation-inside-pointevaluator))