






The webbrowser module
======================




(New in 2.0) This module provides a basic interface to the system’s
standard webrowser. It provides a **open** function, which takes a
file name or an URL, and displays it in the browser. If you call
**open** again, it attempts to display the new page in the same
browser window.

**Example: Using the webbrowser module**

.. sourcecode:: python

    
    # File: `webbrowser-example-1.py <webbrowser-example-1.py>`__
    
    import webbrowser
    import time
    
    webbrowser.open("http://www.pythonware.com")
    
    # wait a while, and then go to another page
    time.sleep(5)
    webbrowser.open(
        "http://www.pythonware.com/people/fredrik/librarybook.htm"
        )




On Unix, this module supports lynx, Netscape, Mosaic, Konquerer, and
Grail. On Windows and Macintosh, it uses the standard browser (as
defined in the registry or the Internet configuration panel).


