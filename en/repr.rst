






The repr module
================




Provides a robust version of the built-in **repr** function, with
limits on most sizes (string lengths, recursion, etc).


**Example: Using the repr module**

.. sourcecode:: python

    
    # File: `repr-example-1.py <repr-example-1.py>`__
    
    # note: the next line overrides the built-in 'repr' function
    # for this script
    from repr import repr
    
    # an annoyingly recursive data structure
    data = (
        "X" * 100000,
        )
    data = [data]
    data.append(data)
    
    print repr(data)
    


.. sourcecode:: python

    
    [('XXXXXXXXXXXX...XXXXXXXXXXXXX',), [('XXXXXXXXXXXX...XXXXXXXXXX
    XXX',), [('XXXXXXXXXXXX...XXXXXXXXXXXXX',), [('XXXXXXXXXXXX...XX
    XXXXXXXXXXX',), [('XXXXXXXXXXXX...XXXXXXXXXXXXX',), [(...), [...
    ]]]]]]]


