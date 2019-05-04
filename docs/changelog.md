Version 19.05
===

**Features**:

+ Add progress dialog on contracted link assortment enumeration.
+ Nested do loop method for contracted graph enumeration.
    + Speed up performance of searching contracted graphs.

**Development**:

+ None

Version 19.04
===

**Features**:

+ Add basic Readthedocs and MkDocs project for user manual.

**Development**:

+ Contracted graph enumeration algorithm:
    + Speed up performance for searching between link assortment.

Version 19.03
===

**Features**:

+ Show a progress dialog when loading file or database.
+ CAD kernels improvements.
+ Performance improvement of algorithms.
+ Monochrome mode for mechanism. (Excluding indicators)

**Development**:

+ Remove related import at "core" (root module) to speed up the compile time.
+ Remove customized splash class that is used once.
+ Update new Cython wrapper of Python-Solvespace.
    + Removed SWIG requirement.
+ Removed the support of Eric IDE.
+ Basic logging method instead of "print" function.
    + Now Pyslvs will create a log file beside executable.
    + The log file will be delete after generally closed Pyslvs.
+ Add startup time record.
+ Test the kernels when packing executable.
+ Performance improvement if dimensional synthesis algorithm.
+ Add code of conduct.

Version 19.02
===

**Features**:

+ Add single graph saving function for synthesis collection panel.
+ UI description improvements.
+ Removed "ground enumerate" button of synthesis collection panel.
+ Fix the bug of deleting a point is inside the input pairs.
+ Fix the bug of limitation option when algorithm option loaded.
+ Widget focus behavior correction of tables.
+ Fix the bug of saving a YAML project.
+ Remove "solution" preview function from preview canvas class.
+ Adjustment margin size of preview window.
+ Support the "Categories" key of AppImage desktop file.
+ Enhancement of "link adjust" function.
+ Enhancement of mechanism grammar.
+ Set the table headers to auto resize mode.
+ Change the merge behavior of synthesis result as add to storage.
+ New style selection tip widget instead of QToolTip.
+ Solve the memory leak of Qt dialogs.
+ Unified the IO encoding of text-based files.

**Development**:

+ Stop support Python 3.6 or below.
+ Since become 3.7:
    + Follow the literal type annotation style instead of strings.
    + Recursive import when doing type checking.
    + Generic typing with Qt object is allowed.
+ Change the name of all most camelcase methods to lowercase.
+ Re-design the inherit method of main window classes.
+ Simplified Qt module introduction when imported.
+ Rename "signal" and "slot" introduction of PyQt.
+ Enhancement of enum types.
+ Adjust limitation option of algorithm to "max_gen", "min_fit" and "max_time".
+ BFGS solver:
    + Fix memory leaked.
    + Reformat the wrapper for more readability.
+ Rename the dialog resources as "dialogs".
+ Refactor of all widgets names into underscore lowercase.
+ Add generate source function with "generate_source.py".
+ Environment of Visual Studio 2017 version 15.9 supported.

Version 19.01
===

**Development**:

+ This version has been skipped.

Version 18.12
===

**Features**:

+ "External loop" layout for atlas of structural synthesis.
+ Other layout functions are removed from option.
+ Add progress dialog for number synthesis.
+ Fix the error of dimensional synthesis.
+ Fix the bug of number synthesis when import from mechanism.
+ Image background color fixed for structural synthesis atlas.

**Development**:

+ Methods and function naming corrections of Cython libraries.
+ Removed NetworkX requirement.
+ Two functions are moved to core kernel. ("edges_view" and "graph2vpoints")
+ Add "--platform" argument for Qt plugins.
+ Optimization of joint type of "VPoint" class from core kernel.
+ Update SHELL variable of Makefile on Windows platform.
+ Environment of Visual Studio 2017 version 15.8 supported. (`_MSC_VER == 1915`)

Version 18.11
===

**Features**:

