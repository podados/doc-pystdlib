






The sched module
=================




This is a simple event scheduler for non-threaded environments.

**Example: Using the sched module**

.. sourcecode:: python

    
    # File: `sched-example-1.py <sched-example-1.py>`__
    
    import sched
    import time, sys
    
    scheduler = sched.scheduler(time.time, time.sleep)
    
    # add a few operations to the queue
    scheduler.enter(0.5, 100, sys.stdout.write, ("one\n",))
    scheduler.enter(1.0, 300, sys.stdout.write, ("three\n",))
    scheduler.enter(1.0, 200, sys.stdout.write, ("two\n",))
    
    scheduler.run()
    


.. sourcecode:: python

    
    one
    two
    three



