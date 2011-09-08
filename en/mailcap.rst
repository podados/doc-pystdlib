






The mailcap module
===================




This module contains code to deal with “mailcap” files, which
contain information on how to deal with different document formats (on
Unix platforms).

**Example: Using the mailcap module to get a capability dictionary**

.. sourcecode:: python

    
    # File: `mailcap-example-1.py <mailcap-example-1.py>`__
    
    import mailcap
    
    caps = mailcap.getcaps()
    
    for k, v in caps.items():
        print k, "=", v
    


.. sourcecode:: python

    
    image/* = [{'view': 'pilview'}]
    application/postscript = [{'view': 'ghostview'}]




In the above example, the system uses **pilview** for all kinds of
images, and **ghostscript** viewer for PostScript documents.

**Example: Using the mailcap module to find a viewer**

.. sourcecode:: python

    
    # File: `mailcap-example-2.py <mailcap-example-2.py>`__
    
    import mailcap
    
    caps = mailcap.getcaps()
    
    command, info = mailcap.findmatch(
        caps, "image/jpeg", "view", "samples/sample.jpg"
        )
    
    print command
    


.. sourcecode:: python

    
    pilview samples/sample.jpg



