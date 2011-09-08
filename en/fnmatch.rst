






The fnmatch module
===================




This module allows you to match filenames against a pattern.



The pattern syntax is the same as that used in Unix shells. An
asterisk ( *****) matches zero or more characters, and a question mark
( **?**) exactly one character. You can also use brackets to indicate
character ranges, such as **[0-9]** for a single digit. All other
characters match themselves.

**Example: Using the fnmatch module to match files**

.. sourcecode:: python

    
    # File: `fnmatch-example-1.py <fnmatch-example-1.py>`__
    
    import fnmatch
    import os
    
    for file in os.listdir("samples"):
        if fnmatch.fnmatch(file, "*.jpg"):
            print file
    


.. sourcecode:: python

    
    sample.jpg




The **translate** function converts a file pattern to a regular
expression:

**Example: Using the fnmatch module to convert a pattern to a regular
expression**

.. sourcecode:: python

    
    # File: `fnmatch-example-2.py <fnmatch-example-2.py>`__
    
    import fnmatch
    import os, re
    
    pattern = fnmatch.translate("*.jpg")
    
    for file in os.listdir("samples"):
        if re.match(pattern, file):
            print file
    
    print "(pattern was %s)" % pattern
    


.. sourcecode:: python

    
    sample.jpg
    (pattern was .*\.jpg$)




This module is used by the **`glob <glob.htm>`__** and **`find
<find.htm>`__** modules.


