






The gopherlib module
=====================




This module contains a gopher client implementation.


**Example: Using the gopherlib module**

.. sourcecode:: python

    
    # File: `gopherlib-example-1.py <gopherlib-example-1.py>`__
    
    import gopherlib
    
    host = "gopher.spam.egg"
    
    f = gopherlib.send_selector("1/", host)
    for item in gopherlib.get_directory(f):
        print item
    


.. sourcecode:: python

    
    ['0', "About Spam.Egg's Gopher Server", "0/About's Spam.Egg's
    Gopher Server", 'gopher.spam.egg', '70', '+']
    ['1', 'About Spam.Egg', '1/Spam.Egg', 'gopher.spam.egg', '70', '+']
    ['1', 'Misc', '1/Misc', 'gopher.spam.egg', '70', '+']
    ...


