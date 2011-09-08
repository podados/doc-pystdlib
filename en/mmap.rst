






The mmap module
================




(New in 2.0) This module provides an interface to the operating
system’s memory mapping functions. The mapped region behaves pretty
much like a string object, but data is read directly from the file.

**Example: Using the mmap module**

.. sourcecode:: python

    
    # File: `mmap-example-1.py <mmap-example-1.py>`__
    
    import mmap
    import os
    
    filename = "samples/sample.txt"
    
    file = open(filename, "r+")
    size = os.path.getsize(filename)
    
    data = mmap.mmap(file.fileno(), size)
    
    # basics
    print data
    print len(data), size
    
    # use slicing to read from the file
    print repr(data[:10]), repr(data[:10])
    
    # or use the standard file interface
    print repr(data.read(10)), repr(data.read(10))
    


.. sourcecode:: python

    
    $ python mmap-example-1.py
    
    302 302
    'We will pe' 'We will pe'
    'We will pe' 'rhaps even'




Under Windows, the file must currently be opened for both reading and
writing ( **r+**, or **w+**), or the **mmap** call will fail.



Memory mapped regions can be used instead of ordinary strings in many
places, including regular expressions and many string operations:

**Example: Using string functions and regular expressions on a mapped
region**

.. sourcecode:: python

    
    # File: `mmap-example-2.py <mmap-example-2.py>`__
    
    import mmap
    import os, string, re
    
    def mapfile(filename):
        file = open(filename, "r+")
        size = os.path.getsize(filename)
        return mmap.mmap(file.fileno(), size)
    
    data = mapfile("samples/sample.txt")
    
    # search
    index = data.find("small")
    print index, repr(data[index-5:index+15])
    
    # regular expressions work too!
    m = re.search("small", data)
    print m.start(), m.group()
    


.. sourcecode:: python

    
    $ python mmap-example-2.py
    43 'only small\015\012modules '
    43 small



