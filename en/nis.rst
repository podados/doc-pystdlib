






The nis module
===============




(Unix only, Optional). This module provides an interface to the NIS
(yellow pages) services. It can be used to fetch values from a NIS
database, if available.

**Example: Using the nis module**

.. sourcecode:: python

    
    # File: `nis-example-1.py <nis-example-1.py>`__
    
    import nis
    import string
    
    print nis.cat("ypservers")
    print string.split(nis.match("bacon", "hosts.byname"))


.. sourcecode:: python

    
    $ python nis-example-1.py
    {'bacon.spam.egg': 'bacon.spam.egg'}
    ['194.18.155.250', 'bacon.spam.egg', 'bacon', 'spam-010']



