






The posixpath module
=====================




This module provides **`os.path <os-path.htm>`__** functionality on
Unix and other POSIX compatible platforms. You can also use it if you
need to handle POSIX paths on other platforms. It can also be used to
process uniform resource locators (URLs).

**Example: Using the posixpath module**

.. sourcecode:: python

    
    # File: `posixpath-example-1.py <posixpath-example-1.py>`__
    
    import posixpath
    
    file = "/my/little/pony"
    
    print "isabs", "=>", posixpath.isabs(file)
    print "dirname", "=>", posixpath.dirname(file)
    print "basename", "=>", posixpath.basename(file)
    print "normpath", "=>", posixpath.normpath(file)
    print "split", "=>", posixpath.split(file)
    print "join", "=>", posixpath.join(file, "zorba")
    


.. sourcecode:: python

    
    isabs => 1
    dirname => /my/little
    basename => pony
    normpath => /my/little/pony
    split => ('/my/little', 'pony')
    join => /my/little/pony/zorba



