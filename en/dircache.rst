






The dircache module
====================




(Obsolete). This module contains a function to get a list of files in
a directory. It’s an extension of the **os.listdir** function, in
that it keeps a cache to avoid rereading directories that haven’t
been modified.

**Example: Using the dircache module**

.. sourcecode:: python

    
    # File: `dircache-example-1.py <dircache-example-1.py>`__
    
    import dircache
    
    import os, time
    
    # 
    # test cached version
    
    t0 = time.clock()
    
    for i in range(100):
        dircache.listdir(os.sep)
    
    print "cached", time.clock() - t0
    
    # 
    # test standard version
    
    t0 = time.clock()
    
    for i in range(100):
        os.listdir(os.sep)
    
    print "standard", time.clock() - t0
    


.. sourcecode:: python

    
    $ python dircache-example-1.py
    cached 0.0664509964968
    standard 0.5560845807



