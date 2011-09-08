






The htmlentitydefs module
==========================




This module contains a dictionary with lots of ISO Latin 1 character
entities used by HTML.

**Example: Using the htmlentitydefs module**

.. sourcecode:: python

    
    # File: `htmlentitydefs-example-1.py <htmlentitydefs-example-1.py>`__
    
    import htmlentitydefs
    
    entities = htmlentitydefs.entitydefs
    
    for entity in "amp", "quot", "copy", "yen":
        print entity, "=", entities[entity]
    


.. sourcecode:: python

    
    $ python htmlentitydefs-example-1.py
    amp = &
    quot = "
    copy = ©
    yen = ¥




The following example shows how to combine regular expressions with
this dictionary to translate entities in a string (the opposite of
**cgi.escape**):

**Example: Using the htmlentitydefs module to translate entities**

.. sourcecode:: python

    
    # File: `htmlentitydefs-example-2.py <htmlentitydefs-example-2.py>`__
    
    import htmlentitydefs
    import re
    import cgi
    
    pattern = re.compile("&(\w+?);")
    
    def descape_entity(m, defs=htmlentitydefs.entitydefs):
        # callback: translate one entity to its ISO Latin value
        try:
            return defs[m.group(1)]
        except KeyError:
            return m.group(0) # use as is
    
    def descape(string):
        return pattern.sub(descape_entity, string)
    
    print descape("<spam&eggs>")
    print descape(cgi.escape(""))
    


.. sourcecode:: python

    
    $ python htmlentitydefs-example-2.py
    
    




Finally, the following example shows how to use translate reserved XML
characters and ISO Latin 1 characters to an XML string. This is
similar to **cgi.escape**, but it also replaces non-ASCII characters.


**Example: Escaping ISO Latin 1 entities**

.. sourcecode:: python

    
    # File: `htmlentitydefs-example-3.py <htmlentitydefs-example-3.py>`__
    
    import htmlentitydefs
    import re, string
    
    # this pattern matches substrings of reserved and non-ASCII characters
    pattern = re.compile(r"[&\"\x80-\xff]+")
    
    # create character map
    entity_map = {}
    
    for i in range(256):
        entity_map[chr(i)] = "&#%d;" % i
    
    for entity, char in htmlentitydefs.entitydefs.items():
        if entity_map.has_key(char):
            entity_map[char] = "&%s;" % entity
    
    def escape_entity(m, get=entity_map.get):
        return string.join(map(get, m.group()), "")
    
    def escape(string):
        return pattern.sub(escape_entity, string)
    
    print escape("")
    print escape("å i åa ä e ö")


.. sourcecode:: python

    
    $ python htmlentitydefs-example-3.py
    <spam&eggs>
     i a  e 


