






The dumbdbm module
===================




This is a very simple database implementation, similar to **`dbm
<dbm.htm>`__** and friends, but written in pure Python. It uses two
files; a binary file (.dat) which contains the data, and a text file
(.dir) which contain data descriptors.



The ` **anydbm** <anydbm.htm>`__ module uses this as the last choice.

**Example: Using the dumbdbm module**

.. sourcecode:: python

    
    # File: `dumbdbm-example-1.py <dumbdbm-example-1.py>`__
    
    import dumbdbm
    
    db = dumbdbm.open("dumbdbm", "c")
    db["first"] = "fear"
    db["second"] = "surprise"
    db["third"] = "ruthless efficiency"
    db["fourth"] = "an almost fanatical devotion to the Pope"
    db["fifth"] = "nice red uniforms"
    db.close()
    
    db = dumbdbm.open("dumbdbm", "r")
    for key in db.keys():
        print repr(key), repr(db[key])
    


.. sourcecode:: python

    
    $ python dumbdbm-example-1.py
    'first' 'fear'
    'third' 'ruthless efficiency'
    'fifth' 'nice red uniforms'
    'second' 'surprise'
    'fourth' 'an almost fanatical devotion to the Pope'



