Date and time 2022-10-05 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter** (JB pick)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Look into updating the `@parallel` test marker (ongoing)
1. DH: talk to Jemma about Firedrake 2022 (nearly done! Abstracts open next week hopefully)

# Agenda

Present: DH, CJC, JB, MK, CW, RNH, SV, NB, DRS, PK, KS

Apologies:

## RNH: SymFem and SymFIAT
[This PR](https://github.com/firedrakeproject/fiat/pull/29) has popped out of nowhere - anyone know what it's for and what SymFem is?

https://github.com/mscroggs/symfem

Basically, yet another FIAT that symbolically compute basis functions

Crouzeix-Falk is FIATable

## RNH: Do we want to (briefly) discuss the `split` confusion complaint on slack?

Rename `split()` method:

DRS:subfields

DH:subfunctions

Action Someone: rename `split()` method `subfunctions()`; `split()` should give warning and call `subfunctions()`. 

Include comments on `split()/subfunctions()` in the first mixed demo.

## Merge PRs

CW: https://github.com/OP2/PyOP2/pull/673

Merged

KS: https://github.com/OP2/PyOP2/pull/674

Changes requested

## 

DH: In Brazil the week of 17th (We don't have meeting)

DH: In Germany in the following week (We may or may not have meeting)

## Date of next meeting

1600 UTC [2022-10-12](./Firedrake-meeting-2022-10-12)
