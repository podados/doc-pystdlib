






Data Storage
=============




“Unlike mainstream component programming, scripts usually do not
introduce new components but simply “wire” existing ones. Scripts
can be seen as introducing behavior but no new state. /…/ Of course,
there is nothing to stop a “scripting” language from introducing
persistent state — it then simply turns into a normal programming
language”

Clemens Szyperski, in Component Software




.. toctree::

    shelve
    anydbm
    whichdb
    shelve
    dbhash
    dbm
    dumbdbm
    gdbm


Python comes with drivers for a number of very similar database
managers, all modeled after Unix’s **dbm** library. These databases
behaves like ordinary dictionaries, with the exception that you can
only use strings for keys and values (the **`shelve <shelve.htm>`__**
module can handle any kind of value).



Contents
~~~~~~~~


`The anydbm module <anydbm.htm>`__



`The whichdb module <whichdb.htm>`__



`The shelve module <shelve.htm>`__



`The dbhash module <dbhash.htm>`__



`The dbm module <dbm.htm>`__



`The dumbdbm module <dumbdbm.htm>`__



`The gdbm module <gdbm.htm>`__


