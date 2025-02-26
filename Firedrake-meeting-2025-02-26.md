Date and time 2025-02-26 1600 UTC

# Action Items
1. **Pick Chair and Minuter** (IM to pick?)
1. ALL: (ongoing) **triage the open issues and confirm if they are indeed still open** (and perhaps provide labels)
1. ALL: do things with SV's branches
1. DH: Email to Andreas to have 2 (+ others!!!) loopy PRs merged **TODO: FIND OUT WHICH PRS THESE ARE**
1. DH: Get Firedrake a docker open source account ([link here](https://www.docker.com/community/open-source/application/))
1. DH: Talk to GregVernon about [PR#2116](https://github.com/firedrakeproject/firedrake/pull/2116).
1. JB: Enable merge queues ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-02-21))
1. LC: Try to merge RNH' PR: [Movable VOM](https://github.com/firedrakeproject/firedrake/pull/2929)
1. PB: Profile and speed up some tests ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-10-30), [minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-11-20))
1. CW: More testing configurations ([minutes](https://github.com/firedrakeproject/firedrake/wiki/Firedrake-meeting-2024-12-11))

# Minutes

Present: DD, DH, RK, JHC, CW, KS, KN, AO, LC

Apologies:

## Pip Installation of Firedrake and Upcoming Release

- CW will handle the launch and inform users.  
- Docker installation is expected to fail.  
- `firedrake-install` will continue to function as usual.  
- Interpolation changes will be included in the October release.  

## pip install?

* JHC: Andy Thomas has suggested we could have a system install of Firedrake on the maths NextGen cluster. Is this something we'd be interested in? We could have specific versions installed for anyone doesn't need bleeding edge features.

## Merge PRs 
*Note that PRs put in this section should either be trivial or already have been reviewed. Discussion-worthy PRs should be separate agenda items.*

### DD: [UFL PR #355](https://github.com/FEniCS/ufl/pull/355)  
- Ensure it does not convert from `Zero` to `ZeroBaseForm`.  
- Investigate where it's failing to return `ZeroBaseForm`.  

### PB: [LinearSolver PR #4012](https://github.com/firedrakeproject/firedrake/pull/4012)  
- Needs to be split into smaller parts.  
- Take care to avoid breaking Firedrake.  

### PB: [Tensor kwarg PR #4056](https://github.com/firedrakeproject/firedrake/pull/4056)  
- Looks good overall.  
- It just needs a minor docstring fix. 

# Date of next meeting
1600 UTC [2025-03-05](./Firedrake-meeting-2025-03-05)