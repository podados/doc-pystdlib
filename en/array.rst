






The array module
=================




This module implements an efficient array storage type. Arrays are
similar to lists, but all items must be of the same primitive type.
The type is defined when the array is created.



Here are some simple examples. The first example creates an **array**
object, and copies the internal buffer to a string through the
**tostring** method:


**Example: Using the array module to convert lists of integers to
strings**

.. sourcecode:: python

    
    # File: array-example-1.py
    import array
    
    a = array.array("B", range(16)) # unsigned char
    b = array.array("h", range(16)) # signed short
    print a
    print repr(a.tostring())
    
    print b
    print repr(b.tostring())


.. sourcecode:: python

    
    array('B', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    '\000\001\002\003\004\005\006\007\010\011\012\013\014\015\016\017'
    array('h', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    '\000\000\001\000\002\000\003\000\004\000\005\000\006\000\007\000
    \010\000\011\000\012\000\013\000\014\000\015\000\016\000\017\000'





The **array** objects can be treated as ordinary lists, to some
extent. You cannot concatenate arrays if they have different type
codes, though.

**Example: Using arrays as ordinary sequences**

.. sourcecode:: python

    
    # File: `array-example-2.py <array-example-2.py>`__
    
    import array
    
    a = array.array("B", [1, 2, 3])
    
    a.append(4)
    
    a = a + a
    
    a = a[2:-2]
    
    print a
    print repr(a.tostring())
    for i in a:
        print i,
    


.. sourcecode:: python

    
    array('B', [3, 4, 1, 2])
    '\003\004\001\002'
    3 4 1 2




This module also provides a very efficient way to turn raw binary data
into a sequence of integers (or floating point values, for that
matter):

**Example: Using arrays to convert strings to lists of integers**

.. sourcecode:: python

    
    # File: `array-example-3.py <array-example-3.py>`__
    
    import array
    
    a = array.array("i", "fish license") # signed integer
    
    print a
    print repr(a.tostring())
    print a.tolist()
    


.. sourcecode:: python

    
    array('i', [1752394086, 1667853344, 1702063717])
    'fish license'
    [1752394086, 1667853344, 1702063717]




Finally, here’s how to use this module to determine the endianess of
the current platform:

**Example: Using the array module to determine platform endianess**

.. sourcecode:: python

    
    # File: `array-example-4.py <array-example-4.py>`__
    
    import array
    
    def little_endian():
        return ord(array.array("i",[1]).tostring()[0])
    
    if little_endian():
        print "little-endian platform (intel, alpha)"
    else:
        print "big-endian platform (motorola, sparc)"
    


.. sourcecode:: python

    
    big-endian platform (motorola, sparc)




Python 2.0 and later provides a **sys.byteorder** attribute, which is
set to either “ **little**” or “ **big**” :

**Example: Using the sys.byteorder attribute to determine platform
endianess (Python 2.0)**

.. sourcecode:: python

    
    # File: `sys-byteorder-example-1.py <sys-byteorder-example-1.py>`__
    
    import sys
    
    # available in Python 2.0 and later
    if sys.byteorder == "little":
        print "little-endian platform (intel, alpha)"
    else:
        print "big-endian platform (motorola, sparc)"
    


.. sourcecode:: python

    
    'big-endian platform (motorola, sparc)'



