






The soundex module
===================




(Optional, 1.5.2 only). This module implements a simple hash
algorithm, which converts words to 6-character strings based on their
English pronunciation.



As of version 2.0, this module is no longer included. Several Python
implementations are available on the net, including this one by Skip
Montanaro:

`http://orca.mojam.com/~skip/python/soundex.py
<http://orca.mojam.com/~skip/python/soundex.py>`__
**Example: Using the soundex module**

.. sourcecode:: python

    
    # File: `soundex-example-1.py <soundex-example-1.py>`__
    
    import soundex
    
    a = "fredrik"
    b = "friedrich"
    
    print soundex.get_soundex(a), soundex.get_soundex(b)
    
    print soundex.sound_similar(a, b)
    


.. sourcecode:: python

    
    F63620 F63620
    1



