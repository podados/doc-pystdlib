






The sys module
===============




This module provides a number of functions and variables that can be
used to manipulate different parts of the Python runtime environment.




Working with command-line arguments #
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


The **argv** list contains the arguments passed to the script, when
the interpreter was started. The first item contains the name of the
script itself.

**Example: Using the sys module to get script arguments**

.. sourcecode:: python

    
    # File: `sys-argv-example-1.py <sys-argv-example-1.py>`__
    
    import sys
    
    print "script name is", sys.argv[0]
    
    if len(sys.argv) > 1:
        print "there are", len(sys.argv)-1, "arguments:"
        for arg in sys.argv[1:]:
            print arg
    else:
        print "there are no arguments!"
    


.. sourcecode:: python

    
    script name is sys-argv-example-1.py
    there are no arguments!




If you read the script from standard input (like “ **python < sys-
argv-example-1.py**” ), the script name is set to an empty string.
If you pass in the program as a string (using the **-c** option), the
script name is set to “ **-c**”






Working with modules #
~~~~~~~~~~~~~~~~~~~~~~~


The **path** list contains a list of directory names where Python
looks for extension modules (Python source modules, compiled modules,
or binary extensions). When you start Python, this list is initialized
from a mixture of built-in rules, the contents of the **PYTHONPATH**
environment variable, and the registry contents (on Windows). But
since it’s an ordinary list, you can also manipulate it from within
the program:

**Example: Using the sys module to manipulate the module search path**

.. sourcecode:: python

    
    # File: `sys-path-example-1.py <sys-path-example-1.py>`__
    
    import sys
    
    print "path has", len(sys.path), "members"
    
    # add the sample directory to the path
    sys.path.insert(0, "samples")
    import sample
    
    # nuke the path
    sys.path = []
    import random # oops!
    


.. sourcecode:: python

    
    path has 7 members
    this is the sample module!
    Traceback (innermost last):
      File "sys-path-example-1.py", line 11, in ?
        import random # oops!
    ImportError: No module named random




The **builtin_module_names** list contains the names of all modules
built into the Python interpreter.

**Example: Using the sys module to find built-in modules**

.. sourcecode:: python

    
    # File: `sys-builtin-module-names-example-1.py <sys-builtin-module-names-example-1.py>`__
    
    import sys
    
    def dump(module):
        print module, "=>",
        if module in sys.builtin_module_names:
            print ""
        else:
            module = __import__(module)
            print module.__file__
    
    dump("os")
    dump("sys")
    dump("string")
    dump("strop")
    dump("zlib")
    


.. sourcecode:: python

    
    os => C:\python\lib\os.pyc
    sys => 
    string => C:\python\lib\string.pyc
    strop => 
    zlib => C:\python\zlib.pyd




The **modules** dictionary contains all loaded modules. The **import**
statement checks this dictionary before it actually loads something
from disk.



As you can see from the following example, Python loads quite a bunch
of modules before it hands control over to your script.

**Example: Using the sys module to find imported modules**

.. sourcecode:: python

    
    # File: `sys-modules-example-1.py <sys-modules-example-1.py>`__
    
    import sys
    
    print sys.modules.keys()
    


.. sourcecode:: python

    
    ['os.path', 'os', 'exceptions', '__main__', 'ntpath', 'strop', 'nt',
    'sys', '__builtin__', 'site', 'signal', 'UserDict', 'string', 'stat']




Working with reference counts #
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


The **getrefcount** function returns the reference count for a given
object — that is, the number of places where this variable is used.
Python keeps track of this value, and when it drops to zero, the
object is destroyed.

**Example: Using the sys module to find the reference count**

.. sourcecode:: python

    
    # File: `sys-getrefcount-example-1.py <sys-getrefcount-example-1.py>`__
    
    import sys
    
    variable = 1234
    
    print sys.getrefcount(0)
    print sys.getrefcount(variable)
    print sys.getrefcount(None)
    


.. sourcecode:: python

    
    50
    3
    192




Note that this value is always larger than the actual count, since the
function itself hangs on to the object while determining the value.



Checking the host platform #
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


The **platform** variable contains the name of the host platform:

**Example: Using the sys module to find the current platform**

.. sourcecode:: python

    
    # File: `sys-platform-example-1.py <sys-platform-example-1.py>`__
    
    import sys
    
    #
    # emulate "import os.path" (sort of)...
    
    if sys.platform == "win32":
        import ntpath
        pathmodule = ntpath
    elif sys.platform == "mac":
        import macpath
        pathmodule = macpath
    else:
        # assume it's a posix platform
        import posixpath
        pathmodule = posixpath
    
    print pathmodule




Typical platform names are **win32** for Windows 9X/NT and **mac** for
Macintosh. For Unix systems, the platform name is usually derived from
the output of the “ **uname -r**” command, such as **irix6**,
**linux2**, or **sunos5** (Solaris).



Tracing the program #
~~~~~~~~~~~~~~~~~~~~~~


