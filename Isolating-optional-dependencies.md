## Policy

Optional dependencies should not be included in Firedrake's global namespace and, if the dependency is  wanted by most users and hence installed by default (e.g. matplotlib), `firedrake-install` should include a flag to skip installing it.

## Details

By "global namespace" we are referring to the classes and functions imported with the command `from firedrake import *`. Optional dependencies should be kept in their own modules/subpackages and only imported with an extra import command (e.g. `from firedrake.ml import *`). Running these import commands without the appropriate packages installed should raise an `ImportError` with an error message that explains how to obtain the necessary packages.

## Motivation

Optional dependencies can often be a headache to install (e.g. pytorch, matplotlib, VTK) and users should not be forced to deal with complicated installation issues for packages that they have no intention of using.