+ UI improvement of structural synthesis and collection panel.
    + Record inspected information.
    + Show more attributes of the graph.
    + Add "Find by links" and "Find by contracted links" buttons.
    + Add "Link as node" option in structural collection panel, but the layout is readonly.
    Auto match graph assortments that came from "mechanism" page.
+ Add independent option of contracted link assortments.
+ Fix EOF error when loading edge set data from text file.
+ Removed unnecessary layout engine option.

**Development**:

+ Replaced all most NetworkX graph type to Pyslvs graph type.
+ Removed PyDot requirement.
+ Add planar graph checking of atlas algorithm.
+ Performance improvements of atlas algorithm (Object creation and function calling).

Version 18.10
===

**Features**:

+ UI adjustments of "Synthesis" tab pages.
+ Adjust options of structural synthesis.
+ Remove "time and fitness" data in file format.
+ Chart dialog only shows after the algorithm completed.
+ Fixed bug in batch function of algorithm tasks.

**Development**:

+ Improvements of "Adesign" kernel.
+ Fixed an error caused by DE strategy option.
+ High performance improvements of atlas algorithm.

Version 18.09.1
===

**Features**:

+ Fix "Save as" error on Qt slot.
+ New YAML-based file format:
    + Suffix: `.pyslvs.yml`
    + New text-based format to support version control.

**Development**:

+ Module of important widgets are be moved to `__init__.py`.
+ Fix compiler option error caused by Python (`cygwinccompiler.py`).
+ Adjust all functions and "private" methods name with PEP 8.
+ New deploy options of Github releases.

Version 18.09
===

**Features**:

+ Appearance adjustments of main canvas.
+ Add scale mechanism option.
+ Change atlas algorithm "cancel" behavior to "skip":
    + Realized partial searching in atlas algorithm.
    + User can skip and keep partial result at each searching step.
+ Add fully support for Mac OS platform:
    + Standalone executable file compilation.
    + Automatic switch to fusion mode to avoid border too wide.
    + CI testing.
+ Add new examples:
    + "Crank slider (Three bar)"
    + "Slider lifter"
+ Input variable:
    + Support slider joint.
    + Add filter for variable list.

**Development**:

+ Using abstract class to implement partial methods.
+ Redefine solver function of Python-Solvespace.
+ Modules are renamed to lower case.
+ Add AppVeyor CI support.

Version 18.08
===

**Features**:

+ Important: File format was changed.
+ Add new examples:
    + "Stephenson I"
    + "Watt I"
    + "Watt II"
    + "Lift Tailgate"
    + "Crank lifter"
    + "Inverted slider"
    + "Ten Fold's levers"
+ Selection label function improvement.
+ UI and selection mode improvements.
+ Add FPS counter.
+ Add background settings.
+ Add limitation of input mechanism in UI.
+ Add command line option to choose specified solver when startup.
+ Adjust interface of about dialog.

**Development**:

+ Database module "peewee" rename to "database".
+ Database function improvements.
+ All PyQt slots renaming to short names.
+ Python version should upgrade to 3.6 or above to support formatted string.

Version 18.07
===

**Features**:

+ Dimensional synthesis data settings and UI has been changed.
+ Input variable settings and UI has been changed.
+ New solving kernel "Sketch Solve" in "pyslvs" core library.
+ Add new examples:
    + "Stephenson II"
    + "Stephenson III"
+ Adjust ask saving message box in "FileWidget" class.

**Development**:

+ Add "Python-Solvespace" kernel as submodule.
+ Merge "-w" flag to "-d" flag.
+ New format with dimensional synthesis function.
+ Example list has been move to "pyslvs" core kernel.
+ Change behavior of auto path preview function.

Version 18.06
===

**Features**:

+ Free move mode:
    + Linkage editing is supported in expression table.
    + Fix the error of angle updating.
+ Show the values on expression table.
+ Add solution selection mode with expression table.
+ Dimensional synthesis function:
    + Re-designed user interface.

**Development**:


+ Update module "dxfwrite" to "ezdxf".
+ Change "Pyslvs" kernel into submodule, including changelog.


Version 18.05
===

**Features**:

