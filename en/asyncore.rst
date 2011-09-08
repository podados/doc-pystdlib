






The asyncore module
====================




This module provides a “reactive” socket implementation. Instead
of creating socket objects, and calling methods on them to do things,
this module lets you write code that is called when something can be
done. To implement an asynchronous socket handler, subclass the
**dispatcher** class, and override one or more of the following
methods:



+
**writable** is called by the asyncore framework to check if the
dispatcher has data to send. The default implementation always returns
True.

+
**readable** is called to check if the dispatcher is ready to process
incoming data, if any. The default implementation always returns True.

+
**handle_connect** is called when a connection is successfully
established.

+
**handle_expt** is called when a connection fails (Windows), or when
out-of-band data arrives (Unix).

+
**handle_accept** is called when a connection request is made to a
listening socket. The callback should call the **accept** method to
get the client socket. In most cases, the callback should create
another socket handler to handle the actual communication.

+
**handle_read** is called when there is data waiting to be read from
the socket. The callback should call the **recv** method to get the
data.

+
**handle_write** is called when data can be written to the socket. Use
the **send** method to write data.

+
**handle_close** is called when the socket is closed or reset.

+
**handle_error(type, value, traceback)** is called if a Python error
occurs in any of the other callbacks. The default implementation
prints an abbreviated traceback to **sys.stdout**.




The first example shows a time client, similar to the one for the
**socket** module:


**Example: Using the asyncore module to get the time from a time
server**

.. sourcecode:: python

    
    # File: `asyncore-example-1.py <asyncore-example-1.py>`__
    
    import asyncore
    import socket, time
    
    # reference time (in seconds since 1900-01-01 00:00:00)
    TIME1970 = 2208988800L # 1970-01-01 00:00:00
    
    class TimeRequest(asyncore.dispatcher):
        # time requestor (as defined in RFC 868)
    
        def __init__(self, host, port=37):
            asyncore.dispatcher.__init__(self)
            self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connect((host, port))
    
        def writable(self):
            return 0 # don't have anything to write
    
        def handle_connect(self):
            pass # connection succeeded
    
        def handle_expt(self):
            self.close() # connection failed, shutdown
    
        def handle_read(self):
            # get local time
            here = int(time.time()) + TIME1970
    
            # get and unpack server time
            s = self.recv(4)
            there = ord(s[3]) + (ord(s[2])<<8) + (ord(s[1])<<16) + (ord(s[0])<<24L)
    
            self.adjust_time(int(here - there))
    
            self.handle_close() # we don't expect more data
    
        def handle_close(self):
            self.close()
    
        def adjust_time(self, delta):
            # override this method!
            print "time difference is", delta
    
    #
    # try it out
    
    request = TimeRequest("www.python.org")
    
    asyncore.loop()
    


.. sourcecode:: python

    
    log: adding channel 
    time difference is 28
    log: closing channel 192:





If you don’t want the log messages, override the **log** method in
your **dispatcher** subclass.



Here’s the corresponding time server. Note that it uses two
**dispatcher** subclasses, one for the listening socket, and one for
the client channel.


**Example: Using the asyncore module to implement a time server**

.. sourcecode:: python

    
    # File: `asyncore-example-2.py <asyncore-example-2.py>`__
    
    import asyncore
    import socket, time
    
    # reference time
    TIME1970 = 2208988800L
    
    class TimeChannel(asyncore.dispatcher):
    
        def handle_write(self):
            t = int(time.time()) + TIME1970
            t = chr(t>>24&255) + chr(t>>16&255) + chr(t>>8&255) + chr(t&255)
            self.send(t)
            self.close()
    
    class TimeServer(asyncore.dispatcher):
    
        def __init__(self, port=37):
            asyncore.dispatcher.__init__(self)
            self.port = port
            self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
            self.bind(("", port))
            self.listen(5)
            print "listening on port", self.port
    
        def handle_accept(self):
            channel, addr = self.accept()
            TimeChannel(channel)
    
    server = TimeServer(8037)
    asyncore.loop()
    


.. sourcecode:: python

    
    log: adding channel 
    listening on port 8037
    log: adding channel 
    log: closing channel 52:





In addition to the plain **dispatcher**, this module also includes a
**dispatcher_with_send** class. This class allows you send larger
amounts of data, without clogging up the network transport buffers.



The following module defines an **AsyncHTTP** class based on the
**dispatcher_with_send** class. When you create an instance of this
class, it issues an HTTP GET request, and sends the incoming data to a
“consumer” target object.


**Example: Using the asyncore module to do HTTP requests**

