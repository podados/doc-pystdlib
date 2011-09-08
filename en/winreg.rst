






The _winreg module
===================




(New in 2.0) This module provides a low-level interface to the Windows
registry database. The interface directly mirrors the underlying
Windows API.


**Example: Using the _winreg module**

.. sourcecode:: python

    
    # File: `winreg-example-1.py <winreg-example-1.py>`__
    
    import _winreg
    
    explorer = _winreg.OpenKey(
        _winreg.HKEY_CURRENT_USER,
        "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer"
        )
    
    # list values owned by this registry key
    try:
        i = 0
        while 1:
            name, value, type = _winreg.EnumValue(explorer, i)
            print repr(name),
            i += 1
    except WindowsError:
        print
    
    value, type = _winreg.QueryValueEx(explorer, "Logon User Name")
    
    print
    print "user is", repr(value)
    


.. sourcecode:: python

    
    $ python winreg-example-1.py
    'Logon User Name' 'CleanShutdown' 'ShellState' 'Shutdown Setting'
    'Reason Setting' 'FaultCount' 'FaultTime' 'IconUnderline' ...
    
    user is u'Effbot'


