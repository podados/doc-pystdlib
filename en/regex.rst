






The regex module
=================




(Obsolete) This is the old (pre-1.5) regular expression machinery. New
code should use **`re <re.htm>`__** where possible.



Note that **regex** is often faster than the **re** module used in
Python 1.5.2, but slower than the new version used in 1.6 and later.


**Example: Using the regex module**

.. sourcecode:: python

    
    # File: `regex-example-1.py <regex-example-1.py>`__
    
    import regex
    
    text = "Man's crisis of identity in the latter half of the 20th century"
    
    p = regex.compile("latter") # literal
    print p.match(text)
    print p.search(text), repr(p.group(0))
    
    p = regex.compile("[0-9]+") # number
    print p.search(text), repr(p.group(0))
    
    p = regex.compile("\<\w\w\>") # two-letter word
    print p.search(text), repr(p.group(0))
    
    p = regex.compile("\w+$") # word at the end
    print p.search(text), repr(p.group(0))
    


.. sourcecode:: python

    
    $ python regex-example-1.py
    -1
    32 'latter'
    51 '20'
    13 'of'
    56 'century'


