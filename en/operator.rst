






The operator module
====================




This module provides a “functional” interface to the standard
operators in Python. The functions in this module can be used instead
of some **lambda** constructs, when processing data with functions
like **map** and **filter**.



They are also quite popular among people who like to write obscure
code, for obvious reasons.


**Example: Using the operator module**

.. sourcecode:: python

    
    # File: `operator-example-1.py <operator-example-1.py>`__
    
    import operator
    
    sequence = 1, 2, 4
    
    print "add", "=>", reduce(operator.add, sequence)
    print "sub", "=>", reduce(operator.sub, sequence)
    print "mul", "=>", reduce(operator.mul, sequence)
    print "concat", "=>", operator.concat("spam", "egg")
    print "repeat", "=>", operator.repeat("spam", 5)
    print "getitem", "=>", operator.getitem(sequence, 2)
    print "indexOf", "=>", operator.indexOf(sequence, 2)
    print "sequenceIncludes", "=>", operator.sequenceIncludes(sequence, 3)
    


.. sourcecode:: python

    
    add => 7
    sub => -5
    mul => 8
    concat => spamegg
    repeat => spamspamspamspamspam
    getitem => 4
    indexOf => 1
    sequenceIncludes => 0





The module also contains a few functions which can be used to check
object types:

**Example: Using the operator module for type checking**

.. sourcecode:: python

    
    # File: `operator-example-2.py <operator-example-2.py>`__
    
    import operator
    import UserList
    
    def dump(data):
        print type(data), "=>",
        if operator.isCallable(data):
            print "CALLABLE",
        if operator.isMappingType(data):
            print "MAPPING",
        if operator.isNumberType(data):
            print "NUMBER",
        if operator.isSequenceType(data):
            print "SEQUENCE",
        print
            
    dump(0)
    dump("string")
    dump("string"[0])
    dump([1, 2, 3])
    dump((1, 2, 3))
    dump({"a": 1})
    dump(len) # function
    dump(UserList) # module
    dump(UserList.UserList) # class
    dump(UserList.UserList()) # instance
    


.. sourcecode:: python

    
     => NUMBER
     => SEQUENCE
     => SEQUENCE
     => SEQUENCE
     => SEQUENCE
     => MAPPING
     => CALLABLE
     =>
     => CALLABLE
     => MAPPING NUMBER SEQUENCE




Note that the operator module doesn’t handle object instances in a
sane fashion. In other words, be careful when you use the
**isNumberType**, **isMappingType**, and **isSequenceType** functions.
It’s easy to make your code less flexible than it has to be.



Also note that a string sequence member (a character) is also a
sequence. If you’re writing a recursive function that uses
**isSequenceType** to traverse an object tree, you better not pass it
an ordinary string (or anything containing one).


