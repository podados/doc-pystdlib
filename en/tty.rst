






The tty module
===============




(Unix only). This module contains some utility functions for dealing
with tty devices. The following example shows how to switch the
terminal window over to “raw” mode, and back again.

**Example: Using the tty module**

.. sourcecode:: python

    
    # File: `tty-example-1.py <tty-example-1.py>`__
    
    import tty
    import os, sys
    
    fileno = sys.stdin.fileno()
    
    tty.setraw(fileno)
    print raw_input("raw input: ")
    
    tty.setcbreak(fileno)
    print raw_input("cbreak input: ")
    
    os.system("stty sane") # ...
    


.. sourcecode:: python

    
    raw input: this is raw input
    cbreak input: this is cbreak input



