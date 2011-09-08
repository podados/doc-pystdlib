






The math module
================




This module implements a number of mathematical operations for
floating point numbers. The functions are generally thin wrappers
around the platform C library functions of the same name, so results
may vary slightly across platforms in normal cases, or vary a lot in
exceptional cases.



The ` **cmath** <cmath.htm>`__ module provides similar functionality
for complex numbers.

**Example: Using the math module**

.. sourcecode:: python

    
    # File: `math-example-1.py <math-example-1.py>`__
    
    import math
    
    print "e", "=>", math.e
    print "pi", "=>", math.pi
    print "hypot", "=>", math.hypot(3.0, 4.0)
    
    # and many others...


.. sourcecode:: python

    
    $ python math-example-1.py
    e => 2.71828182846
    pi => 3.14159265359
    hypot => 5.0




See the Python Library Reference for a full list of functions.


