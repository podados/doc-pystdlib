






The gzip module
================




This module allows you to read and write gzip-compressed files as if
they were ordinary files.

**Example: Using the gzip module to read a compressed file**

.. sourcecode:: python

    
    # File: `gzip-example-1.py <gzip-example-1.py>`__
    
    import gzip
    
    file = gzip.GzipFile("samples/sample.gz")
    
    print file.read()
    


.. sourcecode:: python

    
    Well it certainly looks as though we're in for
    a splendid afternoon's sport in this the 127th
    Upperclass Twit of the Year Show.




The standard implementation doesn’t support the **seek** and
**tell** methods. The following example shows how to add forward
seeking:


**Example: Extending the gzip module to support seek/tell**

.. sourcecode:: python

    
    # File: `gzip-example-2.py <gzip-example-2.py>`__
    
    import gzip
    
    class gzipFile(gzip.GzipFile):
        # adds seek/tell support to GzipFile
    
        offset = 0
    
        def read(self, size=None):
            data = gzip.GzipFile.read(self, size)
            self.offset = self.offset + len(data)
            return data
    
        def seek(self, offset, whence=0):
            # figure out new position (we can only seek forwards)
            if whence == 0:
                position = offset
            elif whence == 1:
                position = self.offset + offset
            else:
                raise IOError, "Illegal argument"
            if position < self.offset:
                raise IOError, "Cannot seek backwards"
    
            # skip forward, in 16k blocks
            while position > self.offset:
                if not self.read(min(position - self.offset, 16384)):
                    break
    
        def tell(self):
            return self.offset
    
    #
    # try it
    
    file = gzipFile("samples/sample.gz")
    file.seek(80)
    
    print file.read()
    


.. sourcecode:: python

    
    this the 127th
    Upperclass Twit of the Year Show.


