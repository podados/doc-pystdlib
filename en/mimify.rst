






The mimify module
==================




This module converts MIME encoded text messages from encoded formats
to plain text (typically ISO Latin), and back. It can be used as a
command line tool, and as a conversion filter for certain mail agents.


.. sourcecode:: python

    
    $ mimify.py -e raw-message mime-message
    $ mimify.py -d mime-message raw-message



It can also be used as a module, as shown in the following example:

**Example: Using the mimify module to decode a message**

.. sourcecode:: python

    
    # File: `mimify-example-1.py <mimify-example-1.py>`__
    
    import mimify
    import sys
    
    mimify.unmimify("samples/sample.msg", sys.stdout, 1)




Here’s a MIME message containing two parts, one encoded as quoted-
printable, and the other as base64. The third argument to **unmimify**
controls whether base64-encoded parts should be decoded or not.


.. sourcecode:: python

    
    MIME-Version: 1.0
    Content-Type: multipart/mixed; boundary='boundary'
    
    this is a multipart sample file.  the two
    parts both contain ISO Latin 1 text, with
    different encoding techniques.
    
    --boundary
    Content-Type: text/plain
    Content-Transfer-Encoding: quoted-printable
    
    sillmj=F6lke! blindstyre! medisterkorv!
    
    --boundary
    Content-Type: text/plain
    Content-Transfer-Encoding: base64
    
    a29tIG5lciBiYXJhLCBvbSBkdSB09nJzIQ==
    
    --boundary--



And here’s the decoded result. Much more readable, at least if you
know the language.


.. sourcecode:: python

    
    MIME-Version: 1.0
    Content-Type: multipart/mixed; boundary='boundary'
    
    this is a multipart sample file.  the two
    parts both contain ISO Latin 1 text, with
    different encoding techniques.
    
    --boundary
    Content-Type: text/plain
    
    sillmjölke! blindstyre! medisterkorv!
    
    --boundary
    Content-Type: text/plain
    
    kom ner bara, om du törs!



Encoding messages is as easy:

**Example: Using the mimify module to encode a message**

.. sourcecode:: python

    
    # File: `mimify-example-2.py <mimify-example-2.py>`__
    
    import mimify
    import StringIO, sys
    
    #
    # decode message into a string buffer
    
    file = StringIO.StringIO()
    
    mimify.unmimify("samples/sample.msg", file, 1)
    
    #
    # encode message from string buffer
    
    file.seek(0) # rewind
    
    mimify.mimify(file, sys.stdout)



