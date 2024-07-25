# Docstring and type hinting policy

Following the [meeting on 2023-10-18](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2023-10-18) it was decided that Firedrake needs stricter policies for the style and layout of all future docstrings and documentation.
Read **new code** as any code not on the master branch of Firedrake as of October 2023 and read **updated code** as code that existed on the master branch of Firedrake before October 2023, but has been modified in a pull request under review from (the 25th) October 2023:

- All new code must follow [PEP8](https://peps.python.org/pep-0008/#documentation-strings) and [PEP257](https://peps.python.org/pep-0257/) conventions (where PEP257 doesn't conflict with numpydoc).
    + This includes the use of [imperative mood](https://en.wikipedia.org/wiki/Imperative_mood).
    + Existing code _should_ follow these conventions already, but there are certainly exceptions.
- All new code must use [Python type hinting](https://docs.python.org/3/library/typing.html).
    + ~Python type hints should be imported from `typing` and not from `collections.abc`. Eg: Use `typing.Callable` not `collections.abc.Callable`. This aims to maintain compatibility with Python 3.8 for as long as possible within its remaining lifetime.~ Python type hints should be imported from `collections.abc` and not `typing`. (Support for Python 3.8 was dropped in 2024)
    + Type hints are not compulsory for new code in the install script.
    + Type hints are not compulsory for new code in the test suite.
- All new code must use [numpy style docstrings](https://numpydoc.readthedocs.io/en/latest/format.html).
    + **It is not necessary to include argument types in the docstring, these should be automatically detected from the function signature.**
- Any pull request with updated code that edits the docstrings (at least for public interfaces), or any other documentation, must have the webpage build artefacts viewed and reviewed before merging (as part of the existing code review process).
- Any pull request with updated code that edits existing docstrings or function calls must update the corresponding code to follow this new policy.