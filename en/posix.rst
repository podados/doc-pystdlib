






The posix module
=================




(Implementation, Unix/POSIX only). This module is an implementation
module used by the **`os <os.htm>`__** module on Unix and other POSIX
systems. While everything in here can be (and should be) accessed via
the **os** module, you may wish to explicitly refer to this module in
situations where you want to make it clear that you expect POSIX
behavior.

**Example: Using the posix module**

.. sourcecode:: python

    
    # File: `posix-example-1.py <posix-example-1.py>`__
    
    import posix
    
    for file in posix.listdir("."):
        print file, posix.stat(file)[6]
    


.. sourcecode:: python

    
    aifc-example-1.py 314
    anydbm-example-1.py 259
    array-example-1.py 48



