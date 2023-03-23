Firedrake aims to work on all [currently supported versions](https://endoflife.date/macos) of macOS.

## Developer notes

Once security updates stop getting released for a particular macOS version the default `MACOSX_DEPLOYMENT_TARGET` environment variable in [`firedrake-install`](https://github.com/firedrakeproject/firedrake/blob/master/scripts/firedrake-install) should be changed.

A good indication that the install script may need to be modified is if macOS users start reporting install failures where the PETSc `configure.log` contains lines like the following:

```
ld: warning: object file (/opt/homebrew/Cellar/gcc/12.2.0/lib/gcc/current/gcc/aarch64-apple-darwin22/12/libgcc.a(fixhfti.o)) was built for newer macOS version (11.0) than being linked (10.15)
```

In this case indicating that `MACOSX_DEPLOYMENT_TARGET` should be [updated from 10.15 to 11.0](https://github.com/firedrakeproject/firedrake/pull/2838).