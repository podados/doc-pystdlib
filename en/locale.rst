






The locale module
==================




This module provides an interface to C’s localization functions. It
also provides functions to convert between numbers and strings based
on the current locale (functions like **int** and **float**, as well
as the numeric conversion functions in **string**, are not affected by
the current locale).

**Example: Using the locale module for data formatting**

.. sourcecode:: python

    
    # File: `locale-example-1.py <locale-example-1.py>`__
    
    import locale
    
    print "locale", "=>", locale.setlocale(locale.LC_ALL, "")
    
    # integer formatting
    value = 4711
    print locale.format("%d", value, 1), "==",
    print locale.atoi(locale.format("%d", value, 1))
    
    # floating point
    value = 47.11
    print locale.format("%f", value, 1), "==",
    print locale.atof(locale.format("%f", value, 1))
    
    info = locale.localeconv()
    print info["int_curr_symbol"]
    


.. sourcecode:: python

    
    locale => Swedish_Sweden.1252
    4 711 == 4711
    47,110000 == 47.11
    SEK






**Example: Using the locale module to get the platform locale**

.. sourcecode:: python

    
    # File: `locale-example-2.py <locale-example-2.py>`__
    
    import locale
    
    language, encoding = locale.getdefaultlocale()
    
    print "language", language
    print "encoding", encoding
    


.. sourcecode:: python

    
    language sv_SE
    encoding cp1252



