






The commands module
====================




(Unix only). This function contains a few convenience functions,
designed to make it easier to execute external commands under Unix.

**Example: Using the commands module**

.. sourcecode:: python

    
    # File: `commands-example-1.py <commands-example-1.py>`__
    
    import commands
    
    stat, output = commands.getstatusoutput("ls -lR")
    
    print "status", "=>", stat
    print "output", "=>", len(output), "bytes"
    


.. sourcecode:: python

    
    status => 0
    output => 171046 bytes



