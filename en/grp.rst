






The grp module
===============




(Unix only). This module provides an interface to the Unix group
database ( **/etc/group**). The **getgrgid** function returns data for
a given group identity, **getgrnam** for a group name.

**Example: Using the grp module**

.. sourcecode:: python

    
    # File: `grp-example-1.py <grp-example-1.py>`__
    
    import grp
    import os
    
    print grp.getgrgid(os.getgid())
    print grp.getgrnam("wheel")
    


.. sourcecode:: python

    
    $ python grp-example-1.py
    ('effbot', '', 4711, ['effbot'])
    ('wheel', '', 10, ['root', 'effbot', 'gorbot', 'timbot'])




The **getgrall** function returns a list of database entries for all
available groups.



If you’re going to do a lot of group queries, you can save some time
by using **getgrall** to copy all the (current) groups into a
dictionary. The **groupinfo** function in the following example
returns the information for either a group identifier (an integer) or
a group name (a string):

**Example: Using the grp module to cache group information**

.. sourcecode:: python

    
    # File: `grp-example-2.py <grp-example-2.py>`__
    
    import grp
    import os
    
    # preload group dictionary
    _grp = {}
    for info in grp.getgrall():
        _grp[info[0]] = _grp[info[2]] = info
    
    def groupinfo(gid):
        # name or gid integer
        return _grp[gid]
    
    print groupinfo(os.getgid())
    print groupinfo("wheel")


.. sourcecode:: python

    
    $ python grp-example-2.py
    ('effbot', '', 4711, ['effbot'])
    ('wheel', '', 10, ['root', 'effbot', 'gorbot', 'timbot'])



