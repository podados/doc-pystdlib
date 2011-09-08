






The dircmp module
==================




(Obsolete, only in 1.5.2). This module provides a class that can be
used to compare the contents of two disk directories.


**Example: Using the dircmp module**

.. sourcecode:: python

    
    # File: `dircmp-example-1.py <dircmp-example-1.py>`__
    
    import dircmp
    
    d = dircmp.dircmp()
    d.new("samples", "oldsamples")
    d.run()
    d.report()
    


.. sourcecode:: python

    
    $ python dircmp-example-1.py
    diff samples oldsamples
    Only in samples : ['sample.aiff', 'sample.au', 'sample.wav']
    Identical files : ['sample.gif', 'sample.gz', 'sample.jpg', ...]





In Python 2.0 and later, this module has been replaced by the
**`filecmp <filecmp.htm>`__** module.


