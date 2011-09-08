






The wave module
================




This module reads and writes Microsoft WAV audio files.

**Example: Using the wave module**

.. sourcecode:: python

    
    # File: `wave-example-1.py <wave-example-1.py>`__
    
    import wave
    
    w = wave.open("samples/sample.wav", "r")
    
    if w.getnchannels() == 1:
        print "mono,",
    else:
        print "stereo,",
    
    print w.getsampwidth()*8, "bits,",
    print w.getframerate(), "Hz sampling rate"
    


.. sourcecode:: python

    
    mono, 16 bits, 44100 Hz sampling rate



