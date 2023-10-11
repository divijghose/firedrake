Date and time 2023-10-11 16:00 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (NB to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Move pyop3 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. DH: Revisit [PR#2484](https://github.com/firedrakeproject/firedrake/pull/2484).
1. JB: Scheduled GitHub actions to avoid inactivity timeout for website repo ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2023-09-20#jb-scheduled-gh-actions-time-out-after-something-like-60-days-of-inactivity))
1. DH: Order more Firedrake stickers
1. ALL/ANY: Drop libsupermesh ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2023-09-27#cwjb-libsupermesh-needs-updating))?


# Minutes

Present: JB, CW, DD, KS, DH, NB, PB, RNH, UZ, IM, RK

Apologies:

## MacOS Installation issues
There is an open issue with Clang 15 where you must use `ldclassic` flags to restore old behaviour.

It is unclear (right now) whether rolling back to Clang 14 might fix this.

## MacOS Build hardware
Our Mac build hardware is currently not usable, mainly due restrictive Imperial ICT policies.

## NetGEN
- Stable NetGEN doesn't have features that Firedrake needs.
- Need to use nightly.
- Nightly isn't stable.
- Umberto has created a fork.
- Building from scratch takes too long!
- Umberto is now setting up CI on this for to build a wheel from source.

DH: This is a reasonable short term solution, but we don't want to have to build this wheel forever.
This needs to go into netGEN stable.

JB: Action item UZ mark netGEN tests as xfail (urgently).

## Firedrake Wheels
DH: JB is working on developing "fat" wheels for installing PETSc and ultimately Firedrake.

Machine learning want a wheel, but they need to take a long look at how you currently install pytorch and tensor flow before criticising Firedrake.

## Things for Jack to do:
Action item JB: Update Github PR template.

## RNH: What's happening with libsupermesh
JB: We can keep it around if we get our rtree PR in.
DH: However, its days are numbered if it starts holding up progress on a Firedrake wheel.
Also it doesn't work 100% in parallel. VOM does work in parallel (although is not conservative).

## Merge PRs
- RNH: [Test (and fix!) cross mesh interpolation annotation #3145](https://github.com/firedrakeproject/firedrake/pull/3145) Merged.
- JB: [#3041](https://github.com/firedrakeproject/firedrake/pull/3041) FML is ready. Changes requested.
- CW: [#3141](https://github.com/firedrakeproject/firedrake/pull/3141) Merged.
- CW: [#3135](https://github.com/firedrakeproject/firedrake/pull/3135) Merged.
- KS: [#3139](https://github.com/firedrakeproject/firedrake/pull/3139) Merged.
- PB: [#3114](https://github.com/firedrakeproject/firedrake/pull/3114) Closed.
- KS: [#3049](https://github.com/firedrakeproject/firedrake/pull/3049) Rebase required.

# Date of next meeting

1600 BST (1500 UTC) [2023-10-18](./Firedrake-meeting-2023-10-18)
