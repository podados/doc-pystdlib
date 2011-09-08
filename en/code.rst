






The code module
================




This module provides a number of functions that can be used to emulate
the behavior of the standard interpreter’s interactive mode.



The **compile_command** behaves like the built-in **compile**
function, but does some additional tests to make sure you pass it a
complete Python statement.



In the following example, we’re compiling a program line by line,
executing the resulting code objects as soon as we manage to compile.
The program looks like this:


.. sourcecode:: python

    
    a = (
      1,
      2,
      3
    )
    print a



Note that the tuple assignment cannot be properly compiled until
we’ve reached the second parenthesis.

**Example: Using the code module to compile statements**

.. sourcecode:: python

    
    # File: `code-example-1.py <code-example-1.py>`__
    
    import code
    import string
    
    # 
    SCRIPT = [
        "a = (",
        "  1,",
        "  2,",
        "  3 ",
        ")",
        "print a"
    ]
    
    script = ""
    
    for line in SCRIPT:
        script = script + line + "\n"
        co = code.compile_command(script, "", "exec")
        if co:
            # got a complete statement.  execute it!
            print "-"*40
            print script,
            print "-"*40
            exec co
            script = ""
    


.. sourcecode:: python

    
    $ python code-example-1.py
    ----------------------------------------
    a = (
      1,
      2,
      3 
    )
    ----------------------------------------
    ----------------------------------------
    print a
    ----------------------------------------
    (1, 2, 3)




The **InteractiveConsole** class implements an interactive console,
much like the one you get when you fire up the Python interpreter in
interactive mode.



The console can be either active (it calls a function to get the next
line) or passive (you call the **push** method when you have new
data). The default is to use the built-in **raw_input** function.
Overload the method with the same name if you prefer to use another
input function.

**Example: Using the code module to emulate the interactive
interpreter**

.. sourcecode:: python

    
    # File: `code-example-2.py <code-example-2.py>`__
    
    import code
    
    console = code.InteractiveConsole()
    console.interact()
    


.. sourcecode:: python

    
    $ python code-example-2.py
    Python 1.5.2
    Copyright 1991-1995 Stichting Mathematisch Centrum, Amsterdam
    (InteractiveConsole)
    >>> a = (
    ...     1,
    ...     2,
    ...     3
    ... )
    >>> print a
    (1, 2, 3)




The following script defines a function called **keyboard**. It allows
you to hand control over to the interactive interpreter at any point
in your program.

**Example: Using the code module for simple debugging**

.. sourcecode:: python

    
    # File: `code-example-3.py <code-example-3.py>`__
    
    def keyboard(banner=None):
        import code, sys
    
        # use exception trick to pick up the current frame
        try:
            raise None
        except:
            frame = sys.exc_info()[2].tb_frame.f_back
    
        # evaluate commands in current namespace
        namespace = frame.f_globals.copy()
        namespace.update(frame.f_locals)
    
        code.interact(banner=banner, local=namespace)
    
    def func():
        print "START"
        a = 10
        keyboard()
        print "END"
    
    func()
    


.. sourcecode:: python

    
    $ python code-example-3.py
    START
    Python 1.5.2
    Copyright 1991-1995 Stichting Mathematisch Centrum, Amsterdam
    (InteractiveConsole)
    >>> print a
    10
    >>> print keyboard
    
    ^Z
    END



