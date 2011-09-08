






The UserList module
====================




This module contains a list class which can be subclassed (simply a
Python wrapper for the built-in list type).



In the following example, **AutoList** instances work just like
ordinary lists, except that they allow you to insert items at the end
by assigning to it.

**Example: Using the UserList module**

.. sourcecode:: python

    
    # File: `userlist-example-1.py <userlist-example-1.py>`__
    
    import UserList
    
    class AutoList(UserList.UserList):
    
        def __setitem__(self, i, item):
            if i == len(self.data):
                self.data.append(item)
            else:
                self.data[i] = item
    
    list = AutoList()
    
    for i in range(10):
        list[i] = i
    
    print list
    


.. sourcecode:: python

    
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