The **setprofiler** function allows you to install a profiling
function. This is called every time a function or method is called, at
every return (explicit or implied), and for each exception:

**Example: Using the sys module to install a profiler function**

.. sourcecode:: python

    
    # File: `sys-setprofiler-example-1.py <sys-setprofiler-example-1.py>`__
    
    import sys
    
    def test(n):
        j = 0
        for i in range(n):
            j = j + i
        return n
    
    def profiler(frame, event, arg):
        print event, frame.f_code.co_name, frame.f_lineno, "->", arg
    
    # profiler is activated on the next call, return, or exception
    sys.setprofile(profiler)
    
    # profile this function call
    test(1)
    
    # disable profiler
    sys.setprofile(None)
    
    # don't profile this call
    test(2)
    


.. sourcecode:: python

    
    call test 3 -> None
    return test 7 -> 1




The ` **profile** <profile.htm>`__ module provides a complete profiler
framework, based on this function.



The **settrace** function is similar, but the trace function is called
for each new line:

**Example: Using the sys module to install a trace function**

.. sourcecode:: python

    
    # File: `sys-settrace-example-1.py <sys-settrace-example-1.py>`__
    
    import sys
    
    def test(n):
        j = 0
        for i in range(n):
            j = j + i
        return n
    
    def tracer(frame, event, arg):
        print event, frame.f_code.co_name, frame.f_lineno, "->", arg
        return tracer
    
    # tracer is activated on the next call, return, or exception
    sys.settrace(tracer)
    
    # trace this function call
    test(1)
    
    # disable tracing
    sys.settrace(None)
    
    # don't trace this call
    test(2)
    


.. sourcecode:: python

    
    call test 3 -> None
    line test 3 -> None
    line test 4 -> None
    line test 5 -> None
    line test 5 -> None
    line test 6 -> None
    line test 5 -> None
    line test 7 -> None
    return test 7 -> 1




The ` **pdb** <pdb.htm>`__ module provides a complete debugger
framework, based on the tracing facilities offered by this function.



Working with standard input and output #
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


The **stdin**, **stdout** and **stderr** variables contain stream
objects corresponding to the standard I/O streams. You can access them
directly if you need better control over the output than **print** can
give you. You can also replace them, if you want to redirect output
and input to some other device, or process them in some non-standard
way:

**Example: Using the sys module to redirect output**

.. sourcecode:: python

    
    # File: `sys-stdout-example-1.py <sys-stdout-example-1.py>`__
    
    import sys
    import string
    
    class Redirect:
    
        def __init__(self, stdout):
            self.stdout = stdout
    
        def write(self, s):
            self.stdout.write(string.lower(s))
    
    # redirect standard output (including the print statement)
    old_stdout = sys.stdout
    sys.stdout = Redirect(sys.stdout)
    
    print "HEJA SVERIGE",
    print "FRISKT HUMÖR"
    
    # restore standard output
    sys.stdout = old_stdout
    
    print "MÅÅÅÅL!"
    


.. sourcecode:: python

    
    heja sverige friskt humör
    MÅÅÅÅL!




All it takes to redirect output is an object that implements the
**write** method.



(Unless it’s a C type instance, that is: Python uses an integer
attribute called **softspace** to control spacing, and adds it to the
object if it isn’t there. You don’t have to bother if you’re
using Python objects, but if you need to redirect to a C type, you
should make sure that type supports the **softspace** attribute.)





Exiting the program #
~~~~~~~~~~~~~~~~~~~~~~


When you reach the end of the main program, the interpreter is
automatically terminated. If you need to exit in midflight, you can
call the **sys.exit** function instead. This function takes an
optional integer value, which is returned to the calling program.

**Example: Using the sys module to exit the program**

.. sourcecode:: python

    
    # File: `sys-exit-example-1.py <sys-exit-example-1.py>`__
    
    import sys
    
    print "hello"
    
    sys.exit(1)
    
    print "there"
    


.. sourcecode:: python

    
    hello




It may not be obvious, but **sys.exit** doesn’t exit at once.
Instead, it raises a **SystemExit** exception. This means that you can
trap calls to **sys.exit** in your main program:

**Example: Catching the sys.exit call**

.. sourcecode:: python

    
    # File: `sys-exit-example-2.py <sys-exit-example-2.py>`__
    
    import sys
    
    print "hello"
    
    try:
        sys.exit(1)
    except SystemExit:
        pass
    
    print "there"
    


.. sourcecode:: python

    
    hello
    there




If you want to clean things up after you, you can install an “exit
handler”, which is a function that is automatically called on the
way out.

**Example: Catching the sys.exit call**

.. sourcecode:: python

    
    # File: `sys-exitfunc-example-1.py <sys-exitfunc-example-1.py>`__
    
    import sys
    
    def exitfunc():
        print "world"
    
    sys.exitfunc = exitfunc
    
    print "hello"
    sys.exit(1)
    print "there" # never printed
    


.. sourcecode:: python

    
    hello
    world




In Python 2.0, you can use the ` **atexit** <atexit.htm>`__ module to
register more than one exit handler.



