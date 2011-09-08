






The mimetools module
=====================




The Multipurpose Internet Mail Extensions (MIME) standard defines how
to store non-ASCII text, images, and other data in RFC 822-style
messages.



This module contains a number of tools for writing programs which read
or write MIME messages. Among other things, it contains a version of
the **rfc822** module’s **Message** class, which knows a bit more
about MIME encoded messages.

**Example: Using the mimetools module**

.. sourcecode:: python

    
    # File: `mimetools-example-1.py <mimetools-example-1.py>`__
    
    import mimetools
    
    file = open("samples/sample.msg")
    
    msg = mimetools.Message(file)
    
    print "type", "=>", msg.gettype()
    print "encoding", "=>", msg.getencoding()
    print "plist", "=>", msg.getplist()
    
    print "header", "=>"
    for k, v in msg.items():
        print "  ", k, "=", v
    


.. sourcecode:: python

    
    type => text/plain
    encoding => 7bit
    plist => ['charset="iso-8859-1"']
    header =>
       mime-version = 1.0
       content-type = text/plain;
     charset="iso-8859-1"
       to = effbot@spam.egg
       date = Fri, 15 Oct 1999 03:21:15 -0400
       content-transfer-encoding = 7bit
       from = "Fredrik Lundh" 
       subject = By the way...
    ...



