






The sha module
===============




This module provides an alternative way to calculate message
signatures. It’s similar to the ` **md5** <md5.htm>`__ module, but
generates 160-bit signatures instead.


**Example: Using the sha module**

.. sourcecode:: python

    
    # File: `sha-example-1.py <sha-example-1.py>`__
    
    import sha
    
    hash = sha.new()
    hash.update("spam, spam, and eggs")
    
    print repr(hash.digest())
    print hash.hexdigest()
    


.. sourcecode:: python

    
    '\321\333\003\026I\331\272-j\303\247\240\345\343Tvq\364\346\311'
    d1db031649d9ba2d6ac3a7a0e5e3547671f4e6c9





See the **`md5 <md5.htm>`__** examples for more ways to use message
signatures.


