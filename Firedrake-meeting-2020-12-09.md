Date and time 2020-12-09 16:00UTC (16:00GMT)

# Action Items
1. Pick Chair and Minuter.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. ~??: Build master on centos to catch errors~
1. CW: Report back on GCC JIT

# Agenda

Present: SV, CW, DAH, LM, DRS, KS, JDB, SK, RNH, KK

Apologies: CJC

## CW: Found [dragonffi](https://github.com/aguinet/dragonffi)

Looks to be a good choice for a LLVM-based JIT.

Action: CW to try getting it to work at all.

Things to check: can get debuggable code (if there's a segfault, do we
only see assembly, or also the C code?). Can we control compiler
flags?


## JB: CentOS Build
Given that CentOS is [going
away](https://blog.centos.org/2020/12/future-is-centos-stream/), do we
want to keep the "Build master on centos" action item or abandon?

Decision: Removed item.

## RNH + DH: Non-Point Evaluation Dual Evals/Interpolations
How do we deal with complicated cases, like different numbers of
different "classes" of functionals per element?

Problem: when we have functionals that are more than just point evals,
we get an effectively "unstructured" list of points at which to
evaluate the expression. We can stack these all up, but how do we then
know which quadrature weight to apply to which evaluation, and which
functional they should go out to.

Proposal: Generate points with structure, do function evaluation to
get gem for evaluation at all those points. Can optimise this
expression with the tsfc spectral optimiser.

Then we need to extend GEM with data dependent indexing to unpick
this. That is, add a gem node for "unstructured" indexing. Hopefully
one only then needs to handle scheduling (gem->impero) + loopy
codegen.


## Merge PRs:


## AOB


## Date of next meeting

[2020-12-16](./Firedrake-meeting-2020-12-16) 16:00UTC (16:00GMT)
