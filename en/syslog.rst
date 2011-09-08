






The syslog module
==================




(Unix only, Optional). This module sends messages to the system logger
facility ( **syslogd**). Exactly what happens to these messages is
system-dependent, but they usually end up in a log file named
**/var/log/messages**, **/var/adm/syslog**, or some variation thereof.
(If you cannot find it, check with your favorite system
administrator.)


**Example: Using the syslog module**

.. sourcecode:: python

    
    # File: `syslog-example-1.py <syslog-example-1.py>`__
    
    import syslog
    import sys
    
    syslog.openlog(sys.argv[0])
    
    syslog.syslog(syslog.LOG_NOTICE, "a log notice")
    syslog.syslog(syslog.LOG_NOTICE, "another log notice: %s" % "watch out!")
    
    syslog.closelog()


