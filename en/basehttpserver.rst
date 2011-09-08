






The BaseHTTPServer module
==========================




This is a basic framework for HTTP servers, built on top of the
**`SocketServer <socketserver.htm>`__** framework.



The following example generates a random message each time you reload
the page. The **path** variable contains the current URL, which you
can use to generate different contents for different URLs (as it
stands, the script returns an error page for anything but the root
path).

**Example: Using the BaseHTTPServer module**

.. sourcecode:: python

# File: `basehttpserver-example-1.py <basehttpserver-example-1.py>`__
import BaseHTTPServer import cgi, random, sys MESSAGES = [ "That's as
maybe, it's still a frog.", "Albatross! Albatross! Albatross!", "It's
Wolfgang Amadeus Mozart", "A pink form from Reading.", "Hello people,
and welcome to 'It's a Tree'" "I simply stare at the brick and it goes
to sleep.", ] class Handler(BaseHTTPServer.BaseHTTPRequestHandler):
def do_GET(self): if self.path != "/": self.send_error(404, "File not
found") return self.send_response(200) self.send_header("Content-
type", "text/html") self.end_headers() try: # redirect stdout to
client stdout = sys.stdout sys.stdout = self.wfile self.makepage()
finally: sys.stdout = stdout # restore def makepage(self): # generate
a random message tagline = random.choice(MESSAGES) print "" print ""
print "
Today's quote: " print "%s" % cgi.escape(tagline) print "

    "
            print ""
    
    PORT = 8000
    
    httpd = BaseHTTPServer.HTTPServer(("", PORT), Handler)
    print "serving at port", PORT
    httpd.serve_forever()




See the **`SimpleHTTPServer <simplehttpserver.htm>`__** and
**`CGIHTTPServer <cgihttpserver.htm>`__** modules for more extensive
HTTP frameworks.


