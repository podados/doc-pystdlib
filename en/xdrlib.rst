






The xdrlib module
==================




This module converts between Python data types and Sun’s external
data representation (XDR).

**Example: Using the xdrlib module**

.. sourcecode:: python

    
    # File: `xdrlib-example-1.py <xdrlib-example-1.py>`__
    
    import xdrlib
    
    #
    # create a packer and add some data to it
    
    p = xdrlib.Packer()
    p.pack_uint(1)
    p.pack_string("spam")
    
    data = p.get_buffer()
    
    print "packed:", repr(data)
    
    #
    # create an unpacker and use it to decode the data
    
    u = xdrlib.Unpacker(data)
    
    print "unpacked:", u.unpack_uint(), repr(u.unpack_string())
    
    u.done()
    


.. sourcecode:: python

    
    $ python xdrlib-example-1.py
    packed: '\000\000\000\001\000\000\000\004spam'
    unpacked: 1 'spam'




The XDR format is used by Sun’s remote procedure call (RPC)
protocol. Here’s an incomplete (and rather contrived) example
showing how to build an RPC request package:


**Example: Using the xdrlib module to send a RPC call package**

.. sourcecode:: python

    
    # File: `xdrlib-example-2.py <xdrlib-example-2.py>`__
    
    import xdrlib
    
    # some constants (see the RPC specs for details)
    RPC_CALL = 1
    RPC_VERSION = 2
    
    MY_PROGRAM_ID = 1234 # assigned by Sun
    MY_VERSION_ID = 1000
    MY_TIME_PROCEDURE_ID = 9999
    
    AUTH_NULL = 0
    
    transaction = 1
    
    p = xdrlib.Packer()
    
    # send an Sun RPC call package
    p.pack_uint(transaction)
    p.pack_enum(RPC_CALL)
    p.pack_uint(RPC_VERSION)
    p.pack_uint(MY_PROGRAM_ID)
    p.pack_uint(MY_VERSION_ID)
    p.pack_uint(MY_TIME_PROCEDURE_ID)
    p.pack_enum(AUTH_NULL)
    p.pack_uint(0)
    p.pack_enum(AUTH_NULL)
    p.pack_uint(0)
    
    print repr(p.get_buffer())
    


.. sourcecode:: python

    
    $ python xdrlib-example-2.py
    '\000\000\000\001\000\000\000\001\000\000\000\002\000\000\004\322
    \000\000\003\350\000\000\'\017\000\000\000\000\000\000\000\000\000
    \000\000\000\000\000\000\000'


