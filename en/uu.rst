






The uu module
==============




The **UU** encoding scheme is used to convert arbitrary binary data to
plain text. This format is quite popular on the Usenet, but is slowly
being superseded by`base64 <base64.htm>`__ encoding.



A UU encoder takes groups of three bytes (24 bits), and converts each
group to a sequence of four printable characters (6 bits per
character), using characters from chr(32) (space) to chr(95).
Including the length marker and line feed characters, UU encoding
typically expands data by 40%.



An encoded data stream starts with a **begin** line, which also
includes the file privileges (the Unix mode field, as an octal number)
and the filename (or a hyphen, if the name is not known), and ends
with an **end** line:


.. sourcecode:: python

    
    begin 666 sample.jpg
    M_]C_X  02D9)1@ ! 0   0 !  #_VP!#  @&!@<&!0@'!P<)'0@*#!0-# L+
    ...more lines like this...
    end



The **uu** module provides two functions, **encode** and **decode**:



**encode(infile, outfile, filename)** encodes data from the input file
and writes it to the output file. The input and output file arguments
can be either filenames or file objects. The third argument is used as
filename in the **begin** field.

**Example: Using the uu module to encode a binary file**

.. sourcecode:: python

    
    # File: `uu-example-1.py <uu-example-1.py>`__
    
    import uu
    import os, sys
    
    infile = "samples/sample.jpg"
    
    uu.encode(infile, sys.stdout, os.path.basename(infile))
    


.. sourcecode:: python

    
    begin 666 sample.jpg
    M_]C_X  02D9)1@ ! 0   0 !  #_VP!#  @&!@<&!0@'!P<)"0@*#!0-# L+
    M#!D2$P\4'1H?'AT:'!P@)"XG("(L(QP<*#3@R"XS-#+_
    MVP!# 0D)"0P+#!@-#1@R(1PA,C(R,C(R,C(R,C(R,C(R,C(R,C(R,C(R,C(R
    M,C(R,C(R,C(R,C(R,C(R,C(R,C(R,C+_P  1" "  ( # 2(  A$! Q$!_\0 
    M'P   04! 0$! 0$           $" P0%!@<("0H+_\0 M1   @$# P($ P4%




**decode(infile, outfile)** decodes uu-encoded data from the input
text file, and writes it to the output file. Again, both arguments can
be either filenames or file objects.

**Example: Using the uu module to decode a uu-encoded file**

.. sourcecode:: python

    
    # File: `uu-example-2.py <uu-example-2.py>`__
    
    import uu
    import StringIO
    
    infile = "samples/sample.uue"
    outfile = "samples/sample.jpg"
    
    #
    # decode
    
    fi = open(infile)
    fo = StringIO.StringIO()
    
    uu.decode(fi, fo)
    
    #
    # compare with original data file
    
    data = open(outfile, "rb").read()
    
    if fo.getvalue() == data:
        print len(data), "bytes ok"




The **encode** and **decode** functions work with arbitrary file
objects. You can use the ` **StringIO** <stringio.htm>`__ module to
encode and decode texts that you have in memory:

**Example: Using the uu module to encode and decode text strings**

.. sourcecode:: python

    
    # File: uu-example-3.py
    
    import uu
    import StringIO
    
    def uu_encodestring(text):
        fin = StringIO.StringIO(text)
        fout = StringIO.StringIO()
        uu.encode(fin, fout)
        return fout.getvalue()
    
    def uu_decodestring(text):
        fin = StringIO.StringIO(text)
        fout = StringIO.StringIO()
        uu.decode(fin, fout)
        return fout.getvalue()
    
    text = "hello" * 1000
    
    data = uu_encodestring(text)
    text = uu_decodestring(data)



