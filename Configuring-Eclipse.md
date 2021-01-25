Assuming Eclipse with PyDev and Firedrake are installed, the IDE can be configured as follows:
 1. Start Eclipse from within a Firedrake terminal
     * `source firedrake/bin/activate`
     * `eclipse`
 2. Point the Interpreter to Firedrake Python
     * `Eclipse/Window/Preferences/PyDev/Interpreters/Python Interpreters/` Browse for python/pypy exe
     * Chose Python in `/firedrake/bin/`
 3. Remove the PyDev project Configuration
     * In the Package Explorer right click on the project and select `/PyDev/Remove PyDef Project Config`
 4. Reload the Python Script

From my limited understanding Eclipse does always have to be started from within the Firedrake terminal.

Thanks to BitByte_Bake on stackexchange who found the solution here https://stackoverflow.com/a/29351006.
