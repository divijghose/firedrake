Date and time 2022-01-20 16:00UTC (16:00GMT)

# Action Items
1. **Pick Chair and Minuter** (LM to pick).
1. ALL: (ongoing) triage the open issues and confirm if they are indeed still open (and perhaps provide labels)

# Agenda

Present:

Apologies:

## From last time:
### Breakage on trunk: linking in `scipy`

> JDB: Fails linking against vectorised libm. Tracking issue
> https://github.com/firedrakeproject/firedrake/issues/2312

Move back to wheel in https://github.com/firedrakeproject/firedrake/pull/2313


### CW: Review my stuff

> https://github.com/firedrakeproject/firedrake/tree/connorjward/new-pyop2-api_wip
> https://github.com/OP2/PyOP2/pull/624

> Caching wrapper in Firedrake needs to be MPI aware: one cache per
> communicator. It is pretty much safe to use the `id` of a
> `dup_comm(comm)` communicator because they persist.

> - Can `PyParloop` get deleted?

> LM: Yes, I believe.

## Merge PRs:

## AOB

## Date of next meeting

1600 UTC (1600 GMT) [2022-01-27](./Firedrake-meeting-2022-01-27/)
