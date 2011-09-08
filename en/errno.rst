






The errno module
=================




This module defines a number of symbolic error codes, such as
**ENOENT** ( “no such directory entry” ), **EPERM** (
“permission denied” ), and others. It also provides a dictionary
mapping from platform dependent numerical error codes to symbolic
names.



In most cases, the **IOError** exception provides a 2-tuple with the
numerical error code, and an explanatory string. If you need to
distinguish between different error codes, use the symbolic names
where possible.

**Example: Using the errno module**

.. sourcecode:: python

    
    # File: `errno-example-1.py <errno-example-1.py>`__
    
    import errno
    
    try:
        fp = open("no.such.file")
    except IOError, (error, message):
        if error == errno.ENOENT:
            print "no such file"
        elif error == errno.EPERM:
            print "permission denied"
        else:
            print message
    


.. sourcecode:: python

    
    no such file




The following example is a bit contrived, but it shows how to use the
**errorcode** dictionary to map from a numerical error code to the
symbolic name.

**Example: Using the errorcode dictionary**

.. sourcecode:: python

    
    # File: `errno-example-2.py <errno-example-2.py>`__
    
    import errno
    
    try:
        fp = open("no.such.file")
    except IOError, (error, message):
        print error, repr(message)
        print errno.errorcode[error]
    


.. sourcecode:: python

    
    2 'No such file or directory'
    ENOENT



