






The packmail module
====================




(Obsolete) This module contain tools to create Unix “shell
archives” . If you have the right tools installed (if you have a
Unix box, they are installed), you can unpack such an archive simply
by executing it.

**Example: Using the packmail module to pack a single file**

.. sourcecode:: python

    
    # File: `packmail-example-1.py <packmail-example-1.py>`__
    
    import packmail
    import sys
    
    packmail.pack(sys.stdout, "samples/sample.txt", "sample.txt")
    


.. sourcecode:: python

    
    echo sample.txt
    sed "s/^X//" >sample.txt <<"!"
    XWe will perhaps eventually be writing only small
    Xmodules which are identified by name as they are
    Xused to build larger ones, so that devices like
    Xindentation, rather than delimiters, might become
    Xfeasible for expressing local structure in the
    Xsource language.
    X    -- Donald E. Knuth, December 1974
    !

**Example: Using the packmail module to pack an entire directory
tree**

.. sourcecode:: python

    
    # File: `packmail-example-2.py <packmail-example-2.py>`__
    
    import packmail
    import sys
    
    packmail.packtree(sys.stdout, "samples")




Note that this module cannot handle binary files, such as images and
sound snippets.


