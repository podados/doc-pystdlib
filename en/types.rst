






The types module
=================




This module contains type objects for all object types defined by the
standard interpreter. All objects of the same type share a single type
object, so you can use **is** to test if an object has a given type.

**Example: Using the types module**

.. sourcecode:: python

    
    # File: `types-example-1.py <types-example-1.py>`__
    
    import types
    
    def check(object):
        print object,
        if type(object) is types.IntType:
            print "INTEGER",
        if type(object) is types.FloatType:
            print "FLOAT",
        if type(object) is types.StringType:
            print "STRING",
        if type(object) is types.ClassType:
            print "CLASS",
        if type(object) is types.InstanceType:
            print "INSTANCE",
        print
    
    check(0)
    check(0.0)
    check("0")
    
    class A:
        pass
    
    class B:
        pass
    
    check(A)
    check(B)
    
    a = A()
    b = B()
    
    check(a)
    check(b)
    


.. sourcecode:: python

    
    0 INTEGER
    0.0 FLOAT
    0 STRING
    A CLASS
    B CLASS
     INSTANCE
     ** INSTANCE
    **




Note that all classes have the same type, and so do all instances. To
test what class hierarchy a class or an instance belongs to, use the
built-in **issubclass** and **isinstance** functions.



In older versions of Python, the **types** module destroys the current
exception state when it is first imported. Avoid importing the module
(or any module that imports it!) from within an exception handler.


