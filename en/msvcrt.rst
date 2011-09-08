






The msvcrt module
==================




(Windows/DOS only). This module gives you access to a number of
functions in the Microsoft Visual C/C++ Runtime Library (MSVCRT).



The **getch** function reads a single keypress from the console:

**Example: Using the msvcrt module to get key presses**

.. sourcecode:: python

    
    # File: `msvcrt-example-1.py <msvcrt-example-1.py>`__
    
    import msvcrt
    
    print "press 'escape' to quit..."
    
    while 1:
        char = msvcrt.getch()
        if char == chr(27):
            break
        print char,
        if char == chr(13):
            print
    


.. sourcecode:: python

    
    $ python msvcrt-example-1.py
    press 'escape' to quit...
    h e l l o




The **kbhit** function returns true if a key has been pressed (which
means that **getch** won’t block).

**Example: Using the msvcrt module to poll the keyboard**

.. sourcecode:: python

    
    # File: `msvcrt-example-2.py <msvcrt-example-2.py>`__
    
    import msvcrt
    import time
    
    print "press SPACE to enter the serial number"
    
    while not msvcrt.kbhit() or msvcrt.getch() != " ":
        # do something else while we're waiting
        print ".",
        time.sleep(0.1)
    
    print
    
    # clear the keyboard buffer
    while msvcrt.kbhit():
        msvcrt.getch()
    
    serial = raw_input("enter your serial number: ")
    
    print "serial number is", serial
    


.. sourcecode:: python

    
    $ python msvcrt-example-2.py
    press SPACE to enter the serial number
    . . . . . . . . . . . . . . . . . . . . . . . .
    enter your serial number: 10
    serial number is 10




The **locking** function can be used to implement cross-process file
locking under Windows:


**Example: Using the msvcrt module for file locking**

.. sourcecode:: python

    
    # File: `msvcrt-example-3.py <msvcrt-example-3.py>`__
    
    import msvcrt
    import os, time
    
    LK_UNLCK = 0 # unlock the file region
    LK_LOCK = 1 # lock the file region
    LK_NBLCK = 2 # non-blocking lock
    LK_RLCK = 3 # lock for writing
    LK_NBRLCK = 4 # non-blocking lock for writing
    
    FILE = "counter.txt"
    
    if not os.path.exists(FILE):
        file = open(FILE, "w")
        file.write("0")
        file.close()
    
    for i in range(20):
        file = open(FILE, "r+")
        # lock from current position (0) to end of file
        msvcrt.locking(file.fileno(), LK_LOCK, os.path.getsize(FILE))
        counter = int(file.readline()) + 1
        file.seek(0)
        file.write(str(counter))
        file.close() # unlocks the file
        print os.getpid(), "=>", counter
        time.sleep(0.1)
    


.. sourcecode:: python

    
    $ python msvcrt-example-3.py
    208 => 21
    208 => 22
    208 => 23
    208 => 24
    208 => 25
    208 => 26


