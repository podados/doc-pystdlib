






The binascii module
====================




This module contains support functions for a number of encoding
modules, including **`base64 <base64.htm>`__**, **`binhex
<binhex.htm>`__**, and **`uu <uu.htm>`__**.



In 2.0 and newer, it also allows you to convert binary data to and
from hexadecimal strings.

**Example: Using the binascii module**

.. sourcecode:: python

    
    # File: `binascii-example-1.py <binascii-example-1.py>`__
    
    import binascii
    
    text = "hello, mrs teal"
    
    data = binascii.b2a_base64(text)
    text = binascii.a2b_base64(data)
    print text, "<=>", repr(data)
    
    data = binascii.b2a_uu(text)
    text = binascii.a2b_uu(data)
    print text, "<=>", repr(data)
    
    data = binascii.b2a_hqx(text)
    text = binascii.a2b_hqx(data)[0]
    print text, "<=>", repr(data)
    
    # 2.0 and newer
    data = binascii.b2a_hex(text)
    text = binascii.a2b_hex(data)
    print text, "<=>", repr(data)
    


.. sourcecode:: python

    
    $ python binascii-example-1.py
    hello, mrs teal <=> 'aGVsbG8sIG1ycyB0ZWFs\012'
    hello, mrs teal <=> '/:&5L;&\\L(<=> 'D\'9XE\'mX)\'ebFb"dC@'
    hello, mrs teal <=> '68656c6c6f2c206d7273207465616c'



