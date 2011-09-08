






The new module
===============




(Optional in 1.5.2). This is a low-level module which allows you to
create various kinds of internal objects, such as class objects,
function objects, and other stuff that is usually created by the
Python runtime system.



Note that if you’re using 1.5.2, you may have to rebuild Python to
use this module; it isn’t enabled by the default on all platforms.
In 2.0 and later, it’s always available.

**Example: Using the new module**

.. sourcecode:: python

    
    # File: `new-example-1.py <new-example-1.py>`__
    
    import new
    
    class Sample:
    
        a = "default"
    
        def __init__(self):
            self.a = "initialised"
    
        def __repr__(self):
            return self.a
    
    #
    # create instances
    
    a = Sample()
    print "normal", "=>", a
    
    b = new.instance(Sample, {})
    print "new.instance", "=>", b
    
    b.__init__()
    print "after __init__", "=>", b
    
    c = new.instance(Sample, {"a": "assigned"})
    print "new.instance w. dictionary", "=>", c
    


.. sourcecode:: python

    
    $ python new-example-1.py
    normal => initialised
    new.instance => default
    after __init__ => initialised
    new.instance w. dictionary => assigned



