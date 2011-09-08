






The cStringIO module
=====================




(Optional). This module contains a faster implementation of the
**`StringIO <stringio.htm>`__** module. It works exactly like
**StringIO**, but it cannot be subclassed.


**Example: Using the cStringIO module**

.. sourcecode:: python

    
    # File: `cstringio-example-1.py <cstringio-example-1.py>`__
    
    import cStringIO
    
    MESSAGE = "That man is depriving a village somewhere of a computer scientist."
    
    file = cStringIO.StringIO(MESSAGE)
    
    print file.read()
    


.. sourcecode:: python

    
    $ python cstringio-example-1.py
    That man is depriving a village somewhere of a computer scientist.





To make your code as fast as possible, but also robust enough to run
on older Python installations, you can fall back on the **StringIO**
module if **cStringIO** is not available:

**Example: Falling back on the StringIO module**

.. sourcecode:: python

    
    # File: `cstringio-example-2.py <cstringio-example-2.py>`__
    
    try:
        import cStringIO
        StringIO = cStringIO
    except ImportError:
        import StringIO
    
    print StringIO
    


.. sourcecode:: python

    
    $ python cstringio-example-2.py
    



