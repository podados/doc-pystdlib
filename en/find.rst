






The find module
================




(Obsolete, 1.5.2 only). The **find** module provides a single
function, with the same name as the module:



**find(pattern, directory) ⇒ list** scans a given directory and all
its subdirectories for files matching a given pattern.



For more information on the pattern syntax, see the **`fnmatch
<fnmatch>`__** module.

**Example: Using the find module**

.. sourcecode:: python

    
    # File: `find-example-1.py <find-example-1.py>`__
    
    import find
    
    # find all JPEG files in or beneath the current directory
    for file in find.find("*.jpg", "."):
        print file
    


.. sourcecode:: python

    
    .\samples\sample.jpg



