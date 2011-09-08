






The winsound module
====================




(Windows only). This module allows you to play Wave sound files on a
Windows machine.

**Example: Using the winsound module**

.. sourcecode:: python

    
    # File: `winsound-example-1.py <winsound-example-1.py>`__
    
    import winsound
    
    file = "samples/sample.wav"
    
    winsound.PlaySound(
        file,
        winsound.SND_FILENAME|winsound.SND_NOWAIT,
        )



