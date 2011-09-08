






The socket module
==================




This module implements an interface to the socket communication layer.
You can create both client and server sockets using this module.



Let’s start with a client example. The following client connects to
a time protocol server, reads the 4-byte response, and converts it to
a time value.

**Example: Using the socket module to implement a time client**

.. sourcecode:: python

    
    # File: `socket-example-1.py <socket-example-1.py>`__
    
    import socket
    import struct, time
    
    # server
    HOST = "www.python.org"
    PORT = 37
    
    # reference time (in seconds since 1900-01-01 00:00:00)
    TIME1970 = 2208988800L # 1970-01-01 00:00:00
    
    # connect to server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    
    # read 4 bytes, and convert to time value
    t = s.recv(4)
    t = struct.unpack("!I", t)[0]
    t = int(t - TIME1970)
    
    s.close()
    
    # print results
    print "server time is", time.ctime(t)
    print "local clock is", int(time.time()) - t, "seconds off"
    


.. sourcecode:: python

    
    server time is Sat Oct 09 16:42:36 1999
    local clock is 8 seconds off




The **socket** factory function creates a new socket of the given type
(in this case, an Internet stream socket, also known as a TCP socket).
The **connect** method attempts to connect this socket to the given
server. Once that has succeeded, the **recv** method is used to read
data.



Creating a server socket is done in a similar fashion. But instead of
connecting to a server, you **bind** the socket to a port on the local
machine, tell it to **listen** for incoming connection requests, and
process each request as fast as possible.



The following example creates a time server, bound to port 8037 on the
local machine (port numbers up to 1024 are reserved for system
services, and you have to have root privileges to use them to
implement services on a Unix system):

**Example: Using the socket module to implement a time server**

.. sourcecode:: python

    
    # File: `socket-example-2.py <socket-example-2.py>`__
    
    import socket
    import struct, time
    
    # user-accessible port
    PORT = 8037
    
    # reference time
    TIME1970 = 2208988800L
    
    # establish server
    service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    service.bind(("", PORT))
    service.listen(1)
    
    print "listening on port", PORT
    
    while 1:
        # serve forever
        channel, info = service.accept()
        print "connection from", info
        t = int(time.time()) + TIME1970
        t = struct.pack("!I", t)
        channel.send(t) # send timestamp
        channel.close() # disconnect
    


.. sourcecode:: python

    
    listening on port 8037
    connection from ('127.0.0.1', 1469)
    connection from ('127.0.0.1', 1470)
    ...




The **listen** call tells the socket that we’re willing to accept
incoming connections. The argument gives the size of the connection
queue (which holds connection requests that our program hasn’t
gotten around to processing yet). Finally, the **accept** loop returns
the current time to any client bold enough to connect.



Note that the **accept** function returns a new socket object, which
is directly connected to the client. The original socket is only used
to establish the connection; all further traffic goes via the new
socket.



To test this server, we can use the following generalized version of
our first example:

**Example: A time protocol client**

.. sourcecode:: python

    
    # File: `timeclient.py <timeclient.py>`__
    
    import socket
    import struct, sys, time
    
    # default server
    host = "localhost"
    port = 8037
    
    # reference time (in seconds since 1900-01-01 00:00:00)
    TIME1970 = 2208988800L # 1970-01-01 00:00:00
    
    def gettime(host, port):
        # fetch time buffer from stream server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        t = s.recv(4)
        s.close()
        t = struct.unpack("!I", t)[0]
        return int(t - TIME1970)
    
    if __name__ == "__main__":
        # command line utility
        if sys.argv[1:]:
            host = sys.argv[1]
            if sys.argv[2:]:
                port = int(sys.argv[2])
            else:
                port = 37 # default for public servers
    
        t = gettime(host, port)
        print "server time is", time.ctime(t)
        print "local clock is", int(time.time()) - t, "seconds off"
    


.. sourcecode:: python

    
    server time is Sat Oct 09 16:58:50 1999
    local clock is 0 seconds off




This sample script can also be used as a module; to get the current
time from a server, import the **timeclient** module, and call the
**gettime** function.



This far, we’ve used stream (or TCP) sockets. The time protocol
specification also mentions UDP sockets, or datagrams. Stream sockets
work pretty much like a phone line; you’ll know if someone at the
remote end picks up the receiver, and you’ll notice when she hangs
up. In contrast, sending datagrams is more like shouting into a dark
room. There might be someone there, but you won’t know unless she
replies.



You don’t need to connect to send data over a datagram socket.
Instead, you use the **sendto** method, which takes both the data and
the address of the receiver. To read incoming datagrams, use the
**recvfrom** method.

**Example: Using the socket module to implement a datagram time
client**

.. sourcecode:: python

    
    # File: `socket-example-4.py <socket-example-4.py>`__
    
    import socket
    import struct, time
    
    # server
    HOST = "localhost"
    PORT = 8037
    
    # reference time (in seconds since 1900-01-01 00:00:00)
    TIME1970 = 2208988800L # 1970-01-01 00:00:00
    
    # connect to server
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # send empty packet
    s.sendto("", (HOST, PORT))
    
    # read 4 bytes from server, and convert to time value
    t, server = s.recvfrom(4)
    t = struct.unpack("!I", t)[0]
    t = int(t - TIME1970)
    
    s.close()
    
    print "server time is", time.ctime(t)
    print "local clock is", int(time.time()) - t, "seconds off"
    


.. sourcecode:: python

    
    server time is Sat Oct 09 16:42:36 1999
    local clock is 8 seconds off




Note that **recvfrom** returns two values; the actual data, and the
address of the sender. Use the latter if you need to reply.



And here’s the corresponding server:

**Example: Using the socket module to implement a datagram time
server**

.. sourcecode:: python

    
    # File: `socket-example-5.py <socket-example-5.py>`__
    
    import socket
    import struct, time
    
    # user-accessible port
    PORT = 8037
    
    # reference time
    TIME1970 = 2208988800L
    
    # establish server
    service = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    service.bind(("", PORT))
    
    print "listening on port", PORT
    
    while 1:
        # serve forever
        data, client = service.recvfrom(0)
        print "connection from", client
        t = int(time.time()) + TIME1970
        t = struct.pack("!I", t)
        service.sendto(t, client) # send timestamp
    


.. sourcecode:: python

    
    listening on port 8037
    connection from ('127.0.0.1', 1469)
    connection from ('127.0.0.1', 1470)
    ...




The main difference is that the server uses **bind** to assign a known
port number to the socket, and sends data back to the client address
returned by **recvfrom**.


