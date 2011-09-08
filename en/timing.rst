






The timing module
==================




(Obsolete, Unix-only). This module can be used to time the execution
of a Python program.

**Example: Using the timing module**

.. sourcecode:: python

    
    # File: `timing-example-1.py <timing-example-1.py>`__
    
    import timing
    import time
    
    def procedure():
        time.sleep(1.234)
    
    timing.start()
    procedure()
    timing.finish()
    
    print "seconds:", timing.seconds()
    print "milliseconds:", timing.milli()
    print "microseconds:", timing.micro()
    


.. sourcecode:: python

    
    seconds: 1
    milliseconds: 1239
    microseconds: 1239999




The following script shows how you can emulate this module using
functions in the standard **`time <time.htm>`__** module.

**Example: Emulating the timing module**

.. sourcecode:: python

    
    # File: `timing-example-2.py <timing-example-2.py>`__
    
    import time, sys
    
    if sys.platform == "win32":
        timer = time.clock
    else:
        timer = time.time
    
    t0 = t1 = 0
    
    def start():
        global t0
        t0 = timer()
    
    def finish():
        global t1
        t1 = timer()
    
    def seconds():
        return int(t1 - t0)
    
    def milli():
        return int((t1 - t0) * 1000)
    
    def micro():
        return int((t1 - t0) * 1000000)




Note that the script uses **time.clock()** on Windows, since it has a
much higher resolution than the ordinary **time()** function on that
platform. On other platforms, you should only use **clock** to get CPU
time.


