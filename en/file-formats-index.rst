






File Formats
=============






.. toctree::

    sgmllib
    htmllib
    formatter
    xmllib
    xml-parsers-expat
    configparser
    netrc
    shlex
    gzip
    zipfile
    zlib
    xmllib
    xml-parsers-expat
    sgmllib
    htmllib
    htmlentitydefs
    formatter
    configparser
    netrc
    shlex
    zipfile
    gzip


This chapter describes a number of modules that are used to parse
different file formats.



Markup Languages
~~~~~~~~~~~~~~~~


Python comes with extensive support for the Extensible Markup Language
XML and Hypertext Markup Language (HTML) file formats. Python also
provides basic support for Standard Generalized Markup Language
(SGML).



All these formats share the same basic structure (this isn’t so
strange, since both HTML and XML are derived from SGML). Each document
contains a mix of start tags , end tags , plain text (also called
character data), and entity references .


.. sourcecode:: python

This is a header This is the body text. The text can contain plain
text ("character data"), tags, and entities.
    
    



In the above example, ** **, ** **, and **

** are start tags. For each start tag, there’s a corresponding end
tag which looks similar, but has a slash before the tag name. The
start tag can also contain one or more attributes , like the **name**
attribute in this example.



Everything between a start tag and its matching end tag is called an
element . In the above example, the **document** element contains two
other elements, **header** and **body**.



Finally, **"** is a character entity. It is used to represent reserved
characters in the text sections (in this case, it’s an ampersand (
**&**) which is used to start the entity itself. Other common entities
include **<** for “less than” ( **<**), and **>** for “greater
than” ( **>**).



While XML, HTML, and SGML all share the same building blocks, there
are important differences between them. In XML, all elements must have
both start tags and end tags, and the tags must be properly nested (if
they are, the document is said to be well-formed ). In addition, XML
is case-sensitive, so ** ** and ** ** are two different element types.



HTML, in contrast, is much more flexible. The HTML parser can often
fill in missing tags; for example, if you open a new paragraph in HTML
using the **




** tag without closing the previous paragraph, the parser
automatically adds a ****

end tag. HTML is also case-insensitive. On the other hand, XML allows
you to define your own elements, while HTML uses a fixed element set,
as defined by the HTML specifications.


SGML is even more flexible. In its full incarnation, you can use a
custom declaration to define how to translate the source text into an
element structure, and a document type description (DTD) to validate
the structure, and fill in missing tags. Technically, both HTML and
XML are SGML applications ; they both have their own SGML declaration,
and HTML also has a standard DTD.



Python comes with parsers for all markup flavors. While SGML is the
most flexible of the formats, Python’s **`sgmllib <sgmllib.htm>`__**
parser is actually pretty simple. It avoids most of the problems by
only understanding enough of the SGML standard to be able to deal with
HTML. It doesn’t handle document type descriptions either; instead,
you can customize the parser via subclassing.



The HTML support is built on top of the SGML parser. The **`htmllib
<htmllib.htm>`__** parser delegates the actual rendering to a
formatter object. The **`formatter <formatter.htm>`__** module
contains a couple of standard formatters.



The XML support is most complex. In Python 1.5.2, the built-in support
was limited to the **`xmllib <xmllib.htm>`__** parser, which is pretty
similar to the **sgmllib** module (with one important difference;
**xmllib** actually tries to support the entire XML standard).



Python 2.0 comes with more advanced XML tools, based on the optional
**`expat <xml-parsers-expat.htm>`__** parser.



Configuration Files
~~~~~~~~~~~~~~~~~~~


The **`ConfigParser <configparser.htm>`__** module reads and writes a
simple configuration file format, similar to Windows INI files.



The **`netrc <netrc.htm>`__** module reads **.netrc** configuration
files, and the **`shlex <shlex.htm>`__** module can be used to read
any configuration file using a shell script-like syntax.



Archive Formats
~~~~~~~~~~~~~~~


Python’s standard library also provides support for the popular GZIP
and ZIP (2.0 only) formats. The ` **gzip** <gzip.htm>`__ module can
read and write GZIP files, and the ` **zipfile** <zipfile.htm>`__
reads and writes ZIP files. Both modules depend on the ` **zlib**
<zlib.htm>`__ data compression module.



Contents
~~~~~~~~


`The xmllib module <xmllib.htm>`__



`The xml.parsers.expat module <xml-parsers-expat.htm>`__



`The sgmllib module <sgmllib.htm>`__



`The htmllib module <htmllib.htm>`__



`The htmlentitydefs module <htmlentitydefs.htm>`__



`The formatter module <formatter.htm>`__



`The ConfigParser module <configparser.htm>`__



`The netrc module <netrc.htm>`__



`The shlex module <shlex.htm>`__



`The zipfile module <zipfile.htm>`__



`The gzip module <gzip.htm>`__


