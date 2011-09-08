






The nt module
==============




(Implementation, Windows only). This module is an implementation
module used by the **`os <os.htm>`__** module on Windows platforms.
There’s hardly any reason to use this module directly; use **os**
instead.

**Example: Using the nt module**

.. sourcecode:: python

    
    # File: `nt-example-1.py <nt-example-1.py>`__
    
    import nt
    
    # in real life, use os.listdir and os.stat instead!
    for file in nt.listdir("."):
        print file, nt.stat(file)[6]
    


.. sourcecode:: python

    
    aifc-example-1.py 314
    anydbm-example-1.py 259
    array-example-1.py 48



