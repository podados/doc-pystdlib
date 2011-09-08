






The gdbm module
================




(Optional). This module provides an interface to the GNU **dbm**
database handler.

**Example: Using the gdbm module**

.. sourcecode:: python

    
    # File: `gdbm-example-1.py <gdbm-example-1.py>`__
    
    import gdbm
    
    db = gdbm.open("gdbm", "c")
    db["1"] = "call"
    db["2"] = "the"
    db["3"] = "next"
    db["4"] = "defendant"
    db.close()
    
    db = gdbm.open("gdbm", "r")
    
    keys = db.keys()
    keys.sort()
    for key in keys:
        print db[key],
    


.. sourcecode:: python

    
    call the next defendant



