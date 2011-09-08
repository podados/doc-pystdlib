






The mimetypes module
=====================




This module contains support for determining the MIME type for a given
uniform resource locator. This is based on a built-in table, plus
Apache and Netscape configuration files, if they are found.

**Example: Using the mimetypes module**

.. sourcecode:: python

    
    # File: `mimetypes-example-1.py <mimetypes-example-1.py>`__
    
    import mimetypes
    import glob, urllib
    
    for file in glob.glob("samples/*"):
        url = urllib.pathname2url(file)
        print file, mimetypes.guess_type(url)
    


.. sourcecode:: python

    
    samples\sample.au ('audio/basic', None)
    samples\sample.ini (None, None)
    samples\sample.jpg ('image/jpeg', None)
    samples\sample.msg (None, None)
    samples\sample.tar ('application/x-tar', None)
    samples\sample.tgz ('application/x-tar', 'gzip')
    samples\sample.txt ('text/plain', None)
    samples\sample.wav ('audio/x-wav', None)
    samples\sample.zip ('application/zip', None)



