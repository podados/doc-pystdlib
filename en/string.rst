






The string module
==================




This module contains a number of functions to process standard Python
strings. In recent versions, most functions are available as string
methods as well (more on this below).


**Example: Using the string module**

.. sourcecode:: python

    
    # File: `string-example-1.py <string-example-1.py>`__
    
    import string
    
    text = "Monty Python's Flying Circus"
    
    print "upper", "=>", string.upper(text)
    print "lower", "=>", string.lower(text)
    print "split", "=>", string.split(text)
    print "join", "=>", string.join(string.split(text), "+")
    print "replace", "=>", string.replace(text, "Python", "Java")
    print "find", "=>", string.find(text, "Python"), string.find(text, "Java")
    print "count", "=>", string.count(text, "n")
    


.. sourcecode:: python

    
    upper => MONTY PYTHON'S FLYING CIRCUS
    lower => monty python's flying circus
    split => ['Monty', "Python's", 'Flying', 'Circus']
    join => Monty+Python's+Flying+Circus
    replace => Monty Java's Flying Circus
    find => 6 -1
    count => 3





In Python 1.5.2 and earlier, this module uses functions from the
**`strop <strop.htm>`__** implementation module where possible.



In Python 1.6 and later, most string operations are made available as
string methods as well, and many functions in the **string** module
are simply wrapper functions that call the corresponding string
method.

**Example: Using string methods instead of string module functions
(Python 1.6 and later)**

.. sourcecode:: python

    
    # File: `string-example-2.py <string-example-2.py>`__
    
    text = "Monty Python's Flying Circus"
    
    print "upper", "=>", text.upper()
    print "lower", "=>", text.lower()
    print "split", "=>", text.split()
    print "join", "=>", "+".join(text.split())
    print "replace", "=>", text.replace("Python", "Perl")
    print "find", "=>", text.find("Python"), text.find("Perl")
    print "count", "=>", text.count("n")
    


.. sourcecode:: python

    
    upper => MONTY PYTHON'S FLYING CIRCUS
    lower => monty python's flying circus
    split => ['Monty', "Python's", 'Flying', 'Circus']
    join => Monty+Python's+Flying+Circus
    replace => Monty Perl's Flying Circus
    find => 6 -1
    count => 3




In addition to the string manipulation stuff, the **string** module
also contains a number of functions which convert strings to other
types:

**Example: Using the string module to convert strings to numbers**

.. sourcecode:: python

    
    # File: `string-example-3.py <string-example-3.py>`__
    
    import string
    
    print int("4711"),
    print string.atoi("4711"),
    print string.atoi("11147", 8), # octal
    print string.atoi("1267", 16), # hexadecimal
    print string.atoi("3mv", 36) # whatever...
    
    print string.atoi("4711", 0),
    print string.atoi("04711", 0),
    print string.atoi("0x4711", 0)
    
    print float("4711"),
    print string.atof("1"),
    print string.atof("1.23e5")
    


.. sourcecode:: python

    
    4711 4711 4711 4711 4711
    4711 2505 18193
    4711.0 1.0 123000.0




In most cases (especially if you’re using 1.6 or later), you can use
the **int** and **float** functions instead of their **string** module
counterparts.



The **atoi** function takes an optional second argument, which
specifices the number base. If the base is zero, the function looks at
the first few characters before attempting to interpret the value: if
“0x” , the base is set to 16 (hexadecimal), and if “0” , the
base is set to 8 (octal). The default is base 10 (decimal), just as if
you hadn’t provided an extra argument.



In 1.6 and later, the **int** also accepts a second argument, just
like **atoi**. But unlike the string versions, **int** and **float**
also accepts Unicode strings.


