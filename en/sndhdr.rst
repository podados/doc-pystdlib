






The sndhdr module
==================




This module can be used to identify different audio file formats, and
extract basic information about the file contents.



If successful, the **what** function returns a 5-tuple, containing the
file type, the sampling rate, the number of channels, the number of
frames in the file (-1 means unknown), and the number of bits per
sample.

**Example: Using the sndhdr module**

.. sourcecode:: python

    
    # File: `sndhdr-example-1.py <sndhdr-example-1.py>`__
    
    import sndhdr
    
    result = sndhdr.what("samples/sample.wav")
    
    if result:
        print "file format:", result
    else:
        print "cannot identify file"
    


.. sourcecode:: python

    
    file format: ('wav', 44100, 1, -1, 16)



