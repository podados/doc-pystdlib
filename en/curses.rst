






The curses module
==================




(Unix only, Optional). The curses module gives you better control of
the text terminal window, in a terminal-independent way.

**Example: Using the curses module**

.. sourcecode:: python

    
    # File: `curses-example-1.py <curses-example-1.py>`__
    
    import curses
    
    text = [
        "a very simple curses demo",
        "",
        "(press any key to exit)"
    ]
    
    # connect to the screen
    screen = curses.initscr()
    
    # setup keyboard
    curses.noecho() # no keyboard echo
    curses.cbreak() # don't wait for newline
    
    # screen size
    rows, columns = screen.getmaxyx()
    
    # draw a border around the screen
    screen.border()
    
    # display centered text
    y = (rows - len(text)) / 2
    
    for line in text:
        screen.addstr(y, (columns-len(line))/2, line)
        y = y + 1
    
    screen.getch()
    
    curses.endwin()



