






The shelve module
==================




This module uses the database handlers to implement persistent
dictionaries. A shelve object uses string keys, but the value can be
of any data type, as long as it can be handled by the **`pickle
<pickle.htm>`__** module.

**Example: Using the shelve module**

.. sourcecode:: python

    
    # File: `shelve-example-1.py <shelve-example-1.py>`__
    
    import shelve
    
    db = shelve.open("database", "c")
    db["one"] = 1
    db["two"] = 2
    db["three"] = 3
    db.close()
    
    db = shelve.open("database", "r")
    for key in db.keys():
        print repr(key), repr(db[key])
    


.. sourcecode:: python

    
    'one' 1
    'three' 3
    'two' 2




The following example shows how to use the **shelve** module with a
given database driver.

**Example: Using the shelve module with a given database**

.. sourcecode:: python

    
    # File: `shelve-example-3.py <shelve-example-3.py>`__
    
    import shelve
    import gdbm
    
    def gdbm_shelve(filename, flag="c"):
        return shelve.Shelf(gdbm.open(filename, flag))
    
    db = gdbm_shelve("dbfile")



