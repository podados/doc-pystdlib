






The quopri module
==================




This module implements quoted printable encoding, according to the
MIME standard.



This encoding can be used if you need to convert text messages which
mostly consists of plain US ASCII text, such as messages written in
most European languages, to messages that only use US ASCII. This can
be quite useful if you’re sending stuff via steam-powered mail
transports to people using vintage mail agents.


**Example: Using the quopri module**

.. sourcecode:: python

    
    # File: `quopri-example-1.py <quopri-example-1.py>`__
    
    import quopri
    import StringIO
    
    # helpers (the quopri module only supports file-to-file conversion)
    
    def encodestring(instring, tabs=0):
        outfile = StringIO.StringIO()
        quopri.encode(StringIO.StringIO(instring), outfile, tabs)
        return outfile.getvalue()
    
    def decodestring(instring):
        outfile = StringIO.StringIO()
        quopri.decode(StringIO.StringIO(instring), outfile)
        return outfile.getvalue()
    
    #
    # try it out
    
    MESSAGE = "å i åa ä e ö!"
    
    encoded_message = encodestring(MESSAGE)
    decoded_message = decodestring(encoded_message)
    
    print "original:", MESSAGE
    print "encoded message:", repr(encoded_message)
    print "decoded message:", decoded_message
    


.. sourcecode:: python

    
    original: å i åa ä e ö!
    encoded message: '=E5 i =E5a =E4 e =F6!\012'
    decoded message: å i åa ä e ö!





As this example shows, non-US characters are mapped to an ‘=’
followed by two hexadecimal digits. So is the ‘=’ character itself
( “=3D” ), as well as whitespace at the end of lines ( “=20”
). Everything else looks just like before. So provided you don’t use
too many weird characters, the encoded string is nearly as readable as
the original.



(Europeans generally hate this encoding, and strongly believe that
certain US programmers deserve to be slapped in the head with a huge
great fish to the jolly music of Edward German…)


