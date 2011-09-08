






The regsub module
==================




(Obsolete). This module provides string replacements, based on regular
expressions. New code should use the **re** module’s **replace**
function instead.

**Example: Using the regsub module**

.. sourcecode:: python

    
    # File: `regsub-example-1.py <regsub-example-1.py>`__
    
    import regsub
    
    text = "Well, there's spam, egg, sausage and spam."
    
    print regsub.sub("spam", "ham", text) # just the first
    print regsub.gsub("spam", "bacon", text) # all of them
    


.. sourcecode:: python

    
    Well, there's ham, egg, sausage and spam.
    Well, there's bacon, egg, sausage and bacon.



