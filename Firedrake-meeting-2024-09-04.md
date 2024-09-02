Date and time 2024-09-04 1600 BST (1500 UTC)

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

# Notices
1. Firedrake User Meeting 16-18 September 2024 [Firedrake](https://www.firedrakeproject.org/firedrake_24.html) (Registration 25th August/Abstracts 18th August)

# Agenda

Present:

Apologies: JB

## JB: Stuff
JB is away this week and probably won't make the meeting, but there are several things up in the air:
- I have a bunch of small PRs open that should probably just be merges (see Merge PRs).
- I think the FInAT hash stuff is ready, I have written a test, I don't think coverage of more elements is necessary.
- The caching changes that are causing deadlock need another look. This is much closer to being merged, this needs:
  + Another look over the [PyOP2 changes](https://github.com/OP2/PyOP2/pull/724)/review.
  + Comments/feedback on `PYOP2_SPMD_STRICT` mode (not switched on by default, but I've already found it exceedingly useful).
  + Feedback/review on the corresponding [Firedrake changes](https://github.com/firedrakeproject/firedrake/pull/3730), specifically I'd like some group thought/wisdom about the hashing functions that are used (ensuring that they are unique, I don't necessarily know all the details of the arguments).
- I have had [this PR](https://github.com/firedrakeproject/firedrake/pull/3385) open for a log time as a bit of a pet project, but find myself needing it more and more. The idea is to allow running the full test suite on systems that do not allow a recursive MPI init call (Side note: there is an officially blessed MPI way of doing this, see: https://github.com/JDBetteridge/mpispawn for a proof of concept solution). This Firedrake branch now contains a bunch of test fixes that ought to be moved back to master. What I want to know is:
  + Can we switch to "MPI on the outside" test execution? Or will I have to keep maintaining this branch to test on HPC and other pedantic systems?
  + Additionally, does someone want to fix, or at least tell me how to fix `tests/output/test_adjoint_disk_checkpointing.py::test_disk_checkpointing`? I have had to mark the test broken in this PR. The test pollutes the tape and only passes on master because each parallel test is run in isolation! Also, I don't think `pytest-mpi` propagates markers like `xfail`.

Can whoever minutes also make it very clear what the outcomes of the discussions are so that I can pick this up next week when I'm back.


## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*
JB: [FIAT #81](https://github.com/firedrakeproject/fiat/pull/81) Use some relevant versions of Python for CI and fix missing `pkg_resources`.

JB: [FInAT #136](https://github.com/FInAT/FInAT/pull/136) Requires the above to pass tests, this can be re-run "live" the tests take <1min.

JB: [FInAT #134](https://github.com/FInAT/FInAT/pull/134) Update FInAT UFL element hashes so they are persistent across invocations (so expressions can be retrieved from disk cache). There is [proof](https://github.com/firedrakeproject/firedrake/pull/3729) that Firedrake works with these changes.



# Date of next meeting
1600 BST (1500 UTC) [2024-09-13](./Firedrake-meeting-2024-09-13)
