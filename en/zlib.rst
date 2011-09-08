






The zlib module
================




(Optional). This module provides support for “zlib” compression.
(This compression method is also known as “deflate” .)



The **compress** and **decompress** functions take string arguments:

**Example: Using the zlib module to compress a string**

.. sourcecode:: python

    
    # File: `zlib-example-1.py <zlib-example-1.py>`__
    
    import zlib
    
    MESSAGE = "life of brian"
    
    compressed_message = zlib.compress(MESSAGE)
    decompressed_message = zlib.decompress(compressed_message)
    
    print "original:", repr(MESSAGE)
    print "compressed message:", repr(compressed_message)
    print "decompressed message:", repr(decompressed_message)
    


.. sourcecode:: python

    
    $ python zlib-example-1.py
    original: 'life of brian'
    compressed message: 'x\234\313\311LKU\310OSH*
    \312L\314\003\000!\010\004\302'
    decompressed message: 'life of brian'




The compression rate varies a lot, depending on the contents of the
file.

**Example: Using the zlib module to compress a group of files**

.. sourcecode:: python

    
    # File: `zlib-example-2.py <zlib-example-2.py>`__
    
    import zlib
    import glob
    
    for file in glob.glob("samples/*"):
    
        indata = open(file, "rb").read()
        outdata = zlib.compress(indata, zlib.Z_BEST_COMPRESSION)
    
        print file, len(indata), "=>", len(outdata),
        print "%d%%" % (len(outdata) * 100 / len(indata))
    


.. sourcecode:: python

    
    $ python zlib-example-2.py
    samples\sample.au 1676 => 1109 66%
    samples\sample.gz 42 => 51 121%
    samples\sample.htm 186 => 135 72%
    samples\sample.ini 246 => 190 77%
    samples\sample.jpg 4762 => 4632 97%
    samples\sample.msg 450 => 275 61%
    samples\sample.sgm 430 => 321 74%
    samples\sample.tar 10240 => 125 1%
    samples\sample.tgz 155 => 159 102%
    samples\sample.txt 302 => 220 72%
    samples\sample.wav 13260 => 10992 82%




You can also compress or decompress data on the fly:

**Example: Using the zlib module to decompress streams**

.. sourcecode:: python

    
    # File: `zlib-example-3.py <zlib-example-3.py>`__
    
    import zlib
    
    encoder = zlib.compressobj()
    
    data = encoder.compress("life")
    data = data + encoder.compress(" of ")
    data = data + encoder.compress("brian")
    data = data + encoder.flush()
    
    print repr(data)
    print repr(zlib.decompress(data))
    


.. sourcecode:: python

    
    $ python zlib-example-3.py
    'x\234\313\311LKU\310OSH*\312L\314\003\000!\010\004\302'
    'life of brian'




To make it a bit more convenient to read a compressed file, you can
wrap a decoder object in a file-like wrapper:


**Example: Emulating a file object for compressed streams**

.. sourcecode:: python

    
    # File: `zlib-example-4.py <zlib-example-4.py>`__
    
    import zlib
    import string, StringIO
    
    class ZipInputStream:
    
        def __init__(self, file):
            self.file = file
            self.__rewind()
    
        def __rewind(self):
            self.zip = zlib.decompressobj()
            self.pos = 0 # position in zipped stream
            self.offset = 0 # position in unzipped stream
            self.data = ""
    
        def __fill(self, bytes):
            if self.zip:
                # read until we have enough bytes in the buffer
                while not bytes or len(self.data) < bytes:
                    self.file.seek(self.pos)
                    data = self.file.read(16384)
                    if not data:
                        self.data = self.data + self.zip.flush()
                        self.zip = None # no more data
                        break
                    self.pos = self.pos + len(data)
                    self.data = self.data + self.zip.decompress(data)
    
        def seek(self, offset, whence=0):
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
    
        def read(self, bytes = 0):
            self.__fill(bytes)
            if bytes:
                data = self.data[:bytes]
                self.data = self.data[bytes:]
            else:
                data = self.data
                self.data = ""
            self.offset = self.offset + len(data)
            return data
    
        def readline(self):
            # make sure we have an entire line
            while self.zip and "\n" not in self.data:
                self.__fill(len(self.data) + 512)
            i = string.find(self.data, "\n") + 1
            if i <= 0:
                return self.read()
            return self.read(i)
    
        def readlines(self):
            lines = []
            while 1:
                s = self.readline()
                if not s:
                    break
                lines.append(s)
            return lines
    
    #
    # try it out
    
    data = open("samples/sample.txt").read()
    data = zlib.compress(data)
    
    file = ZipInputStream(StringIO.StringIO(data))
    for line in file.readlines():
        print line[:-1]
    


.. sourcecode:: python

    
    $ python zlib-example-4.py
    We will perhaps eventually be writing only small
    modules which are identified by name as they are
    used to build larger ones, so that devices like
    indentation, rather than delimiters, might become
    feasible for expressing local structure in the
    source language.
        -- Donald E. Knuth, December 1974


