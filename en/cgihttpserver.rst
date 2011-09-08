






The CGIHTTPServer module
=========================




This is a simple HTTP server that can call external scripts through
the common gateway interface (CGI).

**Example: Using the CGIHTTPServer module**

.. sourcecode:: python

    
    # File: `cgihttpserver-example-1.py <cgihttpserver-example-1.py>`__
    
    import CGIHTTPServer
    import BaseHTTPServer
    
    class Handler(CGIHTTPServer.CGIHTTPRequestHandler):
        cgi_directories = ["/cgi"]
    
    PORT = 8000
    
    httpd = BaseHTTPServer.HTTPServer(("", PORT), Handler)
    print "serving at port", PORT
    httpd.serve_forever()



