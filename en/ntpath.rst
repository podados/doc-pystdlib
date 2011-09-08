






The ntpath module
==================




This module provides **`os.path <os-path.htm>`__** functionality on
Windows platforms. You can also use it if you need to handle Windows
paths on other platforms.

**Example: Using the ntpath module**

.. sourcecode:: python

    
    # File: `ntpath-example-1.py <ntpath-example-1.py>`__
    
    import ntpath
    
    file = "/my/little/pony"
    
    print "isabs", "=>", ntpath.isabs(file)
    print "dirname", "=>", ntpath.dirname(file)
    print "basename", "=>", ntpath.basename(file)
    print "normpath", "=>", ntpath.normpath(file)
    print "split", "=>", ntpath.split(file)
    print "join", "=>", ntpath.join(file, "zorba")
    


.. sourcecode:: python

    
    isabs => 1
    dirname => /my/little
    basename => pony
    normpath => \my\little\pony
    split => ('/my/little', 'pony')
    join => /my/little/pony\zorba




Note that this module treats both forward slashes (/) and backward
slashes (\) as directory separators.


