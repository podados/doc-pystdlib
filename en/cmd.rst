






The cmd module
===============




This module provides a simple framework for command-line interfaces
(CLI). This is used by the **`pdb <pdb.htm>`__** debugger module, but
you can also use it for your own programs.



To implement your own command-line interface, subclass the **Cmd**
class, and define **do** and **help** methods. The base class
automatically turns all **do** methods into commands, and uses the
**help** methods to show help information.

**Example: Using the cmd module**

.. sourcecode:: python

    
    # File: `cmd-example-1.py <cmd-example-1.py>`__
    
    import cmd
    import string, sys
    
    class CLI(cmd.Cmd):
    
        def __init__(self):
            cmd.Cmd.__init__(self)
            self.prompt = '> '
    
        def do_hello(self, arg):
            print "hello again", arg, "!"
    
        def help_hello(self):
            print "syntax: hello [message]",
            print "-- prints a hello message"
    
        def do_quit(self, arg):
            sys.exit(1)
    
        def help_quit(self):
            print "syntax: quit",
            print "-- terminates the application"
    
        # shortcuts
        do_q = do_quit
    
    #
    # try it out
    
    cli = CLI()
    cli.cmdloop()


.. sourcecode:: python

    
    $ python cmd-example-1.py
    > help
    
    Documented commands (type help ):
    ========================================
    hello           quit
    
    Undocumented commands:
    ======================
    help            q
    
    > hello world
    hello again world !
    > q



