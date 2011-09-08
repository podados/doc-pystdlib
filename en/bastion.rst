






The Bastion module
===================




**Note:** This module is not safe in Python 2.2 and later, and has
been removed in Python 2.3.



This module allows you to control how a given object is used. It can
be used to pass objects from unrestricted parts of your application to
code running in restricted mode.



To create a restricted instance, simply call the **Bastion** wrapper.
By default, all instance variables are hidden, as well as all methods
that start with an underscore.

**Example: Using the Bastion module**

.. sourcecode:: python

    
    # File: `bastion-example-1.py <bastion-example-1.py>`__
    
    import Bastion
    
    class Sample:
        value = 0
    
        def _set(self, value):
            self.value = value
    
        def setvalue(self, value):
            if 10 < value <= 20:
                self._set(value)
            else:
                raise ValueError, "illegal value"
    
        def getvalue(self):
            return self.value
    
    #
    # try it
    
    s = Sample()
    s._set(100) # cheat
    print s.getvalue()
    
    s = Bastion.Bastion(Sample())
    s._set(100) # attempt to cheat
    print s.getvalue()
    


.. sourcecode:: python

    
    100
    Traceback (innermost last):
    ...
    AttributeError: _set




You can control which functions to publish. In the following example,
the internal method can be called from outside, but the **getvalue**
no longer works:

**Example: Using the Bastion module with a non-standard filter**

.. sourcecode:: python

    
    # File: `bastion-example-2.py <bastion-example-2.py>`__
    
    import Bastion
    
    class Sample:
        value = 0
    
        def _set(self, value):
            self.value = value
    
        def setvalue(self, value):
            if 10 < value <= 20:
                self._set(value)
            else:
                raise ValueError, "illegal value"
    
        def getvalue(self):
            return self.value
    
    #
    # try it
    
    def is_public(name):
        return name[:3] != "get"
    
    s = Bastion.Bastion(Sample(), is_public)
    s._set(100) # this works
    print s.getvalue() # but not this
    


.. sourcecode:: python

    
    100
    Traceback (innermost last):
    ...
    AttributeError: getvalue



