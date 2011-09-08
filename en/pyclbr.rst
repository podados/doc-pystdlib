






The pyclbr module
==================




This module contains a basic Python class parser.



In 1.5.2, the module exports a single function, **readmodule**, which
parses a given module, and returns a list of all classes defined at
the module’s top level.

**Example: Using the pyclbr module**

.. sourcecode:: python

    
    # File: `pyclbr-example-1.py <pyclbr-example-1.py>`__
    
    import pyclbr
    
    mod = pyclbr.readmodule("cgi")
    
    for k, v in mod.items():
        print k, v
    


.. sourcecode:: python

    
    MiniFieldStorage 
    InterpFormContentDict 
    FieldStorage 
    SvFormContentDict 
    StringIO 
    FormContent 
    FormContentDict 




In 2.0 and later, there’s also an alternative interface,
**readmodule_ex**, which returns global functions as well.

**Example: Using the pyclbr module to read classes and functions**

.. sourcecode:: python

    
    # File: `pyclbr-example-3.py <pyclbr-example-3.py>`__
    
    import pyclbr
    
    # available in Python 2.0 and later
    mod = pyclbr.readmodule_ex("cgi")
    
    for k, v in mod.items():
        print k, v
    


.. sourcecode:: python

    
    MiniFieldStorage 
    parse_header 
    test 
    print_environ_usage 
    parse_multipart 
    FormContentDict 
    initlog 
    parse 
    StringIO 
    SvFormContentDict 
    ...




To get more information about each class, use the various attributes
in the **Class** instances:


**Example: Using the pyclbr module**

.. sourcecode:: python

    
    # File: `pyclbr-example-2.py <pyclbr-example-2.py>`__
    
    import pyclbr
    import string
    
    mod = pyclbr.readmodule("cgi")
    
    def dump(c):
        # print class header
        s = "class " + c.name
        if c.super:
            s = s +  "(" + string.join(map(lambda v: v.name, c.super), ", ") + ")"
        print s + ":"
        # print method names, sorted by line number
        methods = c.methods.items()
        methods.sort(lambda a, b: cmp(a[1], b[1]))
        for method, lineno in methods:
            print "  def " + method
        print
    
    for k, v in mod.items():
        dump(v)
    


.. sourcecode:: python

    
    class MiniFieldStorage:
      def __init__
      def __repr__
    
    class InterpFormContentDict(SvFormContentDict):
      def __getitem__
      def values
      def items
    
    ...


