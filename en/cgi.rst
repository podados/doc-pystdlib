






The cgi module
===============




This module provides a number of support functions and classes for
common gateway interface (CGI) scripts. Among other things, it can
parse CGI form data.



Here’s a simple CGI script that returns a list of a files in a given
directory (relative to the root directory specified in the script).


**Example: Using the cgi module**

.. sourcecode:: python

# File: `cgi-example-1.py <cgi-example-1.py>`__ import cgi import os,
urllib ROOT = "samples" # header print "text/html" print query =
os.environ.get("QUERY_STRING") if not query: query = "." script =
os.environ.get("SCRIPT_NAME", "") if not script: script = "cgi-
example-1.py" print "" print "" print "" print "" print "" print ""
try: files = os.listdir(os.path.join(ROOT, query)) except os.error:
files = [] for file in files: link = cgi.escape(file) if
os.path.isdir(os.path.join(ROOT, query, file)): href = script + "?" +
os.path.join(query, file) print "
`%s <%s>`__" % (href, cgi.escape(link)) else: print "
%s" % link print "


    "
    print ""
    


.. sourcecode:: python

text/html
sample.gif
sample.gz
sample.netrc ...
sample.txt
sample.xml
sample~
`web <cgi-example-1.py?web>`__







    
    


