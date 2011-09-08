






Data Representation
====================




“PALO ALTO, Calif. — Intel says its Pentium Pro and new Pentium II
chips have a flaw that can cause computers to sometimes make mistakes
but said the problems could be fixed easily with rewritten software”

from a Reuters telegram




.. toctree::

    struct
    array
    marshal
    pickle
    cpickle
    pprint
    repr
    binhex
    quopri
    uu
    array
    struct
    xdrlib
    marshal
    pickle
    cpickle
    copy-reg
    pprint
    repr
    binhex
    quopri
    uu
    binascii


This chapter describes a number of modules that can be used to convert
between Python objects and other data representations. They are often
used to read and write foreign file formats, and to store or transfer
Python variables.



Binary data
~~~~~~~~~~~


Python provides several support modules that help you decode and
encode binary data formats. The **`struct <struct.htm>`__** module can
convert between binary data structures (like C structs) and Python
tuples. The **`array <array.htm>`__** module wraps binary arrays of
data (C arrays) into a Python sequence object.



Self-describing formats
~~~~~~~~~~~~~~~~~~~~~~~


To pass data between different Python programs, you can **`marshal
<marshal.htm>`__** or **`pickle <pickle.htm>`__** your data.



The **marshal** module uses a simple self-describing format which
supports most built-in data types, including code objects. Python uses
this format itself, to store compiled code on disk (in PYC files).



The **pickle** module provides a more sophisticated format, which
supports user-defined classes, self-referencing data structures, and
more. This module is available in two versions; the basic **pickle**
module is written in Python, and is relatively slow, while **`cPickle
<cpickle.htm>`__** is written in C, and is usually as fast as
**marshal**.



Output formatting
~~~~~~~~~~~~~~~~~


This group of modules supplement built-in formatting functions like
**repr**, and the **%** string formatting operator.



The **`pprint <pprint.htm>`__** module can print almost any Python
data structure in a nice, readable way (well, as readable as it can
make things, that is).



The **`repr <repr.htm>`__** module provides a replacement for the
built-in function with the same name. The version in this module
applies tight limits on most things; it doesn’t print more than 30
characters from each string, it doesn’t print more than a few levels
of deeply nested data structures, etc.



Encoded binary data
~~~~~~~~~~~~~~~~~~~


Python supports most common binary encodings, such as **`base64
<base64.htm>`__**, **`binhex <binhex.htm>`__** (a macintosh format),
**`quoted printable <quopri.htm>`__**, and **`uu <uu.htm>`__**
encoding.



Contents
~~~~~~~~


`The array module <array.htm>`__



`The struct module <struct.htm>`__



`The xdrlib module <xdrlib.htm>`__



`The marshal module <marshal.htm>`__



`The pickle module <pickle.htm>`__



`The cPickle module <cpickle.htm>`__



`The copy_reg module <copy-reg.htm>`__



`The pprint module <pprint.htm>`__



`The repr module <repr.htm>`__



`The base64 module <base64.htm>`__



`The binhex module <binhex.htm>`__



`The quopri module <quopri.htm>`__



`The uu module <uu.htm>`__



`The binascii module <binascii.htm>`__


