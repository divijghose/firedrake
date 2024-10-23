Date and time 2024-10-23 1600 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (CW to pick)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. JB: Move pyop3 and TSFC to firedrake and move FInAT to FIAT
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PRs: [Voting algorithm](https://github.com/firedrakeproject/firedrake/pull/3293), [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. DH: Finish UFL element.value_shape() update
1. ANY: Add Python 3.13 to PyOP2, TSFC, FIAT, FInAT CI (and others?)
1. JB/UZ: ngsPETSc releases ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-16))

# Agenda

Present: DH, CW, KS, JB, IM, FA, RK, DD, JHC, LC, Y

Apologies: PB

## Merge queues

Low priority for now.

## Voting algorithm

Connor has a WIP solution for this, so will take this on.

## RK: Firedrake USA 2025.

SIAM has funding call deadline next week: $2k ish hopefully. They may expect the meeting to be at a university.

- Finding a venue: in/near Fort Worth, or in Wako?
- Fort Worth: + Easier for people to get to. - Harder logistics. - SIAM may not want to fund something this close?
- Wako: + Easier to organise, RK has contacts. - Harder to get to from Dallas airport. Airport transport can be expensive.

- DH: likely to be fewer UK/Europe attendees than usual, but we want to encourage US attendees. Which is easier location from the US?
- RK: Wako is on the way to Fort Worth, but only for driving. But Washington, LLNL, etc won't be driving. Can we ask on Slack General what people would prefer?

RK: We can organise a group shuttle to get everyone to Fort Worth after Firedrake Meeting.

Ideas for Sunday group activities? Dinosaur footprint valley?

FA: Finite element rodeo is a week before Firedrake & CSE.

## DD: [PR #3723](https://github.com/firedrakeproject/firedrake/pull/3723)

Adjoint Variational Solver and fix recomputing tape when Jacobian is constant.

- DH: Why does memory increase at end of NS example? DD: Will rerun with more time to see if it stabilises.

- Linear wave example: why does memory match? Isn't master version creating a new solver every time? Why doesn't this overhead show up? DD: I will investigate this.


## JB: Long running tests
```
427.50s call     tests/demos/test_demos_run.py::test_demo_runs[full_waveform_inversion.py.rst]
363.02s call     tests/macro/test_macro_interp_project.py::test_piola_convergence[h1_proj-3-Johnson-Mercier-1-1]
345.51s call     tests/regression/test_fdm.py::test_p_independence_hcurl[Box]
```
CI time has shot up as a result.

- DD: It may be possible to simplify FWI demo.
- DH: FWI: inverse problems are inherently large, but what do we want the tests to do? Can we have simpler/smaller parameters when the tests are run.

- RK: Piola convergence is running 2D and 3D convergence tests. Do we need to test these rigorously? But meshes are small, so we need to see why it is taking so long.
- DH: This needs to be on the agenda until PB is at the meeting so we can discuss.

## JB: Move PyOP2 and TSFC to firedrake and move FInAT to FIAT
This is now happening, beware PB we need to pause merges on FIAT/FInAT for a bit.

- JB: FInAT/TSFC: we need a pause on adding elements while we merge them.
- DH: FInAT/TSFC: just merge it

- JB: PyOP2 has successfully been merged!

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

PB: [#3814](https://github.com/firedrakeproject/firedrake/pull/3814) MG for R space. Will deal with this when we have more time.

DD: [#3816](https://github.com/firedrakeproject/firedrake/pull/3816) Fix gradient computation where the boundary condition is a control parameter. Approved and merged.

# Date of next meeting
1600 BST (1500 UTC) [2024-10-30](./Firedrake-meeting-2024-10-30)