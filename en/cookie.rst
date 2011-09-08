






The Cookie module
==================




(New in 2.0). This module provides basic cookie support for HTTP
clients and servers.

**Example: Using the cookie module**

.. sourcecode:: python

    
    # File: `cookie-example-1.py <cookie-example-1.py>`__
    
    import Cookie
    import os, time
    
    cookie = Cookie.SimpleCookie()
    cookie["user"] = "Mimi"
    cookie["timestamp"] = time.time()
    
    print cookie
    
    # simulate CGI roundtrip
    os.environ["HTTP_COOKIE"] = str(cookie)
    
    print
    
    cookie = Cookie.SmartCookie()
    cookie.load(os.environ["HTTP_COOKIE"])
    
    for key, item in cookie.items():
        # dictionary items are "Morsel" instances
        # use value attribute to get actual value
        print key, repr(item.value)


.. sourcecode:: python

    
    Set-Cookie: timestamp=736513200;
    Set-Cookie: user=Mimi;
    
    user 'Mimi'
    timestamp '736513200'



