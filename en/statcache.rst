






The statcache module
=====================




This module contains a function which returns information about files.
It’s an extension of the **os.stat** function, in that it keeps a
cache with recently collected information.

**Example: Using the statcache module**

.. sourcecode:: python

    
    # File: `statcache-example-1.py <statcache-example-1.py>`__
    
    import statcache
    import os, stat, time
    
    now = time.time()
    for i in range(1000):
        st = os.stat("samples/sample.txt")
    print "os.stat", "=>", time.time() - now
    
    now = time.time()
    for i in range(1000):
        st = statcache.stat("samples/sample.txt")
    print "statcache.stat", "=>", time.time() - now
    
    print "mode", "=>", oct(stat.S_IMODE(st[stat.ST_MODE]))
    print "size", "=>", st[stat.ST_SIZE]
    print "last modified", "=>", time.ctime(st[stat.ST_MTIME])
    


.. sourcecode:: python

    
    os.stat => 0.371000051498
    statcache.stat => 0.0199999809265
    mode => 0666
    size => 305
    last modified => Sun Oct 10 18:39:37 1999



