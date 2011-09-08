






The macpath module
===================




This module provides **`os.path <os-path.htm>`__** functionality on
Macintosh platforms. You can also use it if you need to handle Mac
paths on other platforms.

**Example: Using the macpath module**

.. sourcecode:: python

    
    # File: `macpath-example-1.py <macpath-example-1.py>`__
    
    import macpath
    
    file = "my:little:pony"
    
    print "isabs", "=>", macpath.isabs(file)
    print "dirname", "=>", macpath.dirname(file)
    print "basename", "=>", macpath.basename(file)
    print "normpath", "=>", macpath.normpath(file)
    print "split", "=>", macpath.split(file)
    print "join", "=>", macpath.join(file, "zorba")
    


.. sourcecode:: python

    
    isabs => 1
    dirname => my:little
    basename => pony
    normpath => my:little:pony
    split => ('my:little', 'pony')
    join => my:little:pony:zorba



