Date and time 2021-07-21 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. (JB, DH, KS, JW): Firedrake training happening 23rd August, update
1. DH: Firedrake 2021 update

# Minutes

Present:

Apologies:

## Firedrake training
- 50 were registered people on Monday
- DH: by next week double-check Jupiter server is running

## Firedrake 2021
- website is up
- announcements to mailing list, Slack, fenics-slack, NA digest, SIAM CSE mailing list
- registration is not up yet (bureaucracy)
- abstract submission is open

## RNH: Issue [#2095](https://github.com/firedrakeproject/firedrake/issues/2095) Loopy breaking Interpolation Kernels
Complex data types are getting into real mode PyOP2 Kernels (can't create a "Real" interpolator for example).
- issue removing complex node in expression compiler seems to insufficient (in form compiler it is at least called twice, see https://github.com/firedrakeproject/tsfc/blob/94aa4d548bd1cc5520a8490692e12f190287ea86/tsfc/ufl_utils.py#L119 I think)

## CW: What is the data representation of a `MixedDat`?

From [this issue](https://github.com/OP2/PyOP2/issues/626) it is suggested that the data part of a `MixedDat` is just the concatenation of several `Dats`. So a `MixedDat` containing 3 `Dats` of length `n` and `dim=3` would have shape `(3, n, 3)`. How does this work if the `Dats` have different `dims`?

- moved to next week, needs a Lawrence!

## CW: Proposal: A new type system for PyOP2

I am currently trying to introduce a strict divide between the code generation and parloop execution stages in PyOP2. In order to do the code generation we need to know certain bits of information about the data we are operating on such as: `dtype`, `dim` (its local shape), map `arity`, and access descriptor; but we don't want to tie ourselves to the actual data structures.

The suggestion is that these properties can be considered 'type' information for the `Dat`/`Map`/`Global` etc. We could canonicalise this by declaring these attributes as explicit types. E.g. `ScalarDatFloat64` or `Global3Int32` (names to be bike-shedded). Code generation could then happen by only passing in the relevant `type(dat)` instead of storing this information in some sort of namedtuple/dataclass.

There are some outstanding questions about this:

- What do we do about 'type' information that is more varied (e.g. map `offset`)?
- What about mixed?

- DH parloops only exist in connection to data -> Problems: memory leaks and circular reference hell
- extrusion and offsets are an issue

- moved to next week, needs a Lawrence!

## RNH - Workers dying when running tests
See for example https://github.com/firedrakeproject/firedrake/runs/3181344420. Can code mistakes cause this to happen or is it a hardware problem?

- probably caused by segfaulting
- JB maybe debug with pytest -s so stdout is dumbed
- DH job handler is parallel so might cause issues, and also probably slows down the performance at which the tests run by a lot, or try run in docker
- test fail causes the worker to crash, but pytest detects it
- check if tests use MUMPS

## RNH - FInAT dual evaluation feedback
See 
 - https://github.com/firedrakeproject/firedrake/pull/2115
 - https://github.com/firedrakeproject/tsfc/pull/250
 - https://github.com/FInAT/FInAT/pull/89

Possible regression due to multiplying by a bunch of zeros for stuff like high-order tets.
Profiling suggestions welcome.

- RNH: People take a look, it's almost there.
- RNH: Some caveat with EnrichedElements, no sparse representation in GEM

## Merge PRs:

## AOB

## Date of next meeting
[2021-08-04](./Firedrake-meeting-2021-08-04) 15:00UTC (16:00BST)
