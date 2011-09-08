






The whichdb module
===================




This module can be used to figure out which database handler that was
used for a given database file.

**Example: Using the whichdb module**

.. sourcecode:: python

    
    # File: `whichdb-example-1.py <whichdb-example-1.py>`__
    
    import whichdb
    
    filename = "database"
    
    result = whichdb.whichdb(filename)
    
    if result:
        print "file created by", result
        handler = __import__(result)
        db = handler.open(filename, "r")
        print db.keys()
    else:
        # cannot identify data base
        if result is None:
            print "cannot read database file", filename
        else:
            print "cannot identify database file", filename
        db = None




This example used the **__import__** function to import a module with
the given name.


