**DRAFT!**

If changes are made to existing code that does not already conform to this guide, then the code should be rewritten as part of the change.

### Python code

* [PEP 8](https://peps.python.org/pep-0008/) should be followed.
* f-strings should be preferred to the older style `%` and `.format()` string formatting methods. A possible exception to this is with large multi-line strings where `.format()` may be more readable.

### Type hinting

* [Type hinting](https://docs.python.org/3/library/typing.html) should be used throughout. It is not necessary in the test suite.

### Docstrings

* [PEP 257](https://peps.python.org/pep-0257/) (docstrings) should be followed.
* Docstrings should be written in [numpydoc format](https://numpydoc.readthedocs.io/en/latest/format.html). Since type hinting is used it is not necessary to specify the type of function arguments in the docstring (unfortunately the return type still needs to be documented, [ref](https://github.com/sphinx-doc/sphinx/issues/5887)).