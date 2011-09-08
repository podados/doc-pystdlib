






The py_compile module
======================




This module allows you to explicitly compile Python modules to
bytecode. It behaves like Python’s **import** statement, but takes a
file name, not a module name.

**Example: Using the py_compile module**

.. sourcecode:: python

    
    # File: `py-compile-example-1.py <py-compile-example-1.py>`__
    
    import py_compile
    
    # explicitly compile this module
    py_compile.compile("py-compile-example-1.py")




The ` **compileall** <compileall.htm>`__ module can be used to compile
all Python files in an entire directory tree.


