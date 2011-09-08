






The anydbm module
==================




This module provides a unified interface to the simple database
drivers supported by Python.



When you open an existing database, the module uses` **whichdb**
<whichdb.htm>`__ to figure out what driver to use. When you create a
new database, it checks for **`dbhash <dbhash.htm>`__**, **`gdbm
<gdbm.htm>`__**, **`dbm <dbm.htm>`__**, or **`dumbdbm
<dumbdbm.htm>`__**, in that order.

**Example: Using the anydbm module**

.. sourcecode:: python

    
    # File: `anydbm-example-1.py <anydbm-example-1.py>`__
    
    import anydbm
    
    db = anydbm.open("database", "c")
    db["1"] = "one"
    db["2"] = "two"
    db["3"] = "three"
    db.close()
    
    db = anydbm.open("database", "r")
    for key in db.keys():
        print repr(key), repr(db[key])


.. sourcecode:: python

    
    '2' 'two'
    '3' 'three'
    '1' 'one'



