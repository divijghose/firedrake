Date and time 2024-08-07 1600 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (DD to pick)
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

# Minutes

Present: DH, RK, PB, KS, JB, CC, JM

Apologies: DD (pick NB as a minuter)

## Firedrake 24
DH: Submit abstracts please! Before the end of next week (no extensions)

## DD: [#PR143](https://github.com/dolfin-adjoint/pyadjoint/pull/143) (pyadjoint) + [#PR3657](https://github.com/firedrakeproject/firedrake/pull/3657) (firedrake): TAO solver
Note: James is planning to attend this meeting.

JM: TAO based solver for the adjoint for a range of problems (not equality and inequality constraints).

- [#PR143](https://github.com/dolfin-adjoint/pyadjoint/pull/143): Concerns about deadlock on object finalization. Other changes requested, see reviewer comments on PR.
- [#PR3657](https://github.com/firedrakeproject/firedrake/pull/3657): Merged independently (since these methods won't be called by anyone). Connor's review needs addressing, but then it was decided that it shouldn't block this as it can be reverted later if needs be.

## JB: Caching is a bit broken
### (Disk) Caches are broken in serial
Consider the following:
```python
from firedrake import *

# Example 1:
mesh = UnitSquareMesh(10, 10, comm=COMM_WORLD)
V = FunctionSpace(mesh, "Lagrange", 1)
f = Function(V)
x, y = SpatialCoordinate(mesh)

for _ in range(5):
    f.interpolate(sin(1 + 2*pi*x)*cos(1 + 2*pi*y))
```

Run twice in a row this code does not hit disk cache, as it should :slightly_frowning_face:. Hashing of `FiniteElement` in FInAT needs to be fixed so that it is consistent between invocations.

### (Memory/Disk) Caches are broken in parallel
Consider the following:
```python
from firedrake import *

# Example 2:
# Run on more than 1 rank
from mpi4py import MPI
from pprint import pprint
from pyop2.mpi import hash_comm

ids = set()

def make_a_function(comm):
    mesh = UnitSquareMesh(10, 10, comm=comm)
    ids.add(hash_comm(mesh._comm))
    print(f'CW{COMM_WORLD.rank}: {len(ids) = }')
    V = FunctionSpace(mesh, "Lagrange", 1)
    f = Function(V)
    x, y = SpatialCoordinate(mesh)
    return f.interpolate(sin(1 + 2*pi*x)*cos(1 + 2*pi*y))


for iteration in range(1, 10):
    print(f'CW{COMM_WORLD.rank}: {iteration = }')
    color = 0 if COMM_WORLD.rank < 2 else MPI.UNDEFINED
    comm12 = COMM_WORLD.Split(color=color)
    if COMM_WORLD.rank < 2:
        f = make_a_function(comm12)
        comm12.Free()

    color = 0 if COMM_WORLD.rank > 0 else MPI.UNDEFINED
    comm23 = COMM_WORLD.Split(color=color)
    if COMM_WORLD.rank > 0:
        f = make_a_function(comm23)
        comm23.Free()
```

Run across 3 MPI ranks, `COMM_WORLD.rank == 1` will hit memory cache, but `COMM_WORLD.rank == 2` will not. This will produce a deadlock. We need to have per communicator memory caches, not global ones.

### Hashing comms (in PyOP2) is not safe
Currently just `id(comm)` is used instead of a hash, this is fine if you never free communicators, but then you exhaust the comm count limit. If you free the communicators `id(comm)` can return the same value as a previous comm and you have a hash collision. It remains to be seen whether per comm caches is sufficient to remove the need to have comm hashes in the first place.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*Date and time 2024-08-07 1600 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (DD to pick)
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

Present: DH, RK, PB, KS, JB, CC, JM

Apologies: DD (pick NB as a minuter)

## Firedrake 24
DH: Submit abstracts please! Before the end of next week (no extensions)

## DD: [#PR143](https://github.com/dolfin-adjoint/pyadjoint/pull/143) (pyadjoint) + [#PR3657](https://github.com/firedrakeproject/firedrake/pull/3657) (firedrake): TAO solver
Note: James is planning to attend this meeting.

JM: TAO based solver for the adjoint for a range of problems (not equality and inequality constraints).

- [#PR143](https://github.com/dolfin-adjoint/pyadjoint/pull/143): Concerns about deadlock on object finalization. Other changes requested, see reviewer comments on PR.
- [#PR3657](https://github.com/firedrakeproject/firedrake/pull/3657): Merged independently (since these methods won't be called by anyone). Connor's review needs addressing, but then it was decided that it shouldn't block this as it can be reverted later if needs be.

## JB: Caching is a bit broken
### (Disk) Caches are broken in serial
Consider the following:
```python
from firedrake import *

# Example 1:
mesh = UnitSquareMesh(10, 10, comm=COMM_WORLD)
V = FunctionSpace(mesh, "Lagrange", 1)
f = Function(V)
x, y = SpatialCoordinate(mesh)

for _ in range(5):
    f.interpolate(sin(1 + 2*pi*x)*cos(1 + 2*pi*y))
```

Run twice in a row this code does not hit disk cache, as it should :slightly_frowning_face:. Hashing of `FiniteElement` in FInAT needs to be fixed so that it is consistent between invocations.

### (Memory/Disk) Caches are broken in parallel
Consider the following:
```python
from firedrake import *

# Example 2:
# Run on more than 1 rank
from mpi4py import MPI
from pprint import pprint
from pyop2.mpi import hash_comm

ids = set()

def make_a_function(comm):
    mesh = UnitSquareMesh(10, 10, comm=comm)
    ids.add(hash_comm(mesh._comm))
    print(f'CW{COMM_WORLD.rank}: {len(ids) = }')
    V = FunctionSpace(mesh, "Lagrange", 1)
    f = Function(V)
    x, y = SpatialCoordinate(mesh)
    return f.interpolate(sin(1 + 2*pi*x)*cos(1 + 2*pi*y))


for iteration in range(1, 10):
    print(f'CW{COMM_WORLD.rank}: {iteration = }')
    color = 0 if COMM_WORLD.rank < 2 else MPI.UNDEFINED
    comm12 = COMM_WORLD.Split(color=color)
    if COMM_WORLD.rank < 2:
        f = make_a_function(comm12)
        comm12.Free()

    color = 0 if COMM_WORLD.rank > 0 else MPI.UNDEFINED
    comm23 = COMM_WORLD.Split(color=color)
    if COMM_WORLD.rank > 0:
        f = make_a_function(comm23)
        comm23.Free()
```

Run across 3 MPI ranks, `COMM_WORLD.rank == 1` will hit memory cache, but `COMM_WORLD.rank == 2` will not. This will produce a deadlock. We need to have per communicator memory caches, not global ones.

### Hashing comms (in PyOP2) is not safe
Currently just `id(comm)` is used instead of a hash, this is fine if you never free communicators, but then you exhaust the comm count limit. If you free the communicators `id(comm)` can return the same value as a previous comm and you have a hash collision. It remains to be seen whether per comm caches is sufficient to remove the need to have comm hashes in the first place.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

KS: [zany](https://github.com/firedrakeproject/firedrake/pull/3726): Merged

KS: [part1](https://github.com/firedrakeproject/firedrake/pull/3727): Deferred

# Date of next meeting
1600 BST (1500 UTC) [2024-08-21](./Firedrake-meeting-2024-08-21)


KS: [zany](https://github.com/firedrakeproject/firedrake/pull/3726): Merged

KS: [part1](https://github.com/firedrakeproject/firedrake/pull/3727): Deferred

# Date of next meeting
1600 BST (1500 UTC) [2024-08-21](./Firedrake-meeting-2024-08-21)
