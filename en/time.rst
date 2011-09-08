






The time module
================




This module provides a number of functions to deal with dates and the
time within a day. It’s a thin layer on top of the C runtime
library.



A given date and time can either be represented as a floating point
value (the number of seconds since a reference date, usually January
1st, 1970), or as a time tuple.



Getting the current time
~~~~~~~~~~~~~~~~~~~~~~~~
**Example: Using the time module to get the current time**

.. sourcecode:: python

    
    # File: `time-example-1.py <time-example-1.py>`__
    
    import time
    
    now = time.time()
    
    print now, "seconds since", time.gmtime(0)[:6]
    print
    print "or in other words:"
    print "- local time:", time.localtime(now)
    print "- utc:", time.gmtime(now)
    


.. sourcecode:: python

    
    937758359.77 seconds since (1970, 1, 1, 0, 0, 0)
    
    or in other words:
    - local time: (1999, 9, 19, 18, 25, 59, 6, 262, 1)
    - utc: (1999, 9, 19, 16, 25, 59, 6, 262, 0)




The tuple returned by **localtime** and **gmtime** contains (year,
month, day, hour, minute, second, day of week, day of year, daylight
savings flag), where the year number is four digits, the day of week
begins with 0 for Monday, and January 1st is day number 1.



Converting time values to strings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


You can of course use standard string formatting operators to convert
a time tuple to a string, but the **time** module also provides a
number of standard conversion functions:


**Example: Using the time module to format dates and times**

.. sourcecode:: python

    
    # File: `time-example-2.py <time-example-2.py>`__
    
    import time
    
    now = time.localtime(time.time())
    
    print time.asctime(now)
    print time.strftime("%y/%m/%d %H:%M", now)
    print time.strftime("%a %b %d", now)
    print time.strftime("%c", now)
    print time.strftime("%I %p", now)
    print time.strftime("%Y-%m-%d %H:%M:%S %Z", now)
    
    # do it by hand...
    year, month, day, hour, minute, second, weekday, yearday, daylight = now
    print "%04d-%02d-%02d" % (year, month, day)
    print "%02d:%02d:%02d" % (hour, minute, second)
    print ("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN")[weekday], yearday
    


.. sourcecode:: python

    
    Sun Oct 10 21:39:24 1999
    99/10/10 21:39
    Sun Oct 10
    Sun Oct 10 21:39:24 1999
    09 PM
    1999-10-10 21:39:24 CEST
    1999-10-10
    21:39:24
    SUN 283





Converting strings to time values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


On some platforms, the **time** module contains a **strptime**
function, which is pretty much the opposite of **strftime**. Given a
string and a pattern, it returns the corresponding time tuple:

**Example: Using the time.strptime function to parse dates and times**

.. sourcecode:: python

    
    # File: `time-example-6.py <time-example-6.py>`__
    
    import time
    
    # make sure we have a strptime function!
    try:
        strptime = time.strptime
    except AttributeError:
        from strptime import strptime
    
    print strptime("31 Nov 00", "%d %b %y")
    print strptime("1 Jan 70 1:30pm", "%d %b %y %I:%M%p")




The **time.strptime** function is currently only made available by
Python if it’s provided by the platform’s C libraries. For
platforms that don’t have a standard implementation (this includes
Windows), here’s a partial replacement:


**Example: A strptime implementation**

