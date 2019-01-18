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
- 