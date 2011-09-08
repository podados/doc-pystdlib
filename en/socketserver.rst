






The SocketServer module
========================




This module provides a framework for various kinds of socket-based
servers. The module provides a number of classes that can be mixed and
matched to create servers for different purposes.



The following example implements an Internet Time Protocol server,
using this module. Use the **timeclient** script to try it out:


**Example: Using the SocketServer module**

.. sourcecode:: python

    
    # File: `socketserver-example-1.py <socketserver-example-1.py>`__
    
    import SocketServer
    import time
    
    # user-accessible port
    PORT = 8037
    
    # reference time
    TIME1970 = 2208988800L
    
    class TimeRequestHandler(SocketServer.StreamRequestHandler):
        def handle(self):
            print "connection from", self.client_address
            t = int(time.time()) + TIME1970
            b = chr(t>>24&255) + chr(t>>16&255) + chr(t>>8&255) + chr(t&255)
            self.wfile.write(b)
    
    server = SocketServer.TCPServer(("", PORT), TimeRequestHandler)
    print "listening on port", PORT
    server.serve_forever()
    


.. sourcecode:: python

    
    connection from ('127.0.0.1', 1488)
    connection from ('127.0.0.1', 1489)
    ...


