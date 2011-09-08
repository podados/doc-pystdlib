






The fcntl module
=================




(Unix only). This module provides an interface to the **ioctl** and
**fcntl** functions on Unix. They are used for “out of band”
operations on file handles and I/O device handles. This includes
things like reading extended attributes, controlling blocking,
modifying terminal behavior, etc.



Exactly how to use these functions are highly platform dependent. For
more information on what you can do on your platform, check the
corresponding Unix manual pages.



This module also provides an interface to Unix’ file locking
mechanisms. The following example uses the **flock** function to place
an advisory lock on the file, while it is being updated.



The output shown below was obtained by running three instances of the
program in parallel, like this: **python fcntl-example-1.py& python
fcntl-example-1.py& python fcntl-example-1.py&** (all on one command
line). If you comment out the call to **flock**, the counter will not
be updated properly.

**Example: Using the fcntl module for locking**

.. sourcecode:: python

    
    # File: `fcntl-example-1.py <fcntl-example-1.py>`__
    
    import fcntl, FCNTL
    import os, time
    
    FILE = "counter.txt"
    
    if not os.path.exists(FILE):
        # create the counter file if it doesn't exist
        file = open(FILE, "w")
        file.write("0")
        file.close()
    
    for i in range(20):
        # increment the counter
        file = open(FILE, "r+")
        fcntl.flock(file.fileno(), FCNTL.LOCK_EX)
        counter = int(file.readline()) + 1
        file.seek(0)
        file.write(str(counter))
        file.close() # unlocks the file
        print os.getpid(), "=>", counter
        time.sleep(0.1)


.. sourcecode:: python

    
    $ python fcntl-example-1.py
    30940 => 1
    30942 => 2
    30941 => 3
    30940 => 4
    30941 => 5
    30942 => 6



