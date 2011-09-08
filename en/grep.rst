






The grep module
================




(Obsolete; removed in 2.0) This module provides different ways to
search for text in text files.



The **grep** function takes a regular expression (using the old
**regex** syntax, and a list of files to search.

**Example: Using the grep module**

.. sourcecode:: python

    
    # File: `grep-example-1.py <grep-example-1.py>`__
    
    import grep
    import glob
    
    grep.grep("\", glob.glob("samples/*.txt"))


.. sourcecode:: python

    
    $ python grep-example-1.py
    4: indentation, rather than delimiters, might become



