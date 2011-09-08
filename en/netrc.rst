






The netrc module
=================




This module parses **.netrc** configuration files. Such files are used
to store FTP user names and passwords in a user’s home directory
(don’t forget to configure things so that the file can only be read
by the user: “ **chmod 0600 ~/.netrc**” , in other words).

**Example: Using the netrc module**

.. sourcecode:: python

    
    # File: `netrc-example-1.py <netrc-example-1.py>`__
    
    import netrc
    
    # default is $HOME/.netrc
    info = netrc.netrc("samples/sample.netrc")
    
    login, account, password = info.authenticators("secret.fbi")
    print "login", "=>", repr(login)
    print "account", "=>", repr(account)
    print "password", "=>", repr(password)
    


.. sourcecode:: python

    
    login => 'mulder'
    account => None
    password => 'trustno1'



