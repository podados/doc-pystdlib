






The asynchat module
====================




This module is an extension to ` **asyncore** <asyncore>`__. It
provides additional support for line oriented protocols. It also
provides improved buffering support, via the **push** methods and the
“producer” mechanism.



To configure the class, call the **set_terminator** method to specify
what terminator to use. The asyncore layer will then call
**collect_incoming_data** repeatedly, as data arrives, until it sees
the given terminator, and calls **found_terminator**.



To read a given number of bytes without checking for terminators (e.g.
a HTTP body), you can set the terminator to a byte count (an integer).
To disable the terminator check, set the terminator to **None**.



The following example implements a very minimal HTTP responder. It
simply returns a HTML document containing information from HTTP
request (the output appears in the browser window):


**Example: Using the asynchat module to implement a minimal HTTP
server**

.. sourcecode:: python

# File: `asynchat-example-1.py <asynchat-example-1.py>`__ import
asyncore, asynchat import os, socket, string PORT = 8000 class
HTTPChannel(asynchat.async_chat): def __init__(self, server, sock,
addr): asynchat.async_chat.__init__(self, sock)
self.set_terminator("\r\n") self.request = None self.data = ""
self.shutdown = 0 def collect_incoming_data(self, data): self.data =
self.data + data def found_terminator(self): if not self.request: #
got the request line self.request = string.split(self.data, None, 2)
if len(self.request) != 3: self.shutdown = 1 else: self.push("HTTP/1.0
200 OK\r\n") self.push("Content-type: text/html\r\n")
self.push("\r\n") self.data = self.data + "\r\n"
self.set_terminator("\r\n\r\n") # look for end of headers else: #
return payload. self.push("

.. sourcecode:: python

            \r\n")
                        self.push(self.data)
                        self.push("


     \r\n")             self.close_when_done()  class HTTPServer(asyncore.dispatcher):      def __init__(self, port):         asyncore.dispatcher.__init__(self)         self.create_socket(socket.AF_INET, socket.SOCK_STREAM)         self.bind(("", port))         self.listen(5)      def handle_accept(self):         conn, addr = self.accept()         HTTPChannel(self, conn, addr)  # # try it out  s = HTTPServer(PORT) print "serving at port", PORT, "..." asyncore.loop() 


.. sourcecode:: python

    
    GET / HTTP/1.1
    Accept: */*
    Accept-Language: en, sv
    Accept-Encoding: gzip, deflate
    User-Agent: Mozilla/4.0 (compatible; Bruce/1.0)
    Host: localhost:8000
    Connection: Keep-Alive





The producer interface allows you to “push” objects that are too
large to store in memory. **asyncore** calls the producer’s **more**
method whenever it needs more data. To signal end of file, just return
an empty string.



The following example implements a very simple file-based HTTP server,
using a simple **FileProducer** class that reads data from a file, a
few kilobytes at the time.


**Example: Using the asynchat module to implement a simple HTTP
server**

.. sourcecode:: python

# File: `asynchat-example-2.py <asynchat-example-2.py>`__ import
asyncore, asynchat import os, socket, string, sys import StringIO,
mimetools ROOT = "." PORT = 8000 class
HTTPChannel(asynchat.async_chat): def __init__(self, server, sock,
addr): asynchat.async_chat.__init__(self, sock) self.server = server
self.set_terminator("\r\n\r\n") self.header = None self.data = ""
self.shutdown = 0 def collect_incoming_data(self, data): self.data =
self.data + data if len(self.data) > 16384: # limit the header size to
prevent attacks self.shutdown = 1 def found_terminator(self): if not
self.header: # parse http header fp = StringIO.StringIO(self.data)
request = string.split(fp.readline(), None, 2) if len(request) != 3: #
badly formed request; just shut down self.shutdown = 1 else: # parse
message header self.header = mimetools.Message(fp)
self.set_terminator("\r\n") self.server.handle_request( self,
request[0], request[1], self.header ) self.close_when_done() self.data
= "" else: pass # ignore body data, for now def pushstatus(self,
status, explanation="OK"): self.push("HTTP/1.0 %d %s\r\n" % (status,
explanation)) class FileProducer: # a producer which reads data from a
file object def __init__(self, file): self.file = file def more(self):
if self.file: data = self.file.read(2048) if data: return data
self.file = None return "" class HTTPServer(asyncore.dispatcher): def
__init__(self, port=None, request=None):
asyncore.dispatcher.__init__(self) if not port: port = 80 self.port =
port if request: self.handle_request = request # external request
handler self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
self.bind(("", port)) self.listen(5) def handle_accept(self): conn,
addr = self.accept() HTTPChannel(self, conn, addr) def
handle_request(self, channel, method, path, header): try: # this is
not safe! while path[:1] == "/": path = path[1:] filename =
os.path.join(ROOT, path) print path, "=>", filename file =
open(filename, "r") except IOError: channel.pushstatus(404, "Not
found") channel.push("Content-type: text/html\r\n")
channel.push("\r\n") channel.push("File not found.
    \r\n")
            else:
                channel.pushstatus(200, "OK")
                channel.push("Content-type: text/html\r\n")
                channel.push("\r\n")
                channel.push_with_producer(FileProducer(file))
    
    #
    # try it out
    
    s = HTTPServer(PORT)
    print "serving at port", PORT
    asyncore.loop()
    


.. sourcecode:: python

    
    serving at port 8000
    log: adding channel 
    log: adding channel 
    samples/sample.htm => .\samples/sample.htm
    log: closing channel 96:





**Note:** In Python 2.4 and later, you must call the parent’s
**__init__** method when you subclass from **asyncore.dispatcher**. In
earlier versions, that call is optional.


