






The urlparse module
====================




This module contains functions to process uniform resource locators
(URLs), and to convert between URLs and platform-specific filenames.


**Example: Using the urlparse module**

.. sourcecode:: python

    
    # File: `urlparse-example-1.py <urlparse-example-1.py>`__
    
    import urlparse
    
    print urlparse.urlparse("http://host/path;params?query#fragment")
    


.. sourcecode:: python

    
    ('http', 'host', '/path', 'params', 'query', 'fragment')





A common use is to split an HTTP URLs into host and path components
(an HTTP request involves asking the host to return data identified by
the path):


**Example: Using the urlparse module to parse HTTP locators**

.. sourcecode:: python

    
    # File: `urlparse-example-2.py <urlparse-example-2.py>`__
    
    import urlparse
    
    scheme, host, path, params, query, fragment =\
            urlparse.urlparse("http://host/path;params?query#fragment")
    
    if scheme == "http":
        print "host", "=>", host
        if params:
            path = path + ";" + params
        if query:
            path = path + "?" + query
        print "path", "=>", path
    


.. sourcecode:: python

    
    host => host
    path => /path;params?query





Alternatively, you can use the **urlunparse** function to put the URL
back together again:


**Example: Using the urlparse module to parse HTTP locators**

.. sourcecode:: python

    
    # File: `urlparse-example-3.py <urlparse-example-3.py>`__
    
    import urlparse
    
    scheme, host, path, params, query, fragment =\
            urlparse.urlparse("http://host/path;params?query#fragment")
    
    if scheme == "http":
        print "host", "=>", host
        print "path", "=>", urlparse.urlunparse((None, None, path, params, query, None))
    


.. sourcecode:: python

    
    host => host
    path => /path;params?query





The **urljoin** function is used to combine an absolute URL with a
second, possibly relative URL:

**Example: Using the urlparse module to combine relative locators**

.. sourcecode:: python

    
    # File: `urlparse-example-4.py <urlparse-example-4.py>`__
    
    import urlparse
    
    base = "http://spam.egg/my/little/pony"
    
    for path in "/index", "goldfish", "../black/cat":
        print path, "=>", urlparse.urljoin(base, path)
    


.. sourcecode:: python

    
    /index => http://spam.egg/index
    goldfish => http://spam.egg/my/little/goldfish
    ../black/cat => http://spam.egg/my/black/cat



