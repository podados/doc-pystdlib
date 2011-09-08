






The dospath module
===================




(Removed in 2.3) This module provides an **`os.path <os-path.htm>`__**
implementation for DOS platforms. You can also use it directly if you
need to handle DOS paths on other platforms.

**Example: Using the dospath module**

.. sourcecode:: python

    
    # File: `dospath-example-1.py <dospath-example-1.py>`__
    
    import dospath
    
    file = "/my/little/pony"
    
    print "isabs", "=>", dospath.isabs(file)
    print "dirname", "=>", dospath.dirname(file)
    print "basename", "=>", dospath.basename(file)
    print "normpath", "=>", dospath.normpath(file)
    print "split", "=>", dospath.split(file)
    print "join", "=>", dospath.join(file, "zorba")
    


.. sourcecode:: python

    
    $ python dospath-example-1.py
    isabs => 1
    dirname => /my/little
    basename => pony
    normpath => \my\little\pony
    split => ('/my/little', 'pony')
    join => /my/little/pony\zorba




Note that Python’s DOS support can use both forward (/) and
backwards slashes (\) as directory separators.


