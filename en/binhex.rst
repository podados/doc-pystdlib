






The binhex module
==================




This module converts to and from the Macintosh binhex format.


**Example: Using the binhex module**

.. sourcecode:: python

    
    # File: `binhex-example-1.py <binhex-example-1.py>`__
    
    import binhex
    import sys
    
    infile = "samples/sample.jpg"
    
    binhex.binhex(infile, sys.stdout)
    


.. sourcecode:: python

    
    $ python binhex-example-1.py
    (This file must be converted with BinHex 4.0)
    
    :#R0KEA"XC5jUF'F!2j!)!*!%%TS!N!4RdrrBrq!!%%T'58B!!3%!!!%!!3!!rpX
    !3`!)"JB("J8)"`F(#3N)#J`8$3`,#``C%K-2&"dD(aiG'K`F)#3Z*b!L,#-F(#J
    h+5``-63d0"mR16di-M`Z-c3brpX!3`%*#3N-#``B$3dB-L%F)6+3-[r!!"%)!)!
    !J!-")J!#%3%$%3(ra!!I!!!""3'3"J#3#!%#!`3&"JF)#3S,rm3!Y4!!!J%$!`)
    %!`8&"!3!!!!3)$!!34"4)K-8%'%e"b*a&$+"ND%))d+a`495dI!N-f*bJJN


