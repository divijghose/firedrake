## Installation
#### Either
Install with the [script](https://github.com/firedrakeproject/firedrake/blob/tsfc2loopy/scripts/firedrake-install) in the `tsfc2loopy` branch of firedrake with the arguments
```
--package-branch firedrake tsfc2loopy --package-branch tsfc tsfc2loopy --package-branch PyOP2 siam-vec --package-branch loopy cvec
```
#### Or
- Start from a normal firedrake installation
- Check out the branches:
    - firedrake: tsfc2loopy
    - tsfc: tsfc2loopy
    - PyOP2: siam-vec
- `git clone https://github.com/firedrakeproject/loopy --recursive`
- Install loopy with e.g. `pip install -e loopy/`
- Check out loopy branch cvec

## Note
To reduce the complexity and chances of surprises, I've cut corners in a few places:
- Vectorization is off by default, this means on these branches, we are just running as if on the pull request #1186. Turn on vectorization manually by setting PyOP2 parameters:
```
from firedrake import parameters
parameters['pyop2_options']['simd_width'] = 4
```
- OpenMP backend is removed, i.e. vectorization is only through vector extensions and no OpenMP pragmas.
- Reminder loop generation needs more work with vector extensions, so that is removed for now. This means the demo will only work if the number of elements is multiple of batch size.
- Vectorization is switched off for matrix assembly.

