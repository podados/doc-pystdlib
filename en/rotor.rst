






The rotor module
=================




(Optional). This module implements a simple encryption algorithm,
based on the WWII Enigma engine. This algorithm isn’t exactly
strong, and shouldn’t be used for any serious cryptography work.

**Example: Using the rotor module**

.. sourcecode:: python

    
    # File: `rotor-example-1.py <rotor-example-1.py>`__
    
    import rotor
    
    SECRET_KEY = "spam"
    MESSAGE = "the holy grail"
    
    r = rotor.newrotor(SECRET_KEY)
    
    encoded_message = r.encrypt(MESSAGE)
    decoded_message = r.decrypt(encoded_message)
    
    print "original:", repr(MESSAGE)
    print "encoded message:", repr(encoded_message)
    print "decoded message:", repr(decoded_message)
    


.. sourcecode:: python

    
    $ python rotor-example-1.py
    original: 'the holy grail'
    encoded message: '\227\271\244\015\305sw\3340\337\252\237\340U'
    decoded message: 'the holy grail'



