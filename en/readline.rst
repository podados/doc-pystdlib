






The readline module
====================




(Optional). This module activates input editing on Unix, using the GNU
readline library (or a compatible library).



Once imported, this module provides improved command line editing, and
also command history. It also enhances the **input** and **raw_input**
functions.

**Example: Using the readline module**

.. sourcecode:: python

    
    # File: `readline-example-1.py <readline-example-1.py>`__
    
    import readline # activate readline editing




The module supports customized completion handling. The following
example shows how to install a completion handler:

**Example: Installing a custom completion handler**

.. sourcecode:: python

    
    # File: readline-example-2.py
    
    class Completer:
        def __init__(self, words):
            self.words = words
            self.prefix = None
        def complete(self, prefix, index):
            if prefix != self.prefix:
                # we have a new prefix!
                # find all words that start with this prefix
                self.matching_words = [
                    w for w in self.words if w.startswith(prefix)
                    ]
                self.prefix = prefix
            try:
                return self.matching_words[index]
            except IndexError:
                return None
    
    import readline
    
    # a set of more or less interesting words
    words = "perl", "pyjamas", "python", "pythagoras"
    
    completer = Completer(words)
    
    readline.parse_and_bind("tab: complete")
    readline.set_completer(completer.complete)
    
    # try it out!
    while 1:
        print repr(raw_input(">>> "))




The ` **rlcompleter** <rlcompleter.htm>`__ provides more advanced
completion for the Python interpreter command line.


