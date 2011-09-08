






The getopt module
==================




This module contains functions to extract command line options and
arguments. It can handle both short and long option formats.



The second argument specifies the short options that should be
allowed. A colon (:) after an option name means that option must have
an additional argument.

**Example: Using the getopt module**

.. sourcecode:: python

    
    # File: `getopt-example-1.py <getopt-example-1.py>`__
    
    import getopt
    import sys
    
    # simulate command line invocation
    sys.argv = ["myscript.py", "-l", "-d", "directory", "filename"]
    
    # process options
    opts, args = getopt.getopt(sys.argv[1:], "ld:")
    
    long = 0
    directory = None
    
    for o, v in opts:
        if o == "-l":
            long = 1
        elif o == "-d":
            directory = v
    
    print "long", "=", long
    print "directory", "=", directory
    print "arguments", "=", args


.. sourcecode:: python

    
    long = 1
    directory = directory
    arguments = ['filename']




To make it look for long options, pass a list of option descriptors as
the third argument. If an option name ends with an equal sign (=),
that option must have an additional argument.


**Example: Using the getopt module to handle long options**

.. sourcecode:: python

    
    # File: `getopt-example-2.py <getopt-example-2.py>`__
    
    import getopt
    import sys
    
    # simulate command line invocation
    sys.argv = ["myscript.py", "--echo", "--printer", "lp01", "message"]
    
    opts, args = getopt.getopt(sys.argv[1:], "ep:", ["echo", "printer="])
    
    # process options
    echo = 0
    printer = None
    
    for o, v in opts:
        if o in ("-e", "--echo"):
            echo = 1
        elif o in ("-p", "--printer"):
            printer = v
    
    print "echo", "=", echo
    print "printer", "=", printer
    print "arguments", "=", args


.. sourcecode:: python

    
    echo = 1
    printer = lp01
    arguments = ['message']


