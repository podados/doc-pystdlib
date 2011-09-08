






The copy module
================




This module contains two functions which are used to copy objects.



**copy(object) ⇒ object** creates a “shallow” copy of the given
object. In this context, shallow means that the object itself is
copied, but if the object is a container, the members will still refer
to the original member objects.

**Example: Using the copy module to copy objects**

.. sourcecode:: python

    
    # File: `copy-example-1.py <copy-example-1.py>`__
    
    import copy
    
    a = [[1],[2],[3]]
    b = copy.copy(a)
    
    print "before", "=>"
    print a
    print b
    
    # modify original
    a[0][0] = 0
    a[1] = None
    
    print "after", "=>"
    print a
    print b
    


.. sourcecode:: python

    
    before =>
    [[1], [2], [3]]
    [[1], [2], [3]]
    after =>
    [[0], None, [3]]
    [[0], [2], [3]]




Note that you can make shallow copies of lists using the [:] syntax (a
full slice), and make copies of dictionaries using the **copy**
method.



In contrast, **deepcopy(object) ⇒ object** creates a “deep” copy
of the given object. If the object is a container, all members are
copied as well, recursively.

**Example: Using the copy module to copy collections**

.. sourcecode:: python

    
    # File: `copy-example-2.py <copy-example-2.py>`__
    
    import copy
    
    a = [[1],[2],[3]]
    b = copy.deepcopy(a)
    
    print "before", "=>"
    print a
    print b
    
    # modify original
    a[0][0] = 0
    a[1] = None
    
    print "after", "=>"
    print a
    print b
    


.. sourcecode:: python

    
    before =>
    [[1], [2], [3]]
    [[1], [2], [3]]
    after =>
    [[0], None, [3]]
    [[1], [2], [3]]



