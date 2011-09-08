






The statvfs module
===================




This module contains a number of constants and test functions that can
be used with the optional **os.statvfs** function, which returns
information about a file system.

**Example: Using the statvfs module**

.. sourcecode:: python

    
    # File: `statvfs-example-1.py <statvfs-example-1.py>`__
    
    import statvfs
    import os
    
    st = os.statvfs(".")
    
    print "preferred block size", "=>", st[statvfs.F_BSIZE]
    print "fundamental block size", "=>", st[statvfs.F_FRSIZE]
    print "total blocks", "=>", st[statvfs.F_BLOCKS]
    print "total free blocks", "=>", st[statvfs.F_BFREE]
    print "available blocks", "=>", st[statvfs.F_BAVAIL]
    print "total file nodes", "=>", st[statvfs.F_FILES]
    print "total free nodes", "=>", st[statvfs.F_FFREE]
    print "available nodes", "=>", st[statvfs.F_FAVAIL]
    print "max file name length", "=>", st[statvfs.F_NAMEMAX]
    


.. sourcecode:: python

    
    preferred block size => 8192
    fundamental block size => 1024
    total blocks => 749443
    total free blocks => 110442
    available blocks => 35497
    total file nodes => 92158
    total free nodes => 68164
    available nodes => 68164
    max file name length => 255



