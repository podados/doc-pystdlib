






The strop module
=================




(Obsolete) This is a low-level module that provides fast C
implementations of most functions in the **`string <string.htm>`__**
module. It is automatically included by **`string <string.htm>`__**,
so there’s seldom any need to access it directly.



However, one reason to use this module is if you need to tweak the
path before you start loading Python modules.

**Example: Using the strop module**

.. sourcecode:: python

    
    # File: `strop-example-1.py <strop-example-1.py>`__
    
    import strop # built-in module
    import sys # built-in module
    
    # assuming we have an executable named ".../executable", add a
    # directory named ".../executable-extra" to the path
    
    if strop.lower(sys.executable)[-4:] == ".exe":
        extra = sys.executable[:-4] # windows
    else:
        extra = sys.executable
    
    sys.path.insert(0, extra + "-extra")
    
    import mymodule




In Python 2.0 and later, you should use string methods instead of
**strop**. In the above example, replace “
**strop.lower(sys.executable)**” with “
**sys.executable.lower()**”


