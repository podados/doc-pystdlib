






The copy_reg module
====================




This module provides a registry that you can use to register your own
extension types. The **`pickle <pickle.htm>`__** and **`copy
<copy.htm>`__** modules use this registry to figure out how to process
non-standard types.



For example, the standard **`pickle <pickle.htm>`__** implementation
cannot deal with Python code objects, as shown by the following
example:



.. sourcecode:: python

    
    # File: `copy-reg-example-1.py <copy-reg-example-1.py>`__
    
    import pickle
    
    CODE = """
    print 'good evening'
    """
    
    code = compile(CODE, "", "exec")
    
    exec code
    exec pickle.loads(pickle.dumps(code))
    


.. sourcecode:: python

    
    good evening
    Traceback (innermost last):
    ...
    pickle.PicklingError: can't pickle 'code' objects




You can work around this by registering a code object handler. Such a
handler consists of two parts; a pickler which takes the code object
and returns a tuple that can only contain simple data types, and an
unpickler which takes the contents of such a tuple as its arguments:

**Example: Using the copy_reg module to enable pickling of code
objects**

.. sourcecode:: python

    
    # File: `copy-reg-example-2.py <copy-reg-example-2.py>`__
    
    import copy_reg
    import pickle, marshal, types
    
    #
    # register a pickle handler for code objects
    
    def code_unpickler(data):
        return marshal.loads(data)
    
    def code_pickler(code):
        return code_unpickler, (marshal.dumps(code),)
    
    copy_reg.pickle(types.CodeType, code_pickler, code_unpickler)
    
    #
    # try it out
    
    CODE = """
    print "suppose he's got a pointed stick"
    """
    
    code = compile(CODE, "", "exec")
    
    exec code
    exec pickle.loads(pickle.dumps(code))
    


.. sourcecode:: python

    
    suppose he's got a pointed stick
    suppose he's got a pointed stick




If you’re transferring the pickled data across a network, or to
another program, the custom unpickler must of course be available at
the receiving end as well.



For the really adventurous, here’s a version that makes it possible
to pickle open file objects:

**Example: Using the copy_reg module to enable pickling of file
objects**

.. sourcecode:: python

    
    # File: `copy-reg-example-3.py <copy-reg-example-3.py>`__
    
    import copy_reg
    import pickle, types
    import StringIO
    
    #
    # register a pickle handler for file objects
    
    def file_unpickler(position, data):
        file = StringIO.StringIO(data)
        file.seek(position)
        return file
    
    def file_pickler(code):
        position = file.tell()
        file.seek(0)
        data = file.read()
        file.seek(position)
        return file_unpickler, (position, data)
    
    copy_reg.pickle(types.FileType, file_pickler, file_unpickler)
    
    #
    # try it out
    
    file = open("samples/sample.txt", "rb")
    
    print file.read(120),
    print "",
    print pickle.loads(pickle.dumps(file)).read()
    


.. sourcecode:: python

    
    We will perhaps eventually be writing only small
    modules which are identified by name as they are
    used to build larger   ones, so that devices like
    indentation, rather than delimiters, might become
    feasible for expressing local structure in the
    source language.
         -- Donald E. Knuth, December 1974



