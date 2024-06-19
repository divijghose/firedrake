Date and time 2024-06-19 1600 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (CW to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. JB: Move pyop3 and TSFC to firedrake and move FInAT to FIAT
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. DH: Order more Firedrake stickers
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. JB: FML + Gusto
1. JB: move tinyASM to firedrake/preconditioners: [#3604](https://github.com/firedrakeproject/firedrake/pull/3604)

# Notices
1. Firedrake User Meeting 16-18 September 2024 [Firedrake](https://www.firedrakeproject.org/firedrake_24.html) (Registration 25th August/Abstracts 18th August)

# Agenda

Present:

Apologies: NB


## JHC: I would like PETSc branch updating but it's dependent on #3546

## CW: How do we solve [this issue](https://github.com/firedrakeproject/firedrake/issues/3612)?

## JB: Ensemble is broken
And may have been for some time :flushed:

## JB: Numpy 2.0 is out
(this is in PRs below, but might be worth discussing in detail)

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

Johnson-Mercier macroelement (merge in this order)

PB: [FIAT #67](https://github.com/firedrakeproject/fiat/pull/67)

PB: [FInAT #126](https://github.com/FInAT/FInAT/pull/126)

PB: [TSFC #311](https://github.com/firedrakeproject/tsfc/pull/311)

PB: [firedrake #3548](https://github.com/firedrakeproject/firedrake/pull/3548)

Multigrid for macroelements (merge in this order)

PB: [FIAT #73](https://github.com/firedrakeproject/fiat/pull/73)

PB: [FInAT #128](https://github.com/FInAT/FInAT/pull/128)

PB: [firedrake #3615](https://github.com/firedrakeproject/firedrake/pull/3615/)

JB: [Move TinyASM](https://github.com/firedrakeproject/firedrake/pull/3604) - Do we need to notify users?

JB: [Finally numpy 2.0/Python 3.12/Cython3.0](https://github.com/firedrakeproject/firedrake/pull/3546)

JB: [Need to make UID a per comm attribute](https://github.com/firedrakeproject/firedrake/pull/3633)

DD: [Return Function/Confunction according the Riesz representation option](https://github.com/firedrakeproject/firedrake/pull/3637)

DD: [Add derivative options in pyadjoint minimize](https://github.com/dolfin-adjoint/pyadjoint/pull/151)

# Date of next meeting

1600 BST (1500 UTC) [2024-06-26](./Firedrake-meeting-2024-06-26)