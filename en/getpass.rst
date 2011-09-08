






The getpass module
===================




This module provides a platform-independent way to enter a password in
a command-line program.



**getpass(prompt) ⇒ string** prints the prompt string, switches off
keyboard echo, and reads a password. If the prompt argument is
omitted, it prints “ **Password: **”



**getuser() ⇒ string** gets the current username, if possible.

**Example: Using the getpass module**

.. sourcecode:: python

    
    # File: `getpass-example-1.py <getpass-example-1.py>`__
    
    import getpass
    
    usr = getpass.getuser()
    
    pwd = getpass.getpass("enter password for user %s: " % usr)
    
    print usr, pwd
    


.. sourcecode:: python

    
    enter password for user mulder:
    mulder trustno1



