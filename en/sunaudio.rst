






The sunaudio module
====================




This module identifies Sun AU audio files, and extracts basic
information about the file contents. The **`sunau <sunau.htm>`__**
module provides more complete support for Sun AU files.

**Example: Using the sunaudio module**

.. sourcecode:: python

    
    # File: `sunaudio-example-1.py <sunaudio-example-1.py>`__
    
    import sunaudio
    
    file = "samples/sample.au"
    
    print sunaudio.gethdr(open(file, "rb"))
    


.. sourcecode:: python

    
    (6761, 1, 8012, 1, 'sample.au')



