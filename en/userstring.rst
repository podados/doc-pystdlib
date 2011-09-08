






The UserString module
======================




(New in 2.0) This module contains two classes, **UserString** and
**MutableString**. The former is a wrapper for the standard string
type which can be subclassed, the latter is a variation that allows
you to modify the string in place.



Note that **MutableString** is not very efficient. Most operations are
implemented using slicing and string concatenation. If performance is
important, use lists of string fragments, or the **`array
<array.htm>`__** module.

**Example: Using the UserString module**

.. sourcecode:: python

    
    # File: `userstring-example-1.py <userstring-example-1.py>`__
    
    import UserString
    
    class MyString(UserString.MutableString):
    
        def append(self, s):
            self.data = self.data + s
    
        def insert(self, index, s):
            self.data = self.data[index:] + s + self.data[index:]
    
        def remove(self, s):
            self.data = self.data.replace(s, "")
    
    file = open("samples/book.txt")
    text = file.read()
    file.close()
    
    book = MyString(text)
    
    for bird in ["gannet", "robin", "nuthatch"]:
        book.remove(bird)
    
    print book
    


.. sourcecode:: python

    
    ...
    C: The one without the !
    P: The one without the -!!! They've ALL got the !! It's a
    Standard British Bird, the , it's in all the books!!!
    ...



