






The shutil module
==================




This utility module contains some functions for copying files and
directories. The **copy** function copies a file in pretty much the
same way as the Unix **cp** command.

**Example: Using the shutil module to copy files**

.. sourcecode:: python

    
    # File: `shutil-example-1.py <shutil-example-1.py>`__
    
    import shutil
    import os
    
    for file in os.listdir("."):
        if os.path.splitext(file)[1] == ".py":
            print file
            shutil.copy(file, os.path.join("backup", file))
    


.. sourcecode:: python

    
    aifc-example-1.py
    anydbm-example-1.py
    array-example-1.py
    ...




The **copytree** function copies an entire directory tree (same as
**cp -r**), and **rmtree** removes an entire tree (same as **rm -r**).


**Example: Using the shutil module to copy and remove directory
trees**

.. sourcecode:: python

    
    # File: `shutil-example-2.py <shutil-example-2.py>`__
    
    import shutil
    import os
    
    SOURCE = "samples"
    BACKUP = "samples-bak"
    
    # create a backup directory
    shutil.copytree(SOURCE, BACKUP)
    
    print os.listdir(BACKUP)
    
    # remove it
    shutil.rmtree(BACKUP)
    
    print os.listdir(BACKUP)
    


.. sourcecode:: python

    
    ['sample.wav', 'sample.jpg', 'sample.au', 'sample.msg', 'sample.tgz',
    ...
    Traceback (most recent call last):
     File "shutil-example-2.py", line 17, in ?
       print os.listdir(BACKUP)
    os.error: No such file or directory


