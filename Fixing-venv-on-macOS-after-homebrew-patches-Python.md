On macOS using homebrew python, the symlinks in the firedrake venv can be broken when homebrew updates python with a patch version (e.g. 3.7.7 -> 3.7.8).

Should this happen you can fix your venv by

1. With the firedrake venv deactivated run `pip3 install --upgrade virtualenv`
2. Navigate to the firedrake venv root (the firedrake install directory) then run `virtualenv .` to recreate the virtual environment with unbroken symlinks.

**Note that this is unlikely to work for minor release changes (e.g. 3.7.x -> 3.8.x).**