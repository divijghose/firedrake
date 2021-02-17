Date and time 2021-02-10 16:00UTC (16:00GMT)

# Action Items
1. Pick Chair and Minuter.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)

# Minutes

Present:

DH, LM, PK, CW, DS, JB, NB, RNH, RK, SK, SV, KS

Apologies: 

## Stash `assembly_callable` on the form? (CW)

- This would eliminate a lot of the symbolic overhead occurring in `assemble()` but may annoy James.

RK observed 45% assembly time saving by using `create_assembly_callable`.

PyOP2 design question:

- Need nice separation: things that you need to execute and data to execute those on.
- ParLoop objects not to hold DataCarrier objects at all: in principle we just need shapes.
- args (shape, READ/WRITE, Map) are now in code, but these should actually be attached to the kernel separately from data.

Short term hack?
- Don't introduce public API change
- Modify `create_asembly_callable` so that it would take output tensor?

Realated (pointwise assignment):

Pointwise assignement is inefficient for the same reason, but this is harder as there is no persistent object lying around (we make new expression every time).

-> Lift expressions to make them persistent objects.

Related (time integration):

Define reusable Block, and allow for:
```
while t < ntime:
    timestep.replay() # run through stashed parloop
```

CW may or may not work on these.


## FEnICS 2021
What to present

RK: irksome

India: dual space

NB : external operator

KS: subspace (may or may not) -> write abstract

Deadline: 20/02/2021

## RNH: TSFC "bug fixes"
See https://github.com/firedrakeproject/tsfc/pull/237 - source of some discussion (Miklos doesn't think the PR is necessary) that seems to get at some core GEM design philosophy questions.

Two possibilities:
1. `A[i,j]=B[j]` -> implicitly broadcast across i
2. `A[i,j]=Broadcast(B[j], i)` or something (explicit broadcast node makes it more type-safe)

## Merge PRs: 

## AOB

## Date of next meeting

[2021-02-17](./Firedrake-meeting-2021-02-17) 16:00UTC (16:00GMT)
