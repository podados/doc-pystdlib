






The traceback module
=====================




This module allows you to print exception tracebacks inside your
programs, just like the interpreter does when you don’t catch an
exception yourself.

**Example: Using the traceback module to print a traceback**

.. sourcecode:: python

    
    # File: `traceback-example-1.py <traceback-example-1.py>`__
    
    # note! in old Python versions, importing the traceback
    # messes up the exception state.  to be on the safe side,
    # let's import it here.
    import traceback
    
    try:
        raise SyntaxError, "example"
    except:
        traceback.print_exc()
    


.. sourcecode:: python

    
    Traceback (innermost last):
      File "traceback-example-1.py", line 9, in ?
    SyntaxError: example




To put the traceback in a string, use the **StringIO** module:

**Example: Using the traceback module to copy a traceback to a
string**

.. sourcecode:: python

    
    # File: `traceback-example-2.py <traceback-example-2.py>`__
    
    import traceback
    import StringIO
    
    try:
        raise IOError, "an i/o error occurred"
    except:
        fp = StringIO.StringIO()
        traceback.print_exc(file=fp)
        message = fp.getvalue()
    
        print "failure! the error was:", repr(message)
    


.. sourcecode:: python

    
    failure! the error was: 'Traceback (innermost last):\012  File
    "traceback-example-2.py", line 5, in ?\012IOError: an i/o error
    occurred\012'




If you wish to format the traceback in a non-standard way, you can use
the **extract_tb** function to convert a traceback object to a list of
stack entries:


**Example: Using the traceback module to decode a traceback object**

.. sourcecode:: python

    
    # File: `traceback-example-3.py <traceback-example-3.py>`__
    
    import traceback
    import sys
    
    def function():
        raise IOError, "an i/o error occurred"
    
    try:
        function()
    except:
        info = sys.exc_info()
        for file, lineno, function, text in traceback.extract_tb(info[2]):
            print file, "line", lineno, "in", function
            print "=>", repr(text)
        print "** %s: %s" % info[:2]


.. sourcecode:: python

    
    traceback-example-3.py line 8 in ?
    => 'function()'
    traceback-example-3.py line 5 in function
    => 'raise IOError, "an i/o error occurred"'
    ** exceptions.IOError: an i/o error occurred


