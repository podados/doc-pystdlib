






The robotparser module
=======================




(New in 2.0). This module reads **robots.txt** files, which are used
to implement the ` Robot Exclusion Protocol
<http://info.webcrawler.com/mak/projects/robots/robots.html>`__.



If you’re implementing an HTTP robot that will visit arbitrary sites
on the net (not just your own sites), it’s a good idea to use this
module to check that you really are welcome.

**Example: Using the robotparser module**

.. sourcecode:: python

    
    # File: `robotparser-example-1.py <robotparser-example-1.py>`__
    
    import robotparser
    
    r = robotparser.RobotFileParser()
    r.set_url("http://www.python.org/robots.txt")
    r.read()
    
    if r.can_fetch("*", "/index.html"):
        print "may fetch the home page"
    
    if r.can_fetch("*", "/tim_one/index.html"):
        print "may fetch the tim peters archive"
    


.. sourcecode:: python

    
    $ python robotparser-example-1.py
    may fetch the home page



