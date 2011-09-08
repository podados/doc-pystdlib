






The mailbox module
===================




This module contains code to deal with a number of different mailbox
formats (mostly Unix formats). Most mailbox formats simply store plain
`RFC 822-style messages <rfc822.htm>`__ in a long text file, using
some kind of separator line to tell one message from another.



The **next** method returns ` **rfc822.Message** <rfc822.htm>`__
instances, or None if there are no more messages.

**Example: Using the mailbox module**

.. sourcecode:: python

    
    # File: `mailbox-example-1.py <mailbox-example-1.py>`__
    
    import mailbox
    
    mb = mailbox.UnixMailbox(open("/var/spool/mail/effbot"))
    
    while 1:
        msg = mb.next()
        if not msg:
            break
        for k, v in msg.items():
            print k, "=", v
        body = msg.fp.read()
        print len(body), "bytes in body"
    


.. sourcecode:: python

    
    $ python mailbox-example-1.py
    subject = for he's a ...
    message-id = <199910150027.CAA03202@spam.egg>
    received = (from fredrik@pythonware.com)
     by spam.egg (8.8.7/8.8.5) id CAA03202
     for effbot; Fri, 15 Oct 1999 02:27:36 +0200
    from = Fredrik Lundh 
    date = Fri, 15 Oct 1999 12:35:36 +0200
    to = effbot@spam.egg
    1295 bytes in body







