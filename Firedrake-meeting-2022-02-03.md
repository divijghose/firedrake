Date and time 2022-02-03 16:00UTC (16:00GMT)

# Action Items
1. **Pick Chair and Minuter** (JB to pick).
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. DH: Contact Jemma about hosting Firedrake workshop
    
    Jemma enthusiastic at possibility of hosting Firedrake workshop in Exeter.

# Agenda

Present: CW (minuter), KS, JB, LM, DH, RK, SV, DRS, PK, CC

Apologies: 

### DH: GH discussions are now up

### JB: Update for Python3.10 #2311
It's ready to go, pending an M1 wheel

DH: Is planning to purchase some Mac hardware so we can do build testing for PRs.

### DH: Should we support $XDG_CACHE_DIR?

LM: We could try and get loopy to point to our own cache directory.

LM: Using `$XDG_` could put stuff in HPC home directory.

DH: Firedrake, PyOP2, TSFC, loopy should all have API calls that will set their cache directory and this should cascade. We should *only* honour `FIREDRAKE_CACHE_DIR`.

### JB: Validating PETSc installs with `--honour-petsc-dir`

LM/DH: `firedrake-install` should complain if pre-built PETSc does not have the required bits.

DRS: If passing `--honour-petsc-dir` emit a warning straight away that it must be built with the necessary options.

## Merge PRs:

Lots!

- https://github.com/firedrakeproject/firedrake/pull/2309
- https://github.com/firedrakeproject/fiat/pull/26
- https://github.com/FInAT/FInAT/pull/100
- https://github.com/firedrakeproject/tsfc/pull/265

## AOB

## Date of next meeting

1600 UTC (1600 GMT) [2022-02-10](./Firedrake-meeting-2022-02-10/)
