






The posixfile module
=====================




(Obsolete, Unix only). This module provides a file-like object with
support for file locking. New programs should use the **fcntl** module
instead.

**Example: Using the posixfile module**

.. sourcecode:: python

    
    # File: `posixfile-example-1.py <posixfile-example-1.py>`__
    
    import posixfile
    import string
    
    filename = "counter.txt"
    
    try:
        # open for update
        file = posixfile.open(filename, "r+")
        counter = int(file.read(6)) + 1
    except IOError:
        # create it
        file = posixfile.open(filename, "w")
        counter = 0
    
    file.lock("w|", 6)
    
    file.seek(0) # rewind
    file.write("%06d" % counter)
    
    file.close() # releases lock



