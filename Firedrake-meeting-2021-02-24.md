Date and time 2021-02-24 16:00UTC (16:00GMT)

# Action Items
1. Pick Chair and Minuter.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. PB: add comments to own code in this PR

# Agenda

Present: DRS, CW, DH, JB, PB, KS, NB, LM, RK, PK, RNH, SV

Apologies:

## PB: Numerically stable derivatives for very high order elements in FIAT.

- (PB) Quadrature seems to be working well at high degrees.
- (PB) Proposal to change way that basis is computed.
- (DH) Only needed for P1 and P1DG. You need sum factorisation otherwise at high degree you're stuffed.
- (DH) At runtime you're running with tabulated bases. Scaling at 1D is linear. Thinks that any patch will not be controversial.
- (RK) Could be executing FIAT performance issue if changing Jacobi polynomials. Not clear on best path.
- (PB) To attempt barycentric approach.

## RNH: Why did master fail tests?
[This commit](https://github.com/firedrakeproject/firedrake/commit/6ded2a3d89cb2bc274ebd1567585757395963139) mysteriously failed tests. Is this indicative of some underlying issue with Jenkins or our codebase?

- (DH) Could be that system ran out of memory (Thetis uses a lot when it runs tests). If we can't reproduce then ignore.

## Caching Interpolators for the adjoint.

- (DH) Issue is that adjoint has a tendancy to start from an inconveniently high symbolic level. We don't reuse structures enough. How do we avoid having to rebuild the matrices, where do we stash them?
- (DH) We might want to avoid running assembly kernel or symbolic stuff. Assembly only problematic if assembling matrix which adjoint doesn't need to do(it only evaluates the action). The question then becomes can we make interpolate cache it's kernel? Thinks a global cache is suitable.
- (DH) We generally shouldn't stash interpolation matrices. If you're interpolating a coefficient then it would be worth it. Otherwise you don't know if you're getting a fixed matrix.
- (LM) If we do the action then the problem is the symbolic overhead. Then caching is the right thing to do.
- (DH) This is related to Connor's work on separating symbolics and data.

## DRS: OpenBLAS + OpenMP sad times

- (DRS) Is it worth building OpenBLAS so it's built single-threaded? Or just to provide the `NUM\_THREADS=1` var?
- (DH) Can be controlled during PETSc installation.
- (LM) There is a runtime API for this. Might be good for HPC applications.  https://github.com/xianyi/OpenBLAS/wiki/OpenBLAS-Extensions
- (DH) Need `try` block to check for BLAS versions not supporting this.
- (JB) Some users use different BLAS implementations. By default BLAS comes from whatever OS the user is on.
- (DH) Should not set `OMP_NUM_THREADS=1` in activate script since it is not always activated. Also setting `os.environ` in Firedrake init will not work.
- (DH) Setting `OMP_NUM_THREADS=1` should be documented on the install page.
- (LM) We should assume most users are not using old supercomputers so will have shared libs. We can have `try` blocks to set the number of threads.
- (PK) https://stackoverflow.com/questions/29559338/set-max-number-of-threads-at-runtime-on-numpy-openblas


## Merge PRs:

## AOB

- CSE poster session is 9am central time next week. No meeting.

## Date of next meeting

[2021-03-10](./Firedrake-meeting-2021-03-10) 16:00UTC (16:00GMT)