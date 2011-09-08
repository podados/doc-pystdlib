






The linecache module
=====================




This module is used to read lines from module source code. It caches
recently visited modules (the entire source file, actually).

**Example: Using the linecache module**

.. sourcecode:: python

    
    # File: `linecache-example-1.py <linecache-example-1.py>`__
    
    import linecache
    
    print linecache.getline("linecache-example-1.py", 5)
    


.. sourcecode:: python

    
    $ python linecache-example-1.py
    print linecache.getline("linecache-example-1.py", 5)




This module is used by the ` **traceback** <traceback.htm>`__ module.


