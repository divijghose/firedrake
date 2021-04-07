Date and time 2021-04-07 15:00UTC (16:00BST)

# Action Items
1. Pick Chair and Minuter.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. PB: add comments to own code in this PR
1. LM: ~Crap out the geometric boundary stuff~ done: please review https://github.com/firedrakeproject/firedrake/pull/2007
1. ALL: (ongoing) schedule Firedrake Meeting + tutorial session for ICG

# Agenda

Present: Lawrence, Paul, Koki, David, Pablo, Nacime, Rob, Sophia, Jack, Stephan

Apologies: Reuben

## DRS: coding style w/black (continued...)

- (DRS) This could be an issue with `git blame` as it will touch all of the source files.
- (DRS) Also will cause a problem with existing PRs as they would have to rebase.
- Decision is to delay this discussion for those not present to get involved with.

One-off change.
One option might be that code would be black-formatted automatically.
Current proposal instead is that users should run black before commit.  
Q: what problem does it solve?  Proposition: it reduces barriers to entry in committing to codebase.
Q: are there contribution guidelines on the website?  A: not good enough.
Q: what about shared code?

Better projects: docstrings should switch from rst to numpy style.

Conclusion: 
* let's not introduce black at this time
* but let's fix the contribution guidelines

Followup question: should we have a code of conduct?
Cf https://numfocus.org/code-of-conduct
Arguments were presented on both sides.  There is a confusion of objectives.  If we have one, it should be well-written.


## DH: Orientations

## Merge PRs:

## AOB

## Date of next meeting

[2021-04-14](./Firedrake-meeting-2021-04-14) 15:00UTC (16:00BST)