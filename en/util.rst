






The util module
================




(Obsolete, 1.5.2 only). This module is included for backwards
compatibility only. New code should use the replacement constructs
shown in the examples below.



**remove(sequence, item)** removes the given item, if found in the
sequence.

**Example: Emulating the util module’s remove function**

.. sourcecode:: python

    
    # File: `util-example-1.py <util-example-1.py>`__
    
    def remove(sequence, item):
        if item in sequence:
            sequence.remove(item)




**readfile(filename) ⇒ string** reads the contents of a text file as
a single string.

**Example: Emulating the util module’s readfile function**

.. sourcecode:: python

    
    # File: `util-example-2.py <util-example-2.py>`__
    
    def readfile(filename):
        file = open(filename, "r")
        return file.read()




**readopenfile(file) ⇒ string** returns the contents of an open file
(or other file object).

**Example: Emulating the util module’s readopenfile function**

.. sourcecode:: python

    
    # File: `util-example-3.py <util-example-3.py>`__
    
    def readopenfile(file):
        return file.read()



