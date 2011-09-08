






The unicodedata module
=======================




(New in 2.0) This module contains Unicode character properties, such
as character categories, decomposition data, and numerical values.


**Example: Using the unicodedata module**

.. sourcecode:: python

    
    # File: `unicodedata-example-1.py <unicodedata-example-1.py>`__
    
    import unicodedata
    
    for char in [u"A", u"-", u"1", u"\N{LATIN CAPITAL LETTER O WITH DIAERESIS}"]:
        print repr(char),
        print unicodedata.category(char),
        print repr(unicodedata.decomposition(char)),
        print unicodedata.decimal(char, None),
        print unicodedata.numeric(char, None)
    


.. sourcecode:: python

    
    $ python unicodedata-example-1.py
    u'A' Lu '' None None
    u'-' Pd '' None None
    u'1' Nd '' 1 1.0
    u'Ö' Lu '004F 0308' None None





Note that in Python 2.0, properties for CJK ideographs and Hangul
syllables are missing. This affects characters in the range
0x3400-0x4DB5, 0x4E00-0x9FA5, and 0xAC00-D7A3. The first character in
each range has correct properties, so you can work around this problem
by simply mapping each character to the beginning:


.. sourcecode:: python

    
    def remap(char):
        # fix for broken unicode property database in Python 2.0
        c = ord(char)
        if 0x3400 <= c <= 0x4DB5:
            return unichr(0x3400)
        if 0x4E00 <= c <= 0x9FA5:
            return unichr(0x4E00)
        if 0xAC00 <= c <= 0xD7A3:
            return unichr(0xAC00)
        return char



This bug has been fixed in Python 2.1.


