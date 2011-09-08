






The StringIO module
====================




This module implements an in-memory file object. This object can be
used as input or output to most functions that expect a standard file
object.


**Example: Using the StringIO module to read from a static file**

.. sourcecode:: python

    
    # File: `stringio-example-1.py <stringio-example-1.py>`__
    
    import StringIO
    
    MESSAGE = "That man is depriving a village somewhere of a computer scientist."
    
    file = StringIO.StringIO(MESSAGE)
    
    print file.read()
    


.. sourcecode:: python

    
    $ python stringio-example-1.py
    That man is depriving a village somewhere of a computer scientist.





The StringIO class implements memory file versions of all methods
available for built-in file objects, plus a **getvalue** method that
returns the internal string value.

**Example: Using the StringIO module to write to a memory file**

.. sourcecode:: python

    
    # File: `stringio-example-2.py <stringio-example-2.py>`__
    
    import StringIO
    
    file = StringIO.StringIO()
    file.write("This man is no ordinary man. ")
    file.write("This is Mr. F. G. Superman.")
    
    print file.getvalue()
    


.. sourcecode:: python

    
    $ python stringio-example-2.py
    This man is no ordinary man. This is Mr. F. G. Superman.




**StringIO** can be used to capture redirected output from the Python
interpreter:

**Example: Using the StringIO module to capture output**

.. sourcecode:: python

    
    # File: `stringio-example-3.py <stringio-example-3.py>`__
    
    import StringIO
    import string, sys
    
    stdout = sys.stdout
    
    sys.stdout = file = StringIO.StringIO()
    
    print """
    According to Gbaya folktales, trickery and guile
    are the best ways to defeat the python, king of
    snakes, which was hatched from a dragon at the
    world's start. -- National Geographic, May 1997
    """
    
    sys.stdout = stdout
    
    print string.upper(file.getvalue())
    


.. sourcecode:: python

    
    $ python stringio-example-3.py
    ACCORDING TO GBAYA FOLKTALES, TRICKERY AND GUILE
    ARE THE BEST WAYS TO DEFEAT THE PYTHON, KING OF
    SNAKES, WHICH WAS HATCHED FROM A DRAGON AT THE
    WORLD'S START. -- NATIONAL GEOGRAPHIC, MAY 1997




It’s often good idea to wrap the code that generates output in a
try-finally statement, and restore the original sys.stdout in the
finally clause. In this way, stdout will be restored even if the
output operation fails.