.. sourcecode:: python

    
    # File: `strptime.py <strptime.py>`__
    
    import re
    import string
    
    MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
              "Sep", "Oct", "Nov", "Dec"]
    
    SPEC = {
        # map formatting code to a regular expression fragment
        "%a": "(?P[a-z]+)",
        "%A": "(?P[a-z]+)",
        "%b": "(?P[a-z]+)",
        "%B": "(?P[a-z]+)",
        "%C": "(?P\d\d?)",
        "%d": "(?P\d\d?)",
        "%D": "(?P\d\d?)/(?P\d\d?)/(?P\d\d)",
        "%e": "(?P\d\d?)",
        "%h": "(?P[a-z]+)",
        "%H": "(?P\d\d?)",
        "%I": "(?P\d\d?)",
        "%j": "(?P\d\d?\d?)",
        "%m": "(?P\d\d?)",
        "%M": "(?P\d\d?)",
        "%p": "(?Pam|pm)",
        "%R": "(?P\d\d?):(?P\d\d?)",
        "%S": "(?P\d\d?)",
        "%T": "(?P\d\d?):(?P\d\d?):(?P\d\d?)",
        "%U": "(?P\d\d)",
        "%w": "(?P\d)",
        "%W": "(?P\d\d)",
        "%y": "(?P\d\d)",
        "%Y": "(?P\d\d\d\d)",
        "%%": "%"
    }
    
    class TimeParser:
        def __init__(self, format):
            # convert strptime format string to regular expression
            format = string.join(re.split("(?:\s|%t|%n)+", format))
            pattern = []
            try:
                for spec in re.findall("%\w|%%|.", format):
                    if spec[0] == "%":
                        spec = SPEC[spec]
                    pattern.append(spec)
            except KeyError:
                raise ValueError, "unknown specificer: %s" % spec
            self.pattern = re.compile("(?i)" + string.join(pattern, ""))
        def match(self, daytime):
            # match time string
            match = self.pattern.match(daytime)
            if not match:
                raise ValueError, "format mismatch"
            get = match.groupdict().get
            tm = [0] * 9
            # extract date elements
            y = get("year")
            if y:
                y = int(y)
                if y < 68:
                    y = 2000 + y
                elif y < 100:
                    y = 1900 + y
                tm[0] = y
            m = get("month")
            if m:
                if m in MONTHS:
                    m = MONTHS.index(m) + 1
                tm[1] = int(m)
            d = get("day")
            if d: tm[2] = int(d)
            # extract time elements
            h = get("hour")
            if h:
                tm[3] = int(h)
            else:
                h = get("hour12")
                if h:
                    h = int(h)
                    if string.lower(get("ampm12", "")) == "pm":
                        h = h + 12
                    tm[3] = h
            m = get("minute")
            if m: tm[4] = int(m)
            s = get("second")
            if s: tm[5] = int(s)
            # ignore weekday/yearday for now
            return tuple(tm)
    
    def strptime(string, format="%a %b %d %H:%M:%S %Y"):
        return TimeParser(format).match(string)
    
    if __name__ == "__main__":
        # try it out
        import time
        print strptime("2000-12-20 01:02:03", "%Y-%m-%d %H:%M:%S")
        print strptime(time.ctime(time.time()))
    


.. sourcecode:: python

    
    (2000, 12, 20, 1, 2, 3, 0, 0, 0)
    (2000, 11, 15, 12, 30, 45, 0, 0, 0)





Converting time values
~~~~~~~~~~~~~~~~~~~~~~


Converting a time tuple back to a time value is pretty easy, at least
as long as we’re talking about local time. Just pass the time tuple
to the **mktime** function:

**Example: Using the time module to convert a local time tuple to a
time integer**

.. sourcecode:: python

    
    # File: `time-example-3.py <time-example-3.py>`__
    
    import time
    
    t0 = time.time()
    tm = time.localtime(t0)
    
    print tm
    
    print t0
    print time.mktime(tm)
    


.. sourcecode:: python

    
    (1999, 9, 9, 0, 11, 8, 3, 252, 1)
    936828668.16
    936828668.0




Unfortunately, there’s no function in the 1.5.2 standard library
that converts UTC time tuples back to time values (neither in Python
nor in the underlying C libraries). The following example provides a
Python implementation of such a function, called **timegm**:


**Example: Converting a UTC time tuple to a time integer**

.. sourcecode:: python

    
    # File: `time-example-4.py <time-example-4.py>`__
    
    import time
    
    def _d(y, m, d, days=(0,31,59,90,120,151,181,212,243,273,304,334,365)):
        # map a date to the number of days from a reference point
        return (((y - 1901)*1461)/4 + days[m-1] + d +
            ((m > 2 and not y % 4 and (y % 100 or not y % 400)) and 1))
    
    def timegm(tm, epoch=_d(1970,1,1)):
        year, month, day, h, m, s = tm[:6]
        assert year >= 1970
        assert 1 <= month <= 12
        return (_d(year, month, day) - epoch)*86400 + h*3600 + m*60 + s
    
    t0 = time.time()
    tm = time.gmtime(t0)
    
    print tm
    
    print t0
    print timegm(tm)
    


.. sourcecode:: python

    
    (1999, 9, 8, 22, 12, 12, 2, 251, 0)
    936828732.48
    936828732





In 1.6 and later, a similar function is available in the **`calendar
<calendar.htm>`__** module, as **calendar.timegm**.



Timing things
~~~~~~~~~~~~~


The **time** module can be used to time the execution of a Python
program. You can measure either “wall time” (real world time), or
“process time” (the amount of CPU time the process has consumed,
this far).

**Example: Using the time module to benchmark an algorithm**

.. sourcecode:: python

    
    # File: `time-example-5.py <time-example-5.py>`__
    
    import time
    
    def procedure():
        time.sleep(2.5)
    
    # measure process time
    t0 = time.clock()
    procedure()
    print time.clock() - t0, "seconds process time"
    
    # measure wall time
    t0 = time.time()
    procedure()
    print time.time() - t0, "seconds wall time"
    


.. sourcecode:: python

    
    0.0 seconds process time
    2.50903499126 seconds wall time




Not all systems can measure the true process time. On such systems
(including Windows), **clock** usually measures the wall time since
the program was started.



Also see the **`timing <timing.htm>`__** module, which measures the
wall time between two events.



The process time has limited precision. On many systems, it wraps
around after just over 30 minutes.


