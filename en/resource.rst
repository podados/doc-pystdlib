






The resource module
====================




(Unix only, Optional). This module is used to query or modify the
system resource limits.


**Example: Using the resource module to query current settings**

.. sourcecode:: python

    
    # File: `resource-example-1.py <resource-example-1.py>`__
    
    import resource
    
    print "usage stats", "=>", resource.getrusage(resource.RUSAGE_SELF)
    print "max cpu", "=>", resource.getrlimit(resource.RLIMIT_CPU)
    print "max data", "=>", resource.getrlimit(resource.RLIMIT_DATA)
    print "max processes", "=>", resource.getrlimit(resource.RLIMIT_NPROC)
    print "page size", "=>", resource.getpagesize()
    


.. sourcecode:: python

    
    usage stats => (0.03, 0.02, 0, 0, 0, 0, 75, 168, 0, 0, 0, 0, 0, 0, 0, 0)
    max cpu => (2147483647, 2147483647)
    max data => (2147483647, 2147483647)
    max processes => (256, 256)
    page size => 4096


**Example: Using the resource module to limit resources**

.. sourcecode:: python

    
    # File: `resource-example-2.py <resource-example-2.py>`__
    
    import resource
    
    resource.setrlimit(resource.RLIMIT_CPU, (0, 1))
    
    # pretend we're busy
    for i in range(1000):
        for j in range(1000):
            for k in range(1000):
                pass
    


.. sourcecode:: python

    
    CPU time limit exceeded



