






The smtplib module
===================




This module provides a Simple Mail Transfer Protocol (SMTP) client
implementation. This protocol is used to send mail through Unix
mailservers.



To read mail, use the **`poplib <poplib.htm>`__** or **`imaplib
<imaplib.htm>`__** modules.

**Example: Using the smtplib module**

.. sourcecode:: python

    
    # File: `smtplib-example-1.py <smtplib-example-1.py>`__
    
    import smtplib
    import string, sys
    
    HOST = "localhost"
    
    FROM = "effbot@spam.egg"
    TO = "fredrik@spam.egg"
    
    SUBJECT = "for your information!"
    
    BODY = "next week: how to fling an otter"
    
    body = string.join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT,
        "",
        BODY), "\r\n")
    
    print body
    
    server = smtplib.SMTP(HOST)
    server.sendmail(FROM, [TO], body)
    server.quit()
    


.. sourcecode:: python

    
    From: effbot@spam.egg
    To: fredrik@spam.egg
    Subject: for your information!
    
    next week: how to fling an otter




Note that the From and To headers in the message body are ignored by
the SMTP layer; they’re (usually) displayed by the receiver’s mail
client, but the SMTP layer uses the arguments passed to **sendmail**
to control message routing. Also note that the second argument must be
a list or other sequence; you can pass in multiple addresses to send
the same message to more than one receiver.


