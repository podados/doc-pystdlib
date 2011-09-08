






The pwd module
===============




(Unix only). This module provides an interface to the Unix password
“database” ( **/etc/passwd** and friends). This database (usually
a plain text file) contains information about the user accounts on the
local machine.


**Example: Using the pwd module**

.. sourcecode:: python

    
    # File: `pwd-example-1.py <pwd-example-1.py>`__
    
    import pwd
    import os
    
    print pwd.getpwuid(os.getuid())
    print pwd.getpwnam("root")
    


.. sourcecode:: python

    
    ('effbot', 'dsWjk8', 4711, 4711, 'eff-bot', '/home/effbot', '/bin/bosh')
    ('root', 'hs2giiw', 0, 0, 'root', '/root', '/bin/bash')





The **getpwall** function returns a list of database entries for all
available users. This can be useful if you want to search for a user.



If you have to look up many names, you can use **getpwall** to preload
a dictionary:


**Example: Using the pwd module**

.. sourcecode:: python

    
    # File: `pwd-example-2.py <pwd-example-2.py>`__
    
    import pwd
    import os
    
    # preload password dictionary
    _pwd = {}
    for info in pwd.getpwall():
        _pwd[info[0]] = _pwd[info[2]] = info
    
    def userinfo(uid):
        # name or uid integer
        return _pwd[uid]
    
    print userinfo(os.getuid())
    print userinfo("root")


.. sourcecode:: python

    
    ('effbot', 'dsWjk8', 4711, 4711, 'eff-bot', '/home/effbot', '/bin/bosh')
    ('root', 'hs2giiw', 0, 0, 'root', '/root', '/bin/bash')


