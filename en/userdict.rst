






The UserDict module
====================




This module contains a dictionary class which can be subclassed
(it’s actually a Python wrapper for the built-in dictionary type).



The following example shows an enhanced dictionary class, which allows
dictionaries to be ‘added’ to each other, and be initialized using
the keyword argument syntax.

**Example: Using the UserDict module**

.. sourcecode:: python

    
    # File: `userdict-example-1.py <userdict-example-1.py>`__
    
    import UserDict
    
    class FancyDict(UserDict.UserDict):
    
        def __init__(self, data = {}, **kw):
            UserDict.UserDict.__init__(self)
            self.update(data)
            self.update(kw)
    
        def __add__(self, other):
            dict = FancyDict(self.data)
            dict.update(b)
            return dict
    
    a = FancyDict(a = 1)
    b = FancyDict(b = 2)
    
    print a + b
    


.. sourcecode:: python

    
    {'b': 2, 'a': 1}