.. sourcecode:: python

    
    # File: `SimpleAsyncHTTP.py <SimpleAsyncHTTP.py>`__
    
    import asyncore
    import string, socket
    import StringIO
    import mimetools, urlparse
    
    class AsyncHTTP(asyncore.dispatcher_with_send):
        # HTTP requestor
    
        def __init__(self, uri, consumer):
            asyncore.dispatcher_with_send.__init__(self)
    
            self.uri = uri
            self.consumer = consumer
    
            # turn the uri into a valid request
            scheme, host, path, params, query, fragment = urlparse.urlparse(uri)
            assert scheme == "http", "only supports HTTP requests"
            try:
                host, port = string.split(host, ":", 1)
                port = int(port)
            except (TypeError, ValueError):
                port = 80 # default port
            if not path:
                path = "/"
            if params:
                path = path + ";" + params
            if query:
                path = path + "?" + query
    
            self.request = "GET %s HTTP/1.0\r\nHost: %s\r\n\r\n" % (path, host)
    
            self.host = host
            self.port = port
    
            self.status = None
            self.header = None
    
            self.data = ""
    
            # get things going!
            self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connect((host, port))
    
        def handle_connect(self):
            # connection succeeded
            self.send(self.request)
    
        def handle_expt(self):
            # connection failed; notify consumer (status is None)
            self.close()
            try:
                http_header = self.consumer.http_header
            except AttributeError:
                pass
            else:
                http_header(self)
    
        def handle_read(self):
            data = self.recv(2048)
            if not self.header:
                self.data = self.data + data
                try:
                    i = string.index(self.data, "\r\n\r\n")
                except ValueError:
                    return # continue
                else:
                    # parse header
                    fp = StringIO.StringIO(self.data[:i+4])
                    # status line is "HTTP/version status message"
                    status = fp.readline()
                    self.status = string.split(status, " ", 2)
                    # followed by a rfc822-style message header
                    self.header = mimetools.Message(fp)
                    # followed by a newline, and the payload (if any)
                    data = self.data[i+4:]
                    self.data = ""
                    # notify consumer (status is non-zero)
                    try:
                        http_header = self.consumer.http_header
                    except AttributeError:
                        pass
                    else:
                        http_header(self)
                    if not self.connected:
                        return # channel was closed by consumer
    
            self.consumer.feed(data)
    
        def handle_close(self):
            self.consumer.close()
            self.close()





And here’s a simple script using that class:

**Example: Using the SimpleAsyncHTTP class**

.. sourcecode:: python

    
    # File: `asyncore-example-3.py <asyncore-example-3.py>`__
    
    import SimpleAsyncHTTP
    import asyncore
    
    class DummyConsumer:
        size = 0
    
        def http_header(self, request):
            # handle header
            if request.status is None:
                print "connection failed"
            else:
                print "status", "=>", request.status
                for key, value in request.header.items():
                    print key, "=", value
    
        def feed(self, data):
            # handle incoming data
            self.size = self.size + len(data)
    
        def close(self):
            # end of data
            print self.size, "bytes in body"
    
    #
    # try it out
    
    consumer = DummyConsumer()
    
    request = SimpleAsyncHTTP.AsyncHTTP(
        "http://www.pythonware.com",
        consumer
        )
    
    asyncore.loop()
    


.. sourcecode:: python

    
    log: adding channel 
    status => ['HTTP/1.1', '200', 'OK\015\012']
    server = Apache/Unix (Unix)
    content-type = text/html
    content-length = 3730
    ...
    3730 bytes in body
    log: closing channel 156:




Note that the consumer interface is designed to be compatible with the
**htmllib** and **xmllib** parsers. This allows you to parse HTML or
XML data on the fly. Note that the **http_header** method is optional;
if it isn’t defined, it’s simply ignored.



A problem with the above example is that it doesn’t work for
redirected resources. The following example adds an extra consumer
layer, which handles the redirection:

**Example: Using the SimpleAsyncHTTP class with redirection**

.. sourcecode:: python

    
    # File: `asyncore-example-4.py <asyncore-example-4.py>`__
    
    import SimpleAsyncHTTP
    import asyncore
    
    class DummyConsumer:
        size = 0
    
        def http_header(self, request):
            # handle header
            if request.status is None:
                print "connection failed"
            else:
                print "status", "=>", request.status
                for key, value in request.header.items():
                    print key, "=", value
    
        def feed(self, data):
            # handle incoming data
            self.size = self.size + len(data)
    
        def close(self):
            # end of data
            print self.size, "bytes in body"
    
    class RedirectingConsumer:
    
        def __init__(self, consumer):
            self.consumer = consumer
    
        def http_header(self, request):
            # handle header
            if request.status is None or\
               request.status[1] not in ("301", "302"):
                try:
                    http_header = self.consumer.http_header
                except AttributeError:
                    pass
                else:
                    return http_header(request)
            else:
                # redirect!
                uri = request.header["location"]
                print "redirecting to", uri, "..."
                request.close()
                SimpleAsyncHTTP.AsyncHTTP(uri, self)
    
        def feed(self, data):
            self.consumer.feed(data)
    
        def close(self):
            self.consumer.close()
    
    #
    # try it out
    
    consumer = RedirectingConsumer(DummyConsumer())
    
    request = SimpleAsyncHTTP.AsyncHTTP(
        "http://www.pythonware.com/library",
        consumer
        )
    
    asyncore.loop()
    


.. sourcecode:: python

    
    log: adding channel 
    redirecting to http://www.pythonware.com/library/ ...
    log: closing channel 48:
    log: adding channel 
    status => ['HTTP/1.1', '200', 'OK\015\012']
    server = Apache/Unix (Unix)
    content-type = text/html
    content-length = 387
    ...
    387 bytes in body
    log: closing channel 236:




If the server returns status 301 (permanent redirection) or 302
(temporary redirection), the redirecting consumer closes the current
request, and issues a new one for the new address. All other calls to
the consumer are delegated to the original consumer.


