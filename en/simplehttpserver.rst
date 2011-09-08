






The SimpleHTTPServer module
============================




This is a simple HTTP server that provides standard GET and HEAD
request handlers. The path name given by the client is interpreted as
a relative file name (relative to the current directory when the
server was started, that is).


**Example: Using the SimpleHTTPServer module**

.. sourcecode:: python

    
    # File: `simplehttpserver-example-1.py <simplehttpserver-example-1.py>`__
    
    import SimpleHTTPServer
    import SocketServer
    
    # minimal web server.  serves files relative to the
    # current directory.
    
    PORT = 8000
    
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    
    print "serving at port", PORT
    httpd.serve_forever()
    


.. sourcecode:: python

    
    $ python simplehttpserver-example-1.py
    serving at port 8000
    localhost - - [11/Oct/1999 15:07:44] code 403, message Directory listing
    not supported
    localhost - - [11/Oct/1999 15:07:44] "GET / HTTP/1.1" 403 -
    localhost - - [11/Oct/1999 15:07:56] "GET /samples/sample.htm HTTP/1.1" 200 -





The server ignores drive letters and relative path names (such as
‘..’). However, it does not implement any other access control
mechanisms, so be careful how you use it.



The second example implements a truly minimal web proxy. When sent to
a proxy, the HTTP requests should include the full URI for the target
server. This server uses **`urllib <urllib.htm>`__** to fetch data
from the target.

**Example: Using the SimpleHTTPServer module as a proxy**

.. sourcecode:: python

    
    # File: `simplehttpserver-example-2.py <simplehttpserver-example-2.py>`__
    
    # a truly minimal HTTP proxy
    
    import SocketServer
    import SimpleHTTPServer
    import urllib
    
    PORT = 1234
    
    class Proxy(SimpleHTTPServer.SimpleHTTPRequestHandler):
        def do_GET(self):
            self.copyfile(urllib.urlopen(self.path), self.wfile)
    
    httpd = SocketServer.ForkingTCPServer(('', PORT), Proxy)
    print "serving at port", PORT
    httpd.serve_forever()



