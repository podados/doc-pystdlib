






The cmp module
===============




(Obsolete, only in 1.5.2). This module contains a function to compare
two files.

**Example: Using the cmp module**

.. sourcecode:: python

    
    # File: `cmp-example-1.py <cmp-example-1.py>`__
    
    import cmp
    
    if cmp.cmp("samples/sample.au", "samples/sample.wav"):
        print "files are identical"
    else:
        print "files differ!"
    


.. sourcecode:: python

    
    files differ!




In Python 2.0 and later, this module has been replaced by the
**`filecmp <filecmp.htm>`__** module.


