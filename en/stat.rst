






The stat module
================




This module contains a number of constants and test functions that can
be used with the **os.stat** function.

**Example: Using the stat module**

.. sourcecode:: python

    
    # File: `stat-example-1.py <stat-example-1.py>`__
    
    import stat
    import os, time
    
    st = os.stat("samples/sample.txt")
    
    print "mode", "=>", oct(stat.S_IMODE(st[stat.ST_MODE]))
    
    print "type", "=>",
    if stat.S_ISDIR(st[stat.ST_MODE]):
        print "DIRECTORY",
    if stat.S_ISREG(st[stat.ST_MODE]):
        print "REGULAR",
    if stat.S_ISLNK(st[stat.ST_MODE]):
        print "LINK",
    print
    
    print "size", "=>", st[stat.ST_SIZE]
    
    print "last accessed", "=>", time.ctime(st[stat.ST_ATIME])
    print "last modified", "=>", time.ctime(st[stat.ST_MTIME])
    print "inode changed", "=>", time.ctime(st[stat.ST_CTIME])
    


.. sourcecode:: python

    
    mode => 0664
    type => REGULAR
    size => 305
    last accessed => Sun Oct 10 22:12:30 1999
    last modified => Sun Oct 10 18:39:37 1999
    inode changed => Sun Oct 10 15:26:38 1999



