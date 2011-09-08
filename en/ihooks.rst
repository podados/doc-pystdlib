






The ihooks module
==================




This module provides a framework for import replacements. The idea is
to allow several alternate import mechanisms to co-exist.

**Example: Using the ihooks module**

.. sourcecode:: python

    
    # File: `ihooks-example-1.py <ihooks-example-1.py>`__
    
    import ihooks, imp, os
    
    def import_from(filename):
        "Import module from a named file"
    
        loader = ihooks.BasicModuleLoader()
        path, file = os.path.split(filename)
        name, ext  = os.path.splitext(file)
        m = loader.find_module_in_dir(name, path)
        if not m:
            raise ImportError, name
        m = loader.load_module(name, m)
        return m
    
    colorsys = import_from("/python/lib/colorsys.py")
    
    print colorsys
    


.. sourcecode:: python

    
    



