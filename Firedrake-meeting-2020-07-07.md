Date and time 2020-07-07 15:00UTC (16:00BST)

# Action Items
1. **Choose someone to minute and chair**
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. KS, (DH, LM): Document describing what we think the mixed domain interface should look like
(and hence what is needed in UFL, and whether it matches the existing Fenics efforts). Try an alternative description and make previously agreed changes.
1. \*\*: Think about the correct mathematical formulation for Filtered
1. ALL: Please review complex.
1. ~\*\*: Add `--remove-build-files` to make install smaller; convert this to an issue~ [#1771](https://github.com/firedrakeproject/firedrake/issues/1771)


# Minutes

Present: Reuben Hill, Lawrence Mitchell, David Ham, Koki Sagiyama, Paul Kelly, Robert Kirby, Jack Betteridge, Matthew Kan, Mohammad Usman, Nacime Bouziani, Sofia Simola, Sophia Vorderwuelbecke

Apologies: Dan Shapero

## RCK: discuss FIAT progress for dual spaces, what to do in FInAT dual evaluation?

(Note: busy discussion - below notes may contain inaccuracies)

### Element Oracle
 - Problem: Practical implementation has moved well beyond initial design constraints of FIAT and elements are all over the place and complicated interdependencies. Lots of pullbacks in UFL which suggest leaky interface.
 - Proposed Solution: Create an element oracle that would replace FIAT, FinAT, element parts of UFL, and some bits of TSFC. (Rob Kirby can expand on this)
 - Raised issue: UFL needs symbolic pullbacks e.g. for shape derivatives.
   - Response: Have element oracle return legal UFL as result of a pullback. Make element oracle a registered package to avoid circular dependencies (David Ham can expand on this).
   - Alternative: Have coordinate derivative callback in API of element oracle.
 - Making this happen:
   - David Ham will have an UG student able to put in 8 weeks work on element oracle from the end of July.
   - Lawrence Mitchell suggests straw-manning the interface to get it right before putting in serious programming work.

### Dual Spaces in FIAT
 - Rob Kirby has worked on adding dual space representations to FIAT with new concept of point dual bases from which dual functions can be represented as linear sums. (Rob Kirby can expand on this)
 - Could make certain interpolations work out of the box which currently do not.
 - Rob Kirby to make PR.

## LM: reworking MG interpolation
 - Want to make use of new technology for FIAT.
 - Lawrence open to suggestions on how to move forwards

## LM: Vectorisation status
 - Only 1 kernel test failing at time of writing. Close to solving.

## JB: SIAM-CSE
Thoughts on running minisyposia as well as minisymposterium? Chased up Chris Richardson and he's very keen to contribute for possible Exascale simulation themed mini. (Also happy to contribute a poster).

 - Suggested that JB go ahead with Exascale simulation themed minisymposium. 
   - DH will provide names of who to contact

## JB: Randomgen
Is Firedrake currently using any features of randomgen that aren't now in numpy?

 - Apparently parallel safe RNG has been ported to numpy.
 - Aim to try and drop the dependency if possible.

## KS: ufl.Filtered/ufl.Transformed -> ufl.Masked
Status:
https://github.com/firedrakeproject/firedrake/issues/1648 (see `main.pdf` in edited issue description)

Summary:

0. Viewing `ufl.Transformed` as a map is awkward.

1. Introduce `V0 = ufl.Subspace(V, some_constraint)`

2. Introduce `v0 = ufl.Masked(v, V0)` (v0 = v if v in V0 else 0) 

 - After reviewing `main.pdf`:
   - Still have issues with concepts being basis-dependent which is not allowed in UFL.
   - Make concepts like `FunctionSpaceModifier` non-basis-dependent by making them "masks".
   - More design work needed.

## DH Absense
DH will be away for several of the next firedrake meetings.

## Date of next meeting
2020-07-14 15:00UTC (16:00BST)
