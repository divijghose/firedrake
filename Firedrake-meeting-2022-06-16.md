Date and time 2022-06-16 12:00UTC (13:00BST 22:00AEST)

# Action Items
1. **Pick Chair and Minuter** (SV to pick).
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS: Test PETSc main against current Firedrake
1. JB: Look into updating the `@parallel` test marker (ongoing)
1. DH: talk to Jemma about Firedrake 2022

# Agenda

Present: 

Apologies: JB

## DH Firedrake 2022
- No longer hosted by exeter - need to find a new location.

## SV: block optimisation in Slate
merge fix BOP https://github.com/firedrakeproject/firedrake/pull/2446

- KS: To take a look at the code. (done)
- SV: Needs to rerun performance measurements. (done)
- SV: Code is a lot nicer now thanks to Koki

New:
- Koki approves, happy to be merged once history is cleaned up.

## SV: refactoring of Schur complement builder for the Slate preconditioners
https://github.com/firedrakeproject/firedrake/pull/2455
- Looks uncontroversial, Jack to review

## RNH: CSE Minisymposium
CSE23 has opened submissions for minisymposia - the deadline is the end of August. Perhaps we might want to do a code generation symposium again? https://www.siam.org/conferences/cm/conference/cse23

- Yes!
- Coordinate with other code generation people in excalibur: Sysgenx, devito, FEniCS, Firedrake
- We have to come up with a list of talks and submit them all together
- Need 8 talks, only one can be TBD, split into 2 parts
- Alternatively could do minisymposterium (poster session)
- Start by assuming we will do minisymposium and then see who is interested
- Discuss who will take this on next time

## KS and DH: Parallel decomposition of checkpointing
- Getting there, currently dependent on a PETSc change

## DH: Disk checkpointing for Adjoint
https://github.com/firedrakeproject/firedrake/pull/2458
- Stops all calculations always being stored in memory, writes them to disc instead
  - Docs only not building because of usual cross project issues
- Adds a `_package_data` argument to the tape that allows extra information to be added to the tape (such as how to do disk checkpointing), ensures all usual tape arguments still work (clearing, copying etc)
- Package data has an abstract base class to ensure compatibility with (for example) disk checkpointing if you want to use it
- Tested in pyadjoint in serial
- Tested in firedrake in parallel (needs fix to parallel disk checkpointing, see below)
- In firedrake we update blocks:
  - use a `maybe_disk_checkpoint` call which takes information on disk (if necessary) and works out how to turn them back into firedrake `Function`s
- In firedrake checkpointing API updated with `enable_disk_checkpointing` and `checkpointable_mesh(mesh)`
- We use python's garbage manager to clean up files that we don't need any more using a `DiskCheckpointFileRef` (check spelling)
- Checkpoint copy not currently implemented but not likely used by anyone
- Contains API changes needed for "revolve style" checkpointing (i.e. with limited memory) which is DH's next job

## Merge PRs


## Date of next meetings
Next meeting: 1200 UTC [2022-06-23](./Firedrake-meeting-2022-06-23)
