






The atexit module
==================




(2.0 and newer) This module allows you to register one or more
functions that are called when the interpreter is terminated.



To register a function, simply call the **register** function. You can
also add one or more extra arguments, which are passed as arguments to
the exit function.

**Example: Using the atexit module**

.. sourcecode:: python

    
    # File: `atexit-example-1.py <atexit-example-1.py>`__
    
    import atexit
    
    def exit(*args):
        print "exit", args
    
    # register three exit handlers
    atexit.register(exit)
    atexit.register(exit, 1)
    atexit.register(exit, "hello", "world")
    


.. sourcecode:: python

    
    $ python atexit-example-1.py
    exit ('hello', 'world')
    exit (1,)
    exit ()




This module is a straightforward wrapper for the ` **sys.exitfunc**
<sys.htm>`__ hook.


