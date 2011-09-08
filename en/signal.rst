






The signal module
==================




This module is used to install your own signal handlers. When the
interpreter sees a signal, the signal handler is executed as soon as
possible.

**Example: Using the signal module**

.. sourcecode:: python

    
    # File: `signal-example-1.py <signal-example-1.py>`__
    
    import signal
    import time
    
    def handler(signo, frame):
        print "got signal", signo
    
    signal.signal(signal.SIGALRM, handler)
    
    # wake me up in two seconds
    signal.alarm(2)
    
    now = time.time()
    
    time.sleep(200)
    
    print "slept for", time.time() - now, "seconds"
    


.. sourcecode:: python

    
    got signal 14
    slept for 1.99262607098 seconds



