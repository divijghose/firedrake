Date and time 2024-09-11 1600 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (CW to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. JB: Move pyop3 and TSFC to firedrake and move FInAT to FIAT
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))

# Notices
1. Firedrake User Meeting 16-18 September 2024 [Firedrake](https://www.firedrakeproject.org/firedrake_24.html) (Registration 25th August/Abstracts 18th August)

# Minutes

Present: DH, KS, DD (minuter), JB, NB.

Apologies: CW, PB

## NB: Add JAX support

[#3759](https://github.com/firedrakeproject/firedrake/pull/3759): Add support to couple Firedrake and JAX systems in a differentiable manner using external operators and a similar JAX concept.
It is closed to be merged but requires docs fixings.

## JM: Tao optimisation solver: [PR 143](https://github.com/dolfin-adjoint/pyadjoint/pull/143)

It requires discussion (maybe in the firedrake meeting) of the `attach_destroy_finalizer` function. 

## KS: hex interior facet integration : https://github.com/firedrakeproject/firedrake/pull/3755

Associated [PR fiat 83](https://github.com/firedrakeproject/fiat/pull/83): It requires revision. Perhaps a base class may lead to an easier-to-understand code. In addition, improve the docstring.

Associated [PR tsfc 317](https://github.com/firedrakeproject/tsfc/pull/317): Request changes.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

PB: [firedrake #3757](https://github.com/firedrakeproject/firedrake/pull/3757)

Approved!

PB: [firedrake #3762](https://github.com/firedrakeproject/firedrake/pull/3762)

Approved!

JB: [3758](https://github.com/firedrakeproject/firedrake/pull/3758)

It is going to be approved.

JB: [3707](https://github.com/firedrakeproject/firedrake/pull/3707)

Approved!

# Date of next meeting
1600 BST (1500 UTC) [2024-09-18](./Firedrake-meeting-2024-09-18)