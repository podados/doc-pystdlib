






The select module
==================




This module allows you to check for incoming data on one or more
sockets, pipes, or other compatible stream objects.



You can pass one or more sockets to the **select** function, to wait
for them to become readable, writable, or signal an error.



+
A socket becomes ready for reading when 1) someone connects after a
call to **listen** (which means that **accept** won’t block), or 2)
data arrives from the remote end, or 3) the socket is closed or reset
(in this case, **recv** will return an empty string).

+
A socket becomes ready for writing when 1) the connection is
established after a non-blocking call to **connect**, or 2) data can
be written to the socket.

+
A socket signals an error condition when the connection fails after a
non-blocking call to **connect**.



**Example: Using the select module to wait for data arriving over
sockets**

.. sourcecode:: python

    
    # File: `select-example-1.py <select-example-1.py>`__
    
    import select
    import socket
    import time
    
    PORT = 8037
    
    TIME1970 = 2208988800L
    
    service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    service.bind(("", PORT))
    service.listen(1)
    
    print "listening on port", PORT
    
    while 1:
        is_readable = [service]
        is_writable = []
        is_error = []
        r, w, e = select.select(is_readable, is_writable, is_error, 1.0)
        if r:
            channel, info = service.accept()
            print "connection from", info
            t = int(time.time()) + TIME1970
            t = chr(t>>24&255) + chr(t>>16&255) + chr(t>>8&255) + chr(t&255)
            channel.send(t) # send timestamp
            channel.close() # disconnect
        else:
            print "still waiting"
    


.. sourcecode:: python

    
    listening on port 8037
    still waiting
    still waiting
    connection from ('127.0.0.1', 1469)
    still waiting
    connection from ('127.0.0.1', 1470)
    ...





In this example, we wait for the listening socket to become readable,
which indicates that a connection request has arrived. We treat the
channel socket as usual, since it’s not very likely that writing the
four bytes will fill the network buffers. If you need to send larger
amounts of data to the client, you should add it to the
**is_writable** list at the top of the loop, and write only when
**select** tells you to.



If you set the socket in non-blocking mode (by calling the
**setblocking** method), you can use **select** also to wait for a
socket to become connected. But the **`asyncore <asyncore.htm>`__**
module (see the next section) provides a powerful framework which
handles all this for you, so I won’t go into further details here.


