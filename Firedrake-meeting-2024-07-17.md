Date and time 2024-07-17 1600 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (KS to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. JB: Move pyop3 and TSFC to firedrake and move FInAT to FIAT
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. DH: Order more Firedrake stickers
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. JB: FML + Gusto (This will be tackled next week at the Gusto Hackathon)

# Notices
1. Firedrake User Meeting 16-18 September 2024 [Firedrake](https://www.firedrakeproject.org/firedrake_24.html) (Registration 25th August/Abstracts 18th August)

# Agenda

Present:

Apologies:

## CC: MUMPS
Can we change the default direct solver from MUMPS to superlu_dist?

JB: Relevant issue https://github.com/firedrakeproject/firedrake/issues/3463

JB: Tangentially related, we also fail a bunch of tests when we build in "int64 mode"

https://github.com/firedrakeproject/firedrake/pull/3683

https://github.com/firedrakeproject/firedrake/issues/3690


## PB + RK: GLL ordering
We might want to change the default GLL(simplex) DOF ordering/entity_ids that ensure that DOFs on the closure of an edge are aligned with the GLL quadrature. 

https://github.com/firedrakeproject/fiat/pull/75/files 

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

- ~JB: Bug fix for TinyASM when PETSc is compiled with 64-bit indices [#3665](https://github.com/firedrakeproject/firedrake/pull/3665)~

- PB: [FIAT #77](https://github.com/firedrakeproject/fiat/pull/77)

- PB: [FInAT #131](https://github.com/FInAT/FInAT/pull/131)

# Date of next meeting

1600 BST (1500 UTC) [2024-07-24](./Firedrake-meeting-2024-07-24)