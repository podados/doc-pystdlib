






The httplib module
===================




This module provides an HTTP client interface.

**Example: Using the httplib module**

.. sourcecode:: python

    
    # File: `httplib-example-1.py <httplib-example-1.py>`__
    
    import httplib
    
    USER_AGENT = "httplib-example-1.py"
    
    class Error:
        # indicates an HTTP error
        def __init__(self, url, errcode, errmsg, headers):
            self.url = url
            self.errcode = errcode
            self.errmsg = errmsg
            self.headers = headers
        def __repr__(self):
            return (
                "" %
                (self.url, self.errcode, self.errmsg)
                )
    
    class Server:
    
        def __init__(self, host):
            self.host = host
    
        def fetch(self, path):
            http = httplib.HTTP(self.host)
    
            # write header
            http.putrequest("GET", path)
            http.putheader("User-Agent", USER_AGENT)
            http.putheader("Host", self.host)
            http.putheader("Accept", "*/*")
            http.endheaders()
    
            # get response
            errcode, errmsg, headers = http.getreply()
    
            if errcode != 200:
                raise Error(errcode, errmsg, headers)
    
            file = http.getfile()
            return file.read()
    
    if __name__ == "__main__":
    
        server = Server("www.pythonware.com")
        print server.fetch("/index.htm")




Note that the HTTP client provided by this module blocks while waiting
for the server to respond. For an asynchronous solution, which among
other things allows you to issue multiple requests in parallel, see
the examples for the **`asyncore <asyncore.htm>`__** module.



Posting data to an HTTP server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


The **httplib** module also allows you to send other HTTP commands,
such as **POST**.


**Example: Using the httplib module to post data**

.. sourcecode:: python

    
    # File: `httplib-example-2.py <httplib-example-2.py>`__
    
    import httplib
    
    USER_AGENT = "httplib-example-2.py"
    
    def post(host, path, data, type=None):
    
        http = httplib.HTTP(host)
    
        # write header
        http.putrequest("PUT", path)
        http.putheader("User-Agent", USER_AGENT)
        http.putheader("Host", host)
        if type:
            http.putheader("Content-Type", type)
        http.putheader("Content-Length", str(len(data)))
        http.endheaders()
    
        # write body
        http.send(data)
    
        # get response
        errcode, errmsg, headers = http.getreply()
    
        if errcode != 200:
            raise Error(errcode, errmsg, headers)
    
        file = http.getfile()
        return file.read()
    
    if __name__ == "__main__":
    
        post("www.spam.egg", "/bacon.htm", "a piece of data", "text/plain")


