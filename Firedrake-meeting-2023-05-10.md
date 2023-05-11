Date and time 2023-05-10 16:00 BST (1500 UTC)

# Action Items
1. **Pick Chair and Minuter** (DD to pick minuter)
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)
1. JB: Move PyOP2 and FInAT to firedrakeproject
1. ALL: do things with SV's branches
1. ALL: Pick a date for Firedrake User meeting - see below
1. ~Action item: Only check links on master.~ done

# Minutes

Present: CW (minuter), JB, KS, DD, DH, RK, RNH, UZ, PB, FA

Apologies:

## DH: Firedrake user meeting progress

- DH: Looking like week of 11th September (2023), the Firedrake meeting will be Monday-Wednesday or Wednesday-Friday. The rest of the week is for a SysGenX meeting.
- RK: Firedrake 2025 could happen in Texas.
- DH: Firedrake 2024 could possibly happen in Oxford.

## DH: Mesh-to-mesh interpolation should be possible!

- DH: VOM (A) should have a method which returns a VOM (B) with the points in their original locations with the parent mesh being A. This means interpolation is just sending things over the SF.
- Action item: CW, KS, RNH should have a meeting to discuss SFs.
- DH: SFs can form their inverse. Non-matched multigrid should be straightforward to do.

## Merge PRs

 - RNH: [VOM manual pages](https://github.com/firedrakeproject/firedrake/pull/2912) - note website already needs rebuilding - small changes requested
 - UZ: [Fixing issue #2923 and Netgen docs](https://github.com/firedrakeproject/firedrake/pull/2922).
 - PB: [#2801](https://github.com/firedrakeproject/firedrake/pull/2801).

# Date of next meeting

1600 BST (1500 UTC) [2023-05-17](./Firedrake-meeting-2023-05-17)
