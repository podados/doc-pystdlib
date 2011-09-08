






The filecmp module
===================




(New in 2.0) This module contains functions to compare files and
directories.

**Example: Using the filecmp module**

.. sourcecode:: python

    
    # File: `filecmp-example-1.py <filecmp-example-1.py>`__
    
    import filecmp
    
    if filecmp.cmp("samples/sample.au", "samples/sample.wav"):
        print "files are identical"
    else:
        print "files differ!"
    


.. sourcecode:: python

    
    files differ!




In 1.5.2 and earlier, you can use the **`cmp <cmp.htm>`__** and
**`dircmp <dircmp.htm>`__** modules instead.


