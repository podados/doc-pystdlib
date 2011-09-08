






The urllib module
==================




This module provides a unified client interface for HTTP, FTP, and
gopher. It automatically picks the right protocol handler based on the
uniform resource locator (URL) passed to the library.



Fetching data from an URL is extremely easy. Just call the **urlopen**
method, and read from the returned stream object.

**Example: Using the urllib module to fetch a remote resource**

.. sourcecode:: python

    
    # File: `urllib-example-1.py <urllib-example-1.py>`__
    
    import urllib
    
    fp = urllib.urlopen("http://www.python.org")
    
    op = open("out.html", "wb")
    
    n = 0
    
    while 1:
        s = fp.read(8192)
        if not s:
            break
        op.write(s)
        n = n + len(s)
    
    fp.close()
    op.close()
    
    for k, v in fp.headers.items():
        print k, "=", v
    
    print "copied", n, "bytes from", fp.url
    


.. sourcecode:: python

    
    server = Apache/1.3.6 (Unix)
    content-type = text/html
    accept-ranges = bytes
    date = Mon, 11 Oct 1999 20:11:40 GMT
    connection = close
    etag = "741e9-7870-37f356bf"
    content-length = 30832
    last-modified = Thu, 30 Sep 1999 12:25:35 GMT
    copied 30832 bytes from http://www.python.org




Note that stream object provides some non-standard attributes.
**headers** is a **Message** object (as defined by the **mimetools**
module), and **url** contains the actual URL. The latter is updated if
the server redirects the client to a new URL.



The **urlopen** function is actually a helper function, which creates
an instance of the **FancyURLopener** class, and calls its **open**
method. To get special behavior, you can subclass that class. For
example, the following class automatically logs in to the server, when
necessary:

**Example: Using the urllib module with automatic authentication**

.. sourcecode:: python

    
    # File: `urllib-example-3.py <urllib-example-3.py>`__
    
    import urllib
    
    class myURLOpener(urllib.FancyURLopener):
        # read an URL, with automatic HTTP authentication
    
        def setpasswd(self, user, passwd):
            self.__user = user
            self.__passwd = passwd
    
        def prompt_user_passwd(self, host, realm):
            return self.__user, self.__passwd
    
    urlopener = myURLOpener()
    urlopener.setpasswd("mulder", "trustno1")
    
    fp = urlopener.open("http://www.secretlabs.com")
    print fp.read()



