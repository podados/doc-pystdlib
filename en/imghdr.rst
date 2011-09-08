






The imghdr module
==================




This module identifies different image file formats. The current
version identifies **bmp**, **gif**, **jpeg**, **pbm**, **pgm**,
**png**, **ppm**, **rast** (Sun raster), **rgb** (SGI), **tiff**, and
**xbm** images.

**Example: Using the imghdr module**

.. sourcecode:: python

    
    # File: `imghdr-example-1.py <imghdr-example-1.py>`__
    
    import imghdr
    
    result = imghdr.what("samples/sample.jpg")
    
    if result:
        print "file format:", result
    else:
        print "cannot identify file"
    


.. sourcecode:: python

    
    file format: jpeg



.. sourcecode:: python

    
    import Image
    
    im = Image.open("samples/sample.jpg")
    print im.format, im.mode, im.size


