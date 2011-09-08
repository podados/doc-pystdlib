






The nntplib module
===================




This module provides a Network News Transfer Protocol (NNTP) client
implementation.



Listing messages
~~~~~~~~~~~~~~~~


Prior to reading messages from a news server, you have to connect to
the server, and then select a newsgroup. The following script also
downloads a complete list of all messages on the server, and extracts
some more or less interesting statistics from that list:


**Example: Using the nntplib module to list messages**

.. sourcecode:: python

    
    # File: `nntplib-example-1.py <nntplib-example-1.py>`__
    
    import nntplib
    import string
    
    SERVER = "news.spam.egg"
    GROUP  = "comp.lang.python" 
    AUTHOR = "fredrik@pythonware.com" # eff-bots human alias
    
    # connect to server
    server = nntplib.NNTP(SERVER)
    
    # choose a newsgroup
    resp, count, first, last, name = server.group(GROUP)
    print "count", "=>", count
    print "range", "=>", first, last
    
    # list all items on the server
    resp, items = server.xover(first, last)
    
    # extract some statistics
    authors = {}
    subjects = {}
    for id, subject, author, date, message_id, references, size, lines in items:
        authors[author] = None
        if subject[:4] == "Re: ":
            subject = subject[4:]
        subjects[subject] = None
        if string.find(author, AUTHOR) >= 0:
            print id, subject
        
    print "authors", "=>", len(authors)
    print "subjects", "=>", len(subjects)


.. sourcecode:: python

    
    count => 607
    range => 57179 57971
    57474 Three decades of Python!
    ...
    57477 More Python books coming...
    authors => 257
    subjects => 200





Downloading messages
~~~~~~~~~~~~~~~~~~~~


Downloading a message is easy. Just call the **article** method, as
shown in this script:


**Example: Using the nntplib module to download messages**

.. sourcecode:: python

    
    # File: `nntplib-example-2.py <nntplib-example-2.py>`__
    
    import nntplib
    import string
    
    SERVER = "news.spam.egg"
    GROUP  = "comp.lang.python" 
    KEYWORD = "tkinter"
    
    # connect to server
    server = nntplib.NNTP(SERVER)
    
    resp, count, first, last, name = server.group(GROUP)
    resp, items = server.xover(first, last)
    for id, subject, author, date, message_id, references, size, lines in items:
        if string.find(string.lower(subject), KEYWORD) >= 0:
            resp, id, message_id, text = server.article(id)
            print author
            print subject
            print len(text), "lines in article"
    


.. sourcecode:: python

    
    "Fredrik Lundh" 
    Re: Programming Tkinter (In Python)
    110 lines in article
    ...





To further manipulate the messages, you can wrap it up in a
**Message** object (using the **rfc822** module):


**Example: Using the nntplib and rfc822 modules to process messages**

.. sourcecode:: python

    
    # File: `nntplib-example-3.py <nntplib-example-3.py>`__
    
    import nntplib
    import string, random
    import StringIO, rfc822
    
    SERVER = "news.spam.egg"
    GROUP  = "comp.lang.python"
    
    # connect to server
    server = nntplib.NNTP(SERVER)
    
    resp, count, first, last, name = server.group(GROUP)
    for i in range(10):
        try:
            id = random.randint(int(first), int(last))
            resp, id, message_id, text = server.article(str(id))
        except (nntplib.error_temp, nntplib.error_perm):
            pass # no such message (maybe it was deleted?)
        else:
            break # found a message!
    else:
        raise SystemExit
    
    text = string.join(text, "\n")
    file = StringIO.StringIO(text)
    
    message = rfc822.Message(file)
    
    for k, v in message.items():
        print k, "=", v
    
    print message.fp.read()


.. sourcecode:: python

    
    mime-version = 1.0
    content-type = text/plain; charset="iso-8859-1"
    message-id = <008501bf1417$1cf90b70$f29b12c2@sausage.spam.egg>
    lines = 22
    ...
    from = "Fredrik Lundh" 
    nntp-posting-host = parrot.python.org
    subject = ANN: (the eff-bot guide to) The Standard Python Library
    ...
    





Once you’ve gotten this far, you can use modules like` **htmllib**
<htmllib.htm>`__,` **uu** <uu.htm>`__, and` **base64** <base64.htm>`__
to further process the messages.


