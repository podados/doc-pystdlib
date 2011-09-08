






The whatsound module
=====================




(Obsolete). This is an alias for **`sndhdr <sndhdr.htm>`__**.

**Example: Using the whatsound module**

.. sourcecode:: python

    
    # File: `whatsound-example-1.py <whatsound-example-1.py>`__
    
    import whatsound # same as sndhdr
    
    result = whatsound.what("samples/sample.wav")
    
    if result:
        print "file format:", result
    else:
        print "cannot identify file"
    


.. sourcecode:: python

    
    file format: ('wav', 44100, 1, -1, 16)