+ Linkage selection mode:
    + New linkage selection function for both of table widget and main canvas.
    + Using ctrl + mouse wheel can adjust the tab of entities table widget.
+ Main canvas:
    + Add cursor tooltips when dragging on main canvas.
    + Center zooming function and option with 'by cursor' and 'by canvas center'.
+ Colors:
    + Pyslvs can support custom color by using '(R, G, B)' string.
    + Add color picker in setting interface.
+ Solvespace format:
    + Comments will be generate into a new layout in Solvespace format.
    + Simple reading function for \*.slvs format (only support R joint).
    + New option to generate part files.
+ Path record:
    + Add "copy path" function in path context menu.
    + Path preview function are support P joint.
+ New solving kernel option "Pyslvs" as default.
+ Add mouse snapping option (default 1 unit).
+ Triple ball lifter example.
+ Shortcut keys adjustment.
+ "Add" command of storage function will not clean the canvas (should do it by self).
+ Add "merge linkages" function in link context menu.
+ Add virtual model option to change linkages appearance.

**Development**:

+ Expression grammar:
    + New highlight module Pygments, use to support Python and PMKS expression.
    + Now PMKS grammar can support color string, one-line annotations, multiple line and indentations.
+ Cython libraries:
    + Pyslvs kernel has been independently.
    + Compile method adjustment.
    + Merge into 'pyslvs' folder.
    + Using Python typing for Python functions in Cython libraries.
    + Add Cython header to sharing declarations between libraries.
    + Add new "PXY" function to make solution of P joint.
+ Compile:
    + Compile process improvement.
    + Reduce the size while packing AppImage file.
    + Reduce the size of images.
+ Solvespace format:
    + Python API for simple 2D sketch IO.
+ Modules and objects naming adjustment.
+ PyQt version should upgrade to 5.10 or above to support Qt graph methods.


Version 18.04
===

**Features**:

+ Auto preview path will be shown when input joint has been set.
+ Triangular solutions can be show in main canvas when switch to "Expression" table.
+ New driver setting mode of triangular iteration.
+ Add a spin box for input QDial.
+ 'New link' functional behavior improvement.
+ Pyslvs will save the settings in local, if user let it to do this.

**Development**:

+ Several functional corrections and optimizations.
+ PLPP function has been optimized.
+ "P0", "P1", "P2" letters will be use as expression, instead of "A", "B", "C".
+ Main window method was split into sub function at "widget" folder.
+ Build process improvements.


Version 18.03:

**Features**:

+ Fix an error caused by wrong grounded linkage.
+ Auto configuration function in triangular iteration.
+ Backtrack function for the 'Keep DOF' option.
+ Database will saving the inputs variables settings.
+ Inputs variables settings can be support undo function.

**Development**:

+ Script annotations for functions and classes.
+ Separate 'Inputs' tab widget.
+ Cython type checker for Python containers.
+ Windows executable file was compiled by Mysys 2.


Version 18.02
===

**Features**:

+ Dimensional synthesis function has been associated with triangular iteration function.
+ Related function about dimensional synthesis has been improved.
    + Loading profile function.
    + Appearance and editing function of target paths.
    + Result operating function.
    + Task target has been added "fitness" and "time" limitation options.
+ Preview canvas in triangular iteration has been applied to related interface.
+ "New link" function improvement.
+ "Zoom to fit" function improvement.
+ "Mechanism storage" function improvement.
+ Check for updates function.

**Development**:

+ Some improvements about functions and objects.
+ Dimensional synthesis dialog move to a new name space.
+ Remove unnecessary icons and library source code to make execution size reduction.
+ More errors fixed.


Version 18.01
===

**Features**:

+ Triangular iteration function.
+ Collections IO improvements.
+ Dimensional synthesis function improvements.
+ Some options and interface adjustments.

**Development**:

+ Use `__init__.py` modules to manage classes and functions.
+ Cython kernel of Number synthesis.
+ Adjust some modules and classified.

Older Version
===

Version 0.1.0 to 0.9.0.

Prototype stage was not recorded.