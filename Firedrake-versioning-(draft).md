### PETSc's versioning strategy

* Have a `release` branch and a `main` branch.
* Bugfix changes are merged into `release` (and `main`) whilst new features are added to `main`.
* Have *bugfix* releases (e.g. `3.22.1 -> 3.22.2`) every month where a release is made from the `release` branch.
* Have *minor* releases (e.g. `3.22.x -> 3.33.0`) every 6 months where `main` is merged into `release` and a release is made from `release`.

### Our strategy

* Also have `release` and `main` branches.
* Follow the latest release of PETSc. When a new minor release is made we check our CI and update our dependencies as needed.
* If a user wants to use PETSc `main` that is their business.