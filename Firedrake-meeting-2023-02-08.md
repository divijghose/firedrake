Date and time 2023-02-08 16:00UTC

# Action Items
1. **Pick Chair and Minuter** (RNH to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: A Firedrake manual
1. JB: Move PyOP2 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
1. KS: Fix checkpointing error with pickling elements

# Agenda

Present: CW (minuter), RK, KS, DH, JB, IM, DS, RNH, PB, NB, FA, PF

Apologies:

## 1. RCK: Let's discuss the possibility of "extraction operators" in PyOP2/3 as a pathway to get more elements/simplify zany elements?

- RK: Previously assumed a 1-to-1 relationship assumed between global and local basis functions. Makes zany, splines and other bits hard/impossible. This is solved by extraction operators. "Global basis supported on cell i - how do I represent this in a local basis?". Can be encoded as a sparse matrix.
- DH: Would call this "packing" and "unpacking" operators. Need to be careful about data movement.
- DH: Some complex cases of this include Serendipity or H-curl with 2 DoFs per face (can't be represented by permutations).
- DH: This is a property of a function space. Could be computed eagerly or lazily.
- DH: We assume that the element kernel operates in reference/canonical orientation. This means that zany/complex transformations would be happening outside of the element kernel.
- DH: We are effectively proposing a system where for some elements the kernel does not lower to reference space (instead local space). Moves the pullback operation (and possibly other transformations) into the "pack", "unpack" space.
- RK: Need to attach extraction operator to the function space not the finite element as some information belongs to the mesh.

## JB: CI Memory issue
[Often](https://github.com/firedrakeproject/firedrake/actions/runs/4116758225/jobs/7107208525) CI is failing with:
```
Error: Process completed with exit code 137.
```

- DH: Processes never return memory to the OS so tests consume a huge amount of memory by the end. Current plan is to `mpiexec` every single test. This guarantees that tests do not pollute the existing environment.

## JB: [Firedrake Manual](https://github.com/firedrakeproject/firedrake/pull/2633)
Action on everybody to take the time to check your details are up to date. Whilst you're at it please flick through the manual to check for errors. :slightly_smiling_face:

#### JB: Update Funding on website
> This is out of date. We should update the website so the manual contains correct info before it is released.

I have made a start on this

Is there anything else out of date on the website that needs updating? (Feel free to add to this agenda item)

## Merge PRs

PF: [https://github.com/firedrakeproject/firedrake/pull/2756](https://github.com/firedrakeproject/firedrake/pull/2756) - closed (not a good candidate for merging to Firedrake)

PB: [https://github.com/firedrakeproject/firedrake/pull/2708](https://github.com/firedrakeproject/firedrake/pull/2708) - merged

PB: [https://github.com/firedrakeproject/firedrake/pull/2707](https://github.com/firedrakeproject/firedrake/pull/2707) - conflict needs resolving

PB: [https://github.com/firedrakeproject/fiat/pull/34](https://github.com/firedrakeproject/fiat/pull/34) - merged

PB: [https://github.com/firedrakeproject/fiat/pull/35](https://github.com/firedrakeproject/fiat/pull/35) - needs testing

PB: [https://github.com/FInAT/FInAT/pull/107](https://github.com/FInAT/FInAT/pull/107) - merged

RNH: [Firedrake: VertexOnlyMesh on ExtrudedMesh #2750](https://github.com/firedrakeproject/firedrake/pull/2750) - discussed

RNH: [FIAT: Add methods for getting L1 distance of a point from reference cells #33](https://github.com/firedrakeproject/fiat/pull/33)

RNH: [Firedrake: Guarantee finding cell for point on boundary #2662](https://github.com/firedrakeproject/firedrake/pull/2662)

## Date of next meeting

1600 UTC [2023-02-15](./Firedrake-meeting-2023-02-15)


