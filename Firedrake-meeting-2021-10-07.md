Date and time 2021-10-07 15:00UTC (16:00BST)

# Action Items
1. **Pick Chair and Minuter**.
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)

# Agenda

Present: CW (minuter), DH, CC, NB, LM, JB, DRS, KK, RK, SV

Apologies: KS, RNH

## GitHub Discussions - DH

LM: You aren't allowed to write maths, even though Slack doesn't let us do this. Answers are more long-term discoverable.

DH: Lower engagement barrier. Better notification settings.

LM: Mailing list is not very active.

DRS: Doesn't want to complicated things. Already have issues, mailing list and Slack.

DH: Can move entries between issues (bugs) and discussions (user support).

LM: Discussions are marked 'resolved' rather than 'closed' - more discoverable.

DH: To set this up and rebuild website.

## Merge PRs:

## AOB

### Element testing - RK

RK: Can the Firedrake test suite accept new element tests?

DH: Any under 10s are fine.

CC: Usually does not go to full convergence, instead some error.

LM: This approach has some issues.

LM: Most time in test suite is spent compiling so this is the bigger issue.

RK: Some elements are quite complicated so codegen can take a long time.

DH: Use a relatively simple form, that's usually the issue. Apart from interpolation due to a known issue (huge temporaries).

## Date of next meeting

1500 UTC (1600 BST) [2021-10-14](./Firedrake-meeting-2021-10-14/)
