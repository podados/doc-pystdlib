






More Standard Modules
======================




“Now, imagine that your friend kept complaining that she didn’t
want to visit you since she found it too hard to climb up the drain
pipe, and you kept telling her to use the friggin’ stairs like
everyone else…”

eff-bot, June 1998




.. toctree::

    fileinput
    stringio
    cstringio
    userdict
    userlist
    userstring
    random
    whrandom
    sha
    crypt
    rotor
    fileinput
    shutil
    tempfile
    stringio
    cstringio
    mmap
    userdict
    userlist
    userstring
    traceback
    errno
    getopt
    getpass
    glob
    fnmatch
    random
    whrandom
    sha
    crypt
    rotor
    zlib
    code


This chapter describes a number of modules that are used in many
Python programs. It’s perfectly possible to write large Python
programs without using them, but they can help you save a lot of time
and effort.



Files and streams
~~~~~~~~~~~~~~~~~


The **`fileinput <fileinput.htm>`__** module makes it easy to write
different kinds of text filters. This module provides a wrapper class,
which lets you use a simple **for-in** statement to loop over the
contents of one or more text files.



The **`StringIO <stringio.htm>`__** module (and the **`cStringIO
<cstringio.htm>`__** variant) implements an in-memory file object. You
can use **StringIO** objects in many places where Python expects an
ordinary file object.



Type wrappers
~~~~~~~~~~~~~


**`UserDict <userdict.htm>`__**, **`UserList <userlist.htm>`__**, and
**`UserString <userstring.htm>`__** are thin wrappers on top of the
corresponding built-in types. But unlike the built-in types, these
wrappers can be subclassed. This can come in handy if you need a class
that works almost like a built-in type, but has one or more extra
methods.



Random numbers
~~~~~~~~~~~~~~


The **`random <random.htm>`__** module provides a number of different
random number generators. The **`whrandom <whrandom.htm>`__** module
is similar, but it also allows you to create multiple generator
objects.



Digests and encryption algorithms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


The **`md5 <md5.htm>`__** and **`sha <sha.htm>`__** modules are used
to calculate cryptographically strong message signatures (so-called
“message digests” ).



The **`crypt <crypt.htm>`__** module implements a DES-style one-way
encryption. This module is usually only available on Unix systems.



The **`rotor <rotor.htm>`__** module provides simple two-way
encryption.



Contents
~~~~~~~~


`The fileinput module <fileinput.htm>`__



`The shutil module <shutil.htm>`__



`The tempfile module <tempfile.htm>`__



`The StringIO module <stringio.htm>`__



`The cStringIO module <cstringio.htm>`__



`The mmap module <mmap.htm>`__



`The UserDict module <userdict.htm>`__



`The UserList module <userlist.htm>`__



`The UserString module <userstring.htm>`__



`The traceback module <traceback.htm>`__



`The errno module <errno.htm>`__



`The getopt module <getopt.htm>`__



`The getpass module <getpass.htm>`__



`The glob module <glob.htm>`__



`The fnmatch module <fnmatch.htm>`__



`The random module <random.htm>`__



`The whrandom module <whrandom.htm>`__



`The md5 module <md5.htm>`__



`The sha module <sha.htm>`__



`The crypt module <crypt.htm>`__



`The rotor module <rotor.htm>`__



`The zlib module <zlib.htm>`__



`The code module <code.htm>`__


