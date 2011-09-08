






The tzparse module
===================




(Obsolete). This (highly incomplete) module contains a parser for
timezone specifications. When you import this module, it parses the
content of the TZ environment variable.

**Example: Using the tzparse module**

.. sourcecode:: python

    
    # File: `tzparse-example-1.py <tzparse-example-1.py>`__
    
    import os
    if not os.environ.has_key("TZ"):
        # set it to something...
        os.environ["TZ"] = "EST+5EDT;100/2,300/2"
    
    # importing this module will parse the TZ variable
    import tzparse
    
    print "tzparams", "=>", tzparse.tzparams
    print "timezone", "=>", tzparse.timezone
    print "altzone", "=>", tzparse.altzone
    print "daylight", "=>", tzparse.daylight
    print "tzname", "=>", tzparse.tzname
    


.. sourcecode:: python

    
    tzparams => ('EST', 5, 'EDT', 100, 2, 300, 2)
    timezone => 18000
    altzone => 14400
    daylight => 1
    tzname => ('EST', 'EDT')




In addition to the variables shown in this example, this module
contains a number of time manipulation functions that use the defined
time zone.


