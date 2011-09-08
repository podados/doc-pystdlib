






The termios module
===================




(Unix only, Optional). This module provides an interface to the Unix
terminal control facilities. It can be used to control most aspects of
the terminal communication ports.



In the following example, this module is used to temporarily disable
keyboard echo (which is controlled by the **ECHO** flag in the third
flag field):

**Example: Using the termios module to disable keyboard echo**

.. sourcecode:: python

    
    # File: `termios-example-1.py <termios-example-1.py>`__
    
    import termios, TERMIOS
    import sys
    
    fileno = sys.stdin.fileno()
    
    attr = termios.tcgetattr(fileno)
    orig = attr[:]
    
    print "attr =>", attr[:4] # flags
    
    # disable echo flag
    attr[3] = attr[3] & ~TERMIOS.ECHO
    
    try:
        termios.tcsetattr(fileno, TERMIOS.TCSADRAIN, attr)
        message = raw_input("enter secret message: ")
        print
    finally:
        # restore terminal settings
        termios.tcsetattr(fileno, TERMIOS.TCSADRAIN, orig)
    
    print "secret =>", repr(message)
    


.. sourcecode:: python

    
    attr => [1280, 5, 189, 35387]
    enter secret message:
    secret => 'and now for something completely different'



