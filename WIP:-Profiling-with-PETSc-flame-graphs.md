[Flame graphs](https://www.brendangregg.com/flamegraphs.html) allow you to quickly finding hotspots in your code and it is now possible to easily generate them using PETSc's logging infrastructure.
This can be a very useful entry point when trying to optimise your application and can give an indication of where the greatest performance gains are to be made.

Many functions in Firedrake have also been annotated with PETSc events so the flame graphs can tell you quite a lot about the structure of your program.

TODO *example*


## Generating the flame graph

To generate a flame graph from your Firedrake script you need to:

1. Run your code with the extra flag `-log_view :foo.txt:ascii_flamegraph`. This will run your program as usual but output an additional file called `foo.txt`.

2. Visualise the results. This can be done in one of two ways:
  
    1. Generate an SVG file using the `flamegraph.pl` script from [this repository](https://github.com/brendangregg/FlameGraph) with the command:

        ```bash
        $ ./flamegraph.pl foo.txt > foo.svg
        ```

        You can then view the output file in your browser.

    2. Upload the file to [speedscope](https://www.speedscope.app/) and view it there.

## Adding your own events

TODO

## Extra information

- The `flamegraph.pl` script assumes by default that the values in the stack traces are sample counts.
  This means that if you hover over functions in the SVG it will report the count in terms of 'samples' rather than the correct unit of microseconds.
  A simple fix to this is to include the command line option `--countname us` when you generate the SVG.

- If you call `PETSc.Log.begin()` as part of your script/package then profiling will not work as expected. 
  This is because that will start PETSc's default (flat) logging while we need to use nested logging instead.

  This issue can be avoided with the simple guard:
  
  ```python
  from firedrake.petsc import OptionsManager

  # If the -log_view flag is passed you don't need to call 
  # PETSc.Log.begin because it is done automatically.
  if "log_view" in OptionsManager.commandline_options:
      PETSc.Log.begin()
  ```