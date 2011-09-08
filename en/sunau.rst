






The sunau module
=================




This module reads and writes Sun AU audio files.

**Example: Using the sunau module**

.. sourcecode:: python

    
    # File: `sunau-example-1.py <sunau-example-1.py>`__
    
    import sunau
    
    w = sunau.open("samples/sample.au", "r")
    
    if w.getnchannels() == 1:
        print "mono,",
    else:
        print "stereo,",
    
    print w.getsampwidth()*8, "bits,",
    print w.getframerate(), "Hz sampling rate"
    


.. sourcecode:: python

    
    mono, 16 bits, 8012 Hz sampling rate



