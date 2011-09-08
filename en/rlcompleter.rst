






The rlcompleter module
=======================




(Optional, Unix only). This module provides word completion for the
**`readline <readline.htm>`__** module.



To enable word completion, just import this module. By default, the
completion function is bound to the **ESCAPE** key. Press **ESCAPE**
twice to finish the current word. To change the key, you can use
something like:


.. sourcecode:: python

    
    import readline
    readline.parse_and_bind("tab: complete")



The following script shows how to use the completion functions from
within a program.

**Example: Using the rlcompleter module to expand names**

.. sourcecode:: python

    
    # File: `rlcompleter-example-1.py <rlcompleter-example-1.py>`__
    
    import rlcompleter
    import sys
    
    completer = rlcompleter.Completer()
    
    for phrase in "co", "sys.p", "is":
        print phrase, "=>",
        # emulate readline completion handler
        try:
            for index in xrange(sys.maxint):
                term = completer.complete(phrase, index)
                if term is None:
                    break
                print term,
        except:
            pass
        print
    


.. sourcecode:: python

    
    co => continue compile complex coerce completer
    sys.p => sys.path sys.platform sys.prefix
    is => is isinstance issubclass



