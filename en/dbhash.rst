






The dbhash module
==================




(Optional). This module provides a **`dbm <dbm.htm>`__**-compatible
interface to the **bsddb** database handler.


**Example: Using the dbhash module**

.. sourcecode:: python

    
    # File: `dbhash-example-1.py <dbhash-example-1.py>`__
    
    import dbhash
    
    db = dbhash.open("dbhash", "c")
    db["one"] = "the foot"
    db["two"] = "the shoulder"
    db["three"] = "the other foot"
    db["four"] = "the bridge of the nose"
    db["five"] = "the naughty bits"
    db["six"] = "just above the elbow"
    db["seven"] = "two inches to the right of a very naughty bit indeed"
    db["eight"] = "the kneecap"
    db.close()
    
    db = dbhash.open("dbhash", "r")
    for key in db.keys():
        print repr(key), repr(db[key])


