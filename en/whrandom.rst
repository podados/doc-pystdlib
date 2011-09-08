






The whrandom module
====================




This module provides a pseudo-random number generator (based on an
algorithm by Wichmann & Hill, 1982). Unless you need several
generators that do not share internal state (for example, in a multi-
threaded application), it’s better to use the functions in the
**`random <random.htm>`__** module instead.

**Example: Using the whrandom module**

.. sourcecode:: python

    
    # File: `whrandom-example-1.py <whrandom-example-1.py>`__
    
    import whrandom
    
    # same as random
    print whrandom.random()
    print whrandom.choice([1, 2, 3, 5, 9])
    print whrandom.uniform(10, 20)
    print whrandom.randint(100, 1000)
    


.. sourcecode:: python

    
    $ python whrandom-example-1.py
    0.113412062346
    1
    16.8778954689
    799




To create multiple generators, create instances of the **whrandom**
class:

**Example: Using the whrandom module to create multiple random
generators**

.. sourcecode:: python

    
    # File: `whrandom-example-2.py <whrandom-example-2.py>`__
    
    import whrandom
    
    # initialize all generators with the same seed
    rand1 = whrandom.whrandom(4,7,11)
    rand2 = whrandom.whrandom(4,7,11)
    rand3 = whrandom.whrandom(4,7,11)
    
    for i in range(5):
        print rand1.random(), rand2.random(), rand3.random()
    


.. sourcecode:: python

    
    $ python whrandom-example-2.py
    0.123993532536 0.123993532536 0.123993532536
    0.180951499518 0.180951499518 0.180951499518
    0.291924111809 0.291924111809 0.291924111809
    0.952048889363 0.952048889363 0.952048889363
    0.969794283643 0.969794283643 0.969794283643



