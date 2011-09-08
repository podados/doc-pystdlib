






The tempfile module
====================




This module allows you to quickly come up with unique names to use for
temporary files.

**Example: Using the tempfile module to create filenames for temporary
files**

.. sourcecode:: python

    
    # File: `tempfile-example-1.py <tempfile-example-1.py>`__
    
    import tempfile
    import os
    
    tempfile = tempfile.mktemp()
    
    print "tempfile", "=>", tempfile
    
    file = open(tempfile, "w+b")
    file.write("*" * 1000)
    file.seek(0)
    print len(file.read()), "bytes"
    file.close()
    
    try:
        # must remove file when done
        os.remove(tempfile)
    except OSError:
        pass
    


.. sourcecode:: python

    
    tempfile => C:\TEMP\~160-1
    1000 bytes




The **TemporaryFile** function picks a suitable name, and opens the
file. It also makes sure that the file is removed when it’s closed
(under Unix, you can remove an open file and have it disappear when
the file is closed. On other platforms, this is done via a special
wrapper class).

**Example: Using the tempfile module to open temporary files**

.. sourcecode:: python

    
    # File: `tempfile-example-2.py <tempfile-example-2.py>`__
    
    import tempfile
    
    file = tempfile.TemporaryFile()
    
    for i in range(100):
        file.write("*" * 100)
    
    file.close() # removes the file!



