






The crypt module
=================




(Optional). This module implements one-way DES encryption. Unix
systems use this encryption algorithm to store passwords, and this
module is really only useful to generate or check such passwords.



To encrypt a password, call **crypt.crypt** with the password string,
plus a “salt” , which should consist of two random characters. You
can now throw away the actual password, and just store the encrypted
string somewhere.

**Example: Using the crypt module**

.. sourcecode:: python

    
    # File: `crypt-example-1.py <crypt-example-1.py>`__
    
    import crypt
    
    import random, string
    
    def getsalt(chars = string.letters + string.digits):
        # generate a random 2-character 'salt'
        return random.choice(chars) + random.choice(chars)
    
    print crypt.crypt("bananas", getsalt())
    


.. sourcecode:: python

    
    $ python crypt-example-1.py
    'py8UGrijma1j6'




To verify a given password, encrypt the new password using the two
first characters from the encrypted string as the salt. If the result
matches the encrypted string, the password is valid. The following
example uses the **`pwd <pwd.htm>`__** module to fetch the encrypted
password for a given user.

**Example: Using the crypt module for authentication**

.. sourcecode:: python

    
    # File: `crypt-example-2.py <crypt-example-2.py>`__
    
    import pwd, crypt
    
    def login(user, password):
        "Check if user would be able to login using password"
        try:
            pw1 = pwd.getpwnam(user)[1]
            pw2 = crypt.crypt(password, pw1[:2])
            return pw1 == pw2
        except KeyError:
            return 0 # no such user
    
    user = raw_input("username:")
    password = raw_input("password:")
    
    if login(user, password):
        print "welcome", user
    else:
        print "login failed"




For other ways to implement authentication, see the description of the
**`md5 <md5.htm>`__** module.


