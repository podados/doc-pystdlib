






The rexec module
=================




**Note:** This module is not safe in Python 2.2 and later, and has
been removed in Python 2.3.



This module provides versions of **exec**, **eval**, and **import**
which executes code in a restricted execution environment. In this
environment, functions that can damage resources on the local machine
are no longer available.

**Example: Using the rexec module**

.. sourcecode:: python

    
    # File: `rexec-example-1.py <rexec-example-1.py>`__
    
    import rexec
    
    r = rexec.RExec()
    print r.r_eval("1+2+3")
    print r.r_eval("__import__('os').remove('file')")
    


.. sourcecode:: python

    
    6
    Traceback (innermost last):
      File "rexec-example-1.py", line 5, in ?
        print r.r_eval("__import__('os').remove('file')")
      File "/usr/local/lib/python1.5/rexec.py", line 257, in r_eval
        return eval(code, m.__dict__)
      File "", line 0, in ?
    AttributeError: remove



