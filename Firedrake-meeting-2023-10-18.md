Date and time 2023-10-18 16:00 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (JB to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Move pyop3 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. DH: Revisit [PR#2484](https://github.com/firedrakeproject/firedrake/pull/2484).
1. JB: Scheduled GitHub actions to avoid inactivity timeout for website repo ~~([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2023-09-20#jb-scheduled-gh-actions-time-out-after-something-like-60-days-of-inactivity))~~ (See Merge PRs)
1. DH: Order more Firedrake stickers
1. ALL/ANY: Drop libsupermesh ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2023-09-27#cwjb-libsupermesh-needs-updating))?
1. UZ: Mark netGEN tests as xfail (not required any more)
1. JB: Update Github PR template (done)


# Agenda

Present:

Apologies:

## MacOS Installation issues (UPDATE)
JB: I still don't like the MacOS platform
- Apparently can't downgrade CLT to 14.3.1 on latest MacOS Samoa. (I can't find official link, haven't actually tried, been working on a fix).
- MPICH built by PETSc with CLT 15 is broken, it requires additional LDFLAGS (`-Wl,-ld_classic`) to configure. (PETSc need to fix this)
- Firedrake install script is in a bit of a state, don't fix by setting `export PETSC_CONFIGURE_OPTIONS=--LDFLAGS=-Wl,-ld_classic` that will break your BLAS configuration.
- Potential fix, but needs more extensive testing: [PR3171](https://github.com/firedrakeproject/firedrake/pull/3171).

## FML
JB: Documentation needs some policy decisions [#3041](https://github.com/firedrakeproject/firedrake/pull/3041).


## Thoughts on [#3167](https://github.com/firedrakeproject/firedrake/pull/3167)
RNH: Also, why does `Cofunction` not have a `.zero` method?

## Merge PRs
- JB: [#3153](https://github.com/firedrakeproject/firedrake/pull/3153) Github PR template.
- JB: [#3165](https://github.com/firedrakeproject/firedrake/pull/3165)
- JB: [#1](https://github.com/firedrakeproject/firedrakeproject.github.io/pull/1) Do we need protection on this repo?
- UZ: [#3176](https://github.com/firedrakeproject/firedrake/pull/3176) Netgen circular import


# Date of next meeting

1600 BST (1500 UTC) [2023-10-25](./Firedrake-meeting-2023-10-25)
