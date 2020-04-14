On macOS using homebrew python, the symlinks in the firedrake venv can be broken when homebrew updates python.

Should this happen you can fix your venv by

1. With the firedrake venv deactivated run `pip3 install --upgrade virtualenv`
2. Navigate to the firedrake venv root (the firedrake install directory) then run `virtualenv .` to recreate the virtual environment with unbroken symlinks.