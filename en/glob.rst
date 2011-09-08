






The glob module
================




This module generates lists of files matching given patterns, just
like the Unix shell.



File patterns are similar to regular expressions, but simpler. An
asterisk ( *****) matches zero or more characters, and a question mark
( **?**) exactly one character. You can also use brackets to indicate
character ranges, such as **[0-9]** for a single digit. All other
characters match themselves.



**glob(pattern)** returns a list of all files matching a given
pattern.

**Example: Using the glob module**

.. sourcecode:: python

    
    # File: `glob-example-1.py <glob-example-1.py>`__
    
    import glob
    
    for file in glob.glob("samples/*.jpg"):
        print file
    


.. sourcecode:: python

    
    samples/sample.jpg




Note that **glob** returns full path names, unlike the **os.listdir**
function. **glob** uses the **`fnmatch <fnmatch.htm>`__** module to do
the actual pattern matching.


