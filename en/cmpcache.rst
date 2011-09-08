






The cmpcache module
====================




(Obsolete, only in 1.5.2). This module contains a function to compare
two files. It’s an extension of the **`cmp <cmp.htm>`__** module, in
that it keeps a cache over recently made comparisons.

**Example: Using the cmpcache module**

.. sourcecode:: python

    
    # File: `cmpcache-example-1.py <cmpcache-example-1.py>`__
    
    import cmpcache
    
    if cmpcache.cmp("samples/sample.au", "samples/sample.wav"):
        print "files are identical"
    else:
        print "files differ!"


.. sourcecode:: python

    
    files differ!




In Python 2.0 and later, this module has been replaced by the
**`filecmp <filecmp.htm>`__** module.


