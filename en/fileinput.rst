






The fileinput module
=====================




This module allows you to loop over the contents of one or more text
files.

**Example: Using the fileinput module to loop over a text file**

.. sourcecode:: python

    
    # File: `fileinput-example-1.py <fileinput-example-1.py>`__
    
    import fileinput
    import sys
    
    for line in fileinput.input("samples/sample.txt"):
        sys.stdout.write("-> ")
        sys.stdout.write(line)
    


.. sourcecode:: python

    
    -> We will perhaps eventually be writing only small
    -> modules which are identified by name as they are
    -> used to build larger ones, so that devices like
    -> indentation, rather than delimiters, might become
    -> feasible for expressing local structure in the
    -> source language.
    ->      -- Donald E. Knuth, December 1974




You can pass in a single filename, or a list of filenames. If you
leave out the filename argument, **fileinput** gets the names from
**sys.argv**.



The module also allows you to get metainformation about the current
line. This includes **isfirstline**, **filename**, and **lineno**:


**Example: Using the fileinput module to process multiple files**

.. sourcecode:: python

    
    # File: `fileinput-example-2.py <fileinput-example-2.py>`__
    
    import fileinput
    import glob
    import string, sys
    
    for line in fileinput.input(glob.glob("samples/*.txt")):
        if fileinput.isfirstline(): # first in a file?
            sys.stderr.write("-- reading %s --\n" % fileinput.filename())
        sys.stdout.write(str(fileinput.lineno()) + " " + string.upper(line))
    


.. sourcecode:: python

    
    -- reading samples\sample.txt --
    1 WE WILL PERHAPS EVENTUALLY BE WRITING ONLY SMALL
    2 MODULES WHICH ARE IDENTIFIED BY NAME AS THEY ARE
    3 USED TO BUILD LARGER ONES, SO THAT DEVICES LIKE
    4 INDENTATION, RATHER THAN DELIMITERS, MIGHT BECOME
    5 FEASIBLE FOR EXPRESSING LOCAL STRUCTURE IN THE
    6 SOURCE LANGUAGE.
    7    -- DONALD E. KNUTH, DECEMBER 1974





Processing text files in place is also easy. Just call the **input**
function with the **inplace** keyword argument set to 1, and the
module takes care of the rest.

**Example: Using the fileinput module to convert CRLF to LF**

.. sourcecode:: python

    
    # File: `fileinput-example-3.py <fileinput-example-3.py>`__
    
    import fileinput, sys
    
    for line in fileinput.input(inplace=1):
        # convert Windows/DOS text files to Unix files
        if line[-2:] == "\r\n":
            line = line[:-2] + "\n"
        sys.stdout.write(line)



