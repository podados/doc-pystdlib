






The compileall module
======================




This module contains functions to compile all Python scripts in a
given directory (or along the Python path) to bytecode. It can also be
used as a script (on Unix platforms, it’s automatically run when
Python is installed).

**Example: Using the compileall module to compile all modules in a
directory**

.. sourcecode:: python

    
    # File: `compileall-example-1.py <compileall-example-1.py>`__
    
    import compileall
    
    print "This may take a while!"
    
    compileall.compile_dir(".", force=1)
    


.. sourcecode:: python

    
    This may take a while!
    Listing . ...
    Compiling .\SimpleAsyncHTTP.py ...
    Compiling .\aifc-example-1.py ...
    Compiling .\anydbm-example-1.py ...
    ...



