






The cPickle module
===================




(Optional). This module contains a faster reimplementation of the
**`pickle <pickle.htm>`__** module.


**Example: Using the cPickle module**

.. sourcecode:: python

    
    # File: `cpickle-example-1.py <cpickle-example-1.py>`__
    
    try:
        import cPickle as pickle
    except ImportError:
        import pickle # fall back on Python version
    
    class Sample:
        def __init__(self, value):
            self.value = value
    
    sample = Sample(1)
    
    data = pickle.dumps(sample)
    
    print pickle
    print repr(data)
    


.. sourcecode:: python

    
    
    "(i__main__\012Sample\012p1\012(dp2\012S'value'\012p3\012I1\012sb."


