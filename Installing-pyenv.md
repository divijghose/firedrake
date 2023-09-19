## Why

It can be helpful to install Firedrake using a Python executable installed with [pyenv](https://github.com/pyenv/pyenv/) rather than a system provided version. This is because:
- When the system Python bumps a minor version (e.g. 3.10 -> 3.11) the Firedrake virtual environment will still work.
- MacOS ships with a broken Python installation and the homebrew version also does not always work.

## How

To install pyenv (assuming MacOS with homebrew installed) one needs to:
1. Install [build dependencies](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)
1. Install pyenv
    ```
    brew install pyenv
    ```
1. Set `PYENV_ROOT` and `PATH`
    ```
    $ export PYENV_ROOT=$HOME/.pyenv
    $ export PATH=$PYENV_ROOT/bin:$PATH
    ```
1. Initialise the shell
    ```
    $ eval "$(pyenv init -)"
    ```
    Note that this command is optional. One can instead find the installed Python versions under `$(pyenv root)/versions`. See [here](https://github.com/pyenv/pyenv/#advanced-configuration) for more information.
1. Install a Python version (here 3.10)
    ```
    $ pyenv install 3.10
    ```
1. Set this Python as the default for this shell (only if using `pyenv init`)
    ```
    $ pyenv shell 3.10
    ```
1. Run `firedrake-install`, `python` will resolve to the correct executable
    ```
    $ python firedrake-install <args>
    ```

Note that the above instructions are equivalent to those found [here](https://github.com/pyenv/pyenv/#set-up-your-shell-environment-for-pyenv).