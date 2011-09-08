






The __builtin__ module
=======================




This module contains built-in functions which are automatically
available in all Python modules. You usually don’t have to import
this module; Python does that for you when necessary.



Calling a function with arguments from a tuple or dictionary #
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Python allows you to build function argument lists on the fly. Just
put all the arguments in a tuple, and call the built-in **apply**
function:

**Example: Using the apply function**

.. sourcecode:: python

    
    # File: `builtin-apply-example-1.py <builtin-apply-example-1.py>`__
    
    def function(a, b):
        print a, b
    
    apply(function, ("whither", "canada?"))
    apply(function, (1, 2 + 3))
    


.. sourcecode:: python

    
    whither canada?
    1 5




To pass keyword arguments to a function, you can use a dictionary as
the third argument to **apply**:

**Example: Using the apply function to pass keyword arguments**

.. sourcecode:: python

    
    # File: `builtin-apply-example-2.py <builtin-apply-example-2.py>`__
    
    def function(a, b):
        print a, b
    
    apply(function, ("crunchy", "frog"))
    apply(function, ("crunchy",), {"b": "frog"})
    apply(function, (), {"a": "crunchy", "b": "frog"})
    


.. sourcecode:: python

    
    crunchy frog
    crunchy frog
    crunchy frog




One common use for **apply** is to pass constructor arguments from a
subclass on to the base class, especially if the constructor takes a
lot of arguments.


**Example: Using the apply function to call base class constructors**

.. sourcecode:: python

    
    # File: `builtin-apply-example-3.py <builtin-apply-example-3.py>`__
    
    class Rectangle:
        def __init__(self, color="white", width=10, height=10):
            print "create a", color, self, "sized", width, "x", height
    
    class RoundedRectangle(Rectangle):
        def __init__(self, **kw):
            apply(Rectangle.__init__, (self,), kw)
    
    rect = Rectangle(color="green", height=100, width=100)
    rect = RoundedRectangle(color="blue", height=20)
    


.. sourcecode:: python

    
    create a green  sized 100 x 100
    create a blue  sized 10 x 20





Python 2.0 provides an alternate syntax. Instead of **apply**, you can
use an ordinary function call, and use ***** to mark the tuple, and
****** to mark the dictionary.



The following two statements are equivalent:


.. sourcecode:: python

    
    result = function(*args, **kwargs)
    result = apply(function, args, kwargs)



Loading and reloading modules #
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


If you’ve written a Python program larger than just a few lines, you
know that the **import** statement is used to import external modules
(you can also use the **from-import** version). What you might not
know already is that **import** delegates the actual work to a built-
in function called **__import__**.



The trick is that you can actually call this function directly. This
can be handy if you have the module name in a string variable, like in
the following example, which imports all modules whose names end with
“ **-plugin**” :


**Example: Using the __import__ function to load named modules**

.. sourcecode:: python

    
    # File: `builtin-import-example-1.py <builtin-import-example-1.py>`__
    
    import glob, os
    
    modules = []
    
    for module_file in glob.glob("*-plugin.py"):
        try:
            module_name, ext = os.path.splitext(os.path.basename(module_file))
            module = __import__(module_name)
            modules.append(module)
        except ImportError:
            pass # ignore broken modules
    
    # say hello to all modules
    for module in modules:
        module.hello()
    


.. sourcecode:: python

    
    example-plugin says hello





Note that the plugin modules have hyphens in the name. This means that
you cannot import such a module using the ordinary **import** command,
since you cannot have hyphens in Python identifiers.



Here’s the plugin used in this example:

**Example: A sample plugin**

.. sourcecode:: python

    
    # File: `example-plugin.py <example-plugin.py>`__
    
    def hello():
        print "example-plugin says hello"




The following example shows how to get a function object, given that
you have the module and function name as strings:

**Example: Using the __import__ function to get a named function**

.. sourcecode:: python

    
    # File: `builtin-import-example-2.py <builtin-import-example-2.py>`__
    
    def getfunctionbyname(module_name, function_name):
        module = __import__(module_name)
        return getattr(module, function_name)
    
    print repr(getfunctionbyname("dumbdbm", "open"))
    


.. sourcecode:: python

    
    




You can also use this function to implement lazy loading of modules.
In the following example, the **`string <string.htm>`__** module is
imported when it is first used:

**Example: Using the __import__ function to implement lazy import**

.. sourcecode:: python

    
    # File: `builtin-import-example-3.py <builtin-import-example-3.py>`__
    
    class LazyImport:
        def __init__(self, module_name):
            self.module_name = module_name
            self.module = None
        def __getattr__(self, name):
            if self.module is None:
                self.module = __import__(self.module_name)
            return getattr(self.module, name)
    
    string = LazyImport("string")
    
    print string.lowercase
    


.. sourcecode:: python

    
    abcdefghijklmnopqrstuvwxyz




Python provides some basic support for reloading modules that you’ve
already imported. The following example loads the **hello.py** file
three times:

**Example: Using the reload function**

.. sourcecode:: python

    
    # File: `builtin-reload-example-1.py <builtin-reload-example-1.py>`__
    
    import hello
    reload(hello)
    reload(hello)
    


.. sourcecode:: python

    
    hello again, and welcome to the show
    hello again, and welcome to the show
    hello again, and welcome to the show




**reload** uses the module name associated with the module object, not
the variable name. This means that even if you’ve renamed the
module, **reload** will still be able to find the original module.



Note that when you reload a module, it is recompiled, and the new
module replaces the old one in the module dictionary. However, if you
have created instances of classes defined in that module, those
instances will still use the old implementation.



Likewise, if you’ve used **from-import** to create references to
module members in other modules, those references will not be updated.



Looking in namespaces #
~~~~~~~~~~~~~~~~~~~~~~~~


The **dir** function returns a list of all members of a given module,
class, instance, or other type. It’s probably most useful when
you’re working with an interactive Python interpreter, but can also
come in handy in other situations.

**Example: Using the dir function**

.. sourcecode:: python

    
    # File: `builtin-dir-example-1.py <builtin-dir-example-1.py>`__
    
    def dump(value):
        print value, "=>", dir(value)
    
    import sys
    
    dump(0)
    dump(1.0)
    dump(0.0j) # complex number
    dump([]) # list
    dump({}) # dictionary
    dump("string")
    dump(len) # function
    dump(sys) # module
    


.. sourcecode:: python

    
    0 => []
    1.0 => []
    0j => ['conjugate', 'imag', 'real']
    [] => ['append', 'count', 'extend', 'index', 'insert',
        'pop', 'remove', 'reverse', 'sort']
    {} => ['clear', 'copy', 'get', 'has_key', 'items',
        'keys', 'update', 'values']
    string => []
     => ['__doc__', '__name__', '__self__']
     => ['__doc__', '__name__',
        '__stderr__', '__stdin__', '__stdout__', 'argv',
        'builtin_module_names', 'copyright', 'dllhandle',
        'exc_info', 'exc_type', 'exec_prefix', 'executable',
    ...




In the following example, the **getmember** function returns all
class-level attributes and methods defined by a given class:

**Example: Using the dir function to find all members of a class**

.. sourcecode:: python

    
    # File: `builtin-dir-example-2.py <builtin-dir-example-2.py>`__
    
    class A:
        def a(self):
            pass
        def b(self):
            pass
    
    class B(A):
        def c(self):
            pass
        def d(self):
            pass
    
    def getmembers(klass, members=None):
        # get a list of all class members, ordered by class
        if members is None:
            members = []
        for k in klass.__bases__:
            getmembers(k, members)
        for m in dir(klass):
            if m not in members:
                members.append(m)
        return members
    
    print getmembers(A)
    print getmembers(B)
    print getmembers(IOError)
    


.. sourcecode:: python

    
    ['__doc__', '__module__', 'a', 'b']
    ['__doc__', '__module__', 'a', 'b', 'c', 'd']
    ['__doc__', '__getitem__', '__init__', '__module__', '__str__']




Note that the **getmembers** function returns an ordered list. The
earlier a name appears in the list, the higher up in the class
hierarchy it’s defined. If order doesn’t matter, you can use a
dictionary to collect the names instead of a list.



The **vars** function is similar, but it returns a dictionary
containing the current value for each member. If you use it without an
argument, it returns a dictionary containing what’s visible in the
current local namespace:


**Example: Using the vars function**

.. sourcecode:: python

    
    # File: `builtin-vars-example-1.py <builtin-vars-example-1.py>`__
    
    book = "library2"
    pages = 250
    scripts = 350
    
    print "the %(book)s book contains more than %(scripts)s scripts" % vars()
    


.. sourcecode:: python

    
    the library book contains more than 350 scripts





Checking an object’s type #
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Python is a dynamically typed language, which means that a given
variable can be bound to values of different types at different
occasions. In the following example, the same function is called with
an integer, a floating point value, and a string:


.. sourcecode:: python

    
    def function(value):
        print value
    
    function(1)
    function(1.0)
    function("one")



The **type** function allows you to check what type a variable has.
This function returns a type descriptor , which is a unique object for
each type provided by the Python interpreter.

**Example: Using the type function**

.. sourcecode:: python

    
    # File: `builtin-type-example-1.py <builtin-type-example-1.py>`__
    
    def dump(value):
        print type(value), value
    
    dump(1)
    dump(1.0)
    dump("one")
    


.. sourcecode:: python

    
     1
     1.0
     one




Each type has a single corresponding type object, which means that you
can use the **is** operator (object identity) to do type testing:

**Example: Using the type function to distinguish between file names
and file objects**

.. sourcecode:: python

    
    # File: `builtin-type-example-2.py <builtin-type-example-2.py>`__
    
    def load(file):
        if isinstance(file, type("")):
            file = open(file, "rb")
        return file.read()
    
    print len(load("samples/sample.jpg")), "bytes"
    print len(load(open("samples/sample.jpg", "rb"))), "bytes"
    


.. sourcecode:: python

    
    4672 bytes
    4672 bytes




The **callable** function checks if an object can be called (either
directly or via **apply**). It returns true for functions, methods,
lambda expressions, classes, and class instances which define the
**__call__** method.

**Example: Using the callable function**

.. sourcecode:: python

    
    # File: `builtin-callable-example-1.py <builtin-callable-example-1.py>`__
    
    def dump(function):
        if callable(function):
            print function, "is callable"
        else:
            print function, "is *not* callable"
    
    class A:
        def method(self, value):
            return value
    
    class B(A):
        def __call__(self, value):
            return value
    
    a = A()
    b = B()
    
    dump(0) # simple objects
    dump("string")
    dump(callable)
    dump(dump) # function
    
    dump(A) # classes
    dump(B)
    dump(B.method)
    
    dump(a) # instances
    dump(b)
    dump(b.method)
    


.. sourcecode:: python

    
    0 is *not* callable
    string is *not* callable
     is callable
     is callable
    A is callable
    B is callable
     is callable
     is *not* callable
     ** is callable
     is callable
    **




Note that the class objects ( **A** and **B**) are both callable; if
you call them, they create new objects. However, instances of class
**A** are not callable, since that class doesn’t have a **__call__**
method.



You’ll find functions to check if an object is of any of the built-
in number, sequence, or dictionary types in the **`operator
<operator.htm>`__** module. However, since it’s easy to create a
class that implements e.g. the basic sequence methods, it’s usually
a bad idea to use explicit type testing on such objects.



Things get even more complicated when it comes to classes and
instances. Python doesn’t treat classes as types per se. Instead,
all classes belong to a special class type, and all class instances
belong to a special instance type.



This means that you cannot use **type** to test if an instance belongs
to a given class; all instances have the same type! To solve this, you
can use the **isinstance** function, which checks if an object is an
instance of a given class (or of a subclass to it).

**Example: Using the isinstance function**

.. sourcecode:: python

    
    # File: `builtin-isinstance-example-1.py <builtin-isinstance-example-1.py>`__
    
    class A:
        pass
    
    class B:
        pass
    
    class C(A):
        pass
    
    class D(A, B):
        pass
    
    def dump(object):
        print object, "=>",
        if isinstance(object, A):
            print "A",
        if isinstance(object, B):
            print "B",
        if isinstance(object, C):
            print "C",
        if isinstance(object, D):
            print "D",
        print
    
    a = A()
    b = B()
    c = C()
    d = D()
    
    dump(a)
    dump(b)
    dump(c)
    dump(d)
    dump(0)
    dump("string")
    


.. sourcecode:: python

    
     => A
     ** => B
     => A C
     => A B D
    0 =>
    string =>
    **




The **issubclass** is similar, but checks whether a class object is
the same as a given class, or is a subclass of it.



Note that while **isinstance** accepts any kind of object, the
**issubclass** function raises a **TypeError** exception if you use it
on something that is not a class object.

**Example: Using the issubclass function**

.. sourcecode:: python

    
    # File: `builtin-issubclass-example-1.py <builtin-issubclass-example-1.py>`__
    
    class A:
        pass
    
    class B:
        pass
    
    class C(A):
        pass
    
    class D(A, B):
        pass
    
    def dump(object):
        print object, "=>",
        if issubclass(object, A):
            print "A",
        if issubclass(object, B):
            print "B",
        if issubclass(object, C):
            print "C",
        if issubclass(object, D):
            print "D",
        print
    
    dump(A)
    dump(B)
    dump(C)
    dump(D)
    dump(0)
    dump("string")
    


.. sourcecode:: python

    
    A => A
    B => B
    C => A C
    D => A B D
    0 =>
    Traceback (innermost last):
      File "builtin-issubclass-example-1.py", line 29, in ?
      File "builtin-issubclass-example-1.py", line 15, in dump
    TypeError: arguments must be classes




Evaluating Python expressions #
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Python provides several ways to interact with the interpreter from
within a program. For example, the **eval** function evaluates a
string as if it were a Python expression. You can pass it a literal,
simple expressions, or even use built-in functions:

**Example: Using the eval function**

.. sourcecode:: python

    
    # File: `builtin-eval-example-1.py <builtin-eval-example-1.py>`__
    
    def dump(expression):
        result = eval(expression)
        print expression, "=>", result, type(result)
    
    dump("1")
    dump("1.0")
    dump("'string'")
    dump("1.0 + 2.0")
    dump("'*' * 10")
    dump("len('world')")
    


.. sourcecode:: python

    
    1 => 1 
    1.0 => 1.0 
    'string' => string 
    1.0 + 2.0 => 3.0 
    '*' * 10 => ********** 
    len('world') => 5 




A problem with **eval** is that if you cannot trust the source from
which you got the string, you may get into trouble. For example,
someone might use the built-in **__import__** function to load the`
**os** <os.htm>`__ module, and then remove files on your disk:

**Example: Using the eval function to execute arbitrary commands**

.. sourcecode:: python

    
    # File: `builtin-eval-example-2.py <builtin-eval-example-2.py>`__
    
    print eval("__import__('os').getcwd()")
    print eval("__import__('os').remove('file')")
    


.. sourcecode:: python

    
    /home/fredrik/librarybook
    Traceback (innermost last):
     File "builtin-eval-example-2", line 2, in ?
     File "", line 0, in ?
    os.error: (2, 'No such file or directory')




Note that you get an **os.error** exception, which means that Python
actually tried to remove the file!



Luckily, there’s a way around this problem. You can pass a second
argument to **eval**, which should contain a dictionary defining the
namespace in which the expression is evaluated. Let’s pass in an
empty namespace:


.. sourcecode:: python

    
    >>> print eval("__import__('os').remove('file')", {})
    Traceback (innermost last):
      File "", line 1, in ?
      File "", line 0, in ?
    os.error: (2, 'No such file or directory')



Hmm. We still end up with an **os.error** exception.



The reason for this is that Python looks in the dictionary before it
evaluates the code, and if it doesn’t find a variable named
**__builtins__** in there (note the plural form), it adds one:


.. sourcecode:: python

    
    >>> namespace = {}
    >>> print eval("__import__('os').remove('file')", namespace)
    Traceback (innermost last):
      File "", line 1, in ?
      File "", line 0, in ?
    os.error: (2, 'No such file or directory')
    >>> namespace.keys()
    ['__builtins__']



If you print the contents of the namespace variable, you’ll find
that it contains the full set of built-in functions.



The solution to this little dilemma isn’t far away: since Python
doesn’t add this item if it is already there, you just have to add a
dummy item called **__builtins__** to the namespace before calling
**eval**:


**Example: Safely using the eval function to evaluate arbitrary
strings**

.. sourcecode:: python

    
    # File: `builtin-eval-example-3.py <builtin-eval-example-3.py>`__
    
    print eval("__import__('os').getcwd()", {})
    print eval("__import__('os').remove('file')", {"__builtins__": {}})
    


.. sourcecode:: python

    
    /home/fredrik/librarybook
    Traceback (innermost last):
      File "builtin-eval-example-3.py", line 2, in ?
      File "", line 0, in ?
    NameError: __import__





Note that this doesn’t protect you from CPU or memory resource
attacks (for example, something like
**eval(“’*’*1000000*2*2*2*2*2*2*2*2*2”)** will most likely
cause your program to run out of memory after a while). In other
words, **eval** may be useful for trusted sources, but you shouldn’t
use it on arbitrary data, and especially not if you get data from
potentially malevolent sources.



Compiling and executing code #
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


The **eval** function only works for simple expressions. To handle
larger blocks of code, use the **compile** and **exec** functions:

**Example: Using the compile function to check syntax**

.. sourcecode:: python

    
    # File: `builtin-compile-example-1.py <builtin-compile-example-1.py>`__
    
    NAME = "script.py"
    
    BODY = """
    prnt 'owl-stretching time'
    """
    
    try:
        compile(BODY, NAME, "exec")
    except SyntaxError, v:
        print "syntax error:", v, "in", NAME
    


.. sourcecode:: python

    
    syntax error: invalid syntax in script.py




When successful, the **compile** function returns a code object, which
you can execute with the **exec** statement:

**Example: Compiling and executing compiled code**

.. sourcecode:: python

    
    # File: `builtin-compile-example-2.py <builtin-compile-example-2.py>`__
    
    BODY = """
    print 'the ant, an introduction'
    """
    
    code = compile(BODY, "


.. sourcecode:: python

     ``




To generate code on the fly, you can use the class shown in the
following example. Use the **write** method to add statements, and
**indent** and **dedent** to add structure, and this class takes care
of the rest.


**Example: A simple code generator tool**

.. sourcecode:: python

    
    # File: `builtin-compile-example-3.py <builtin-compile-example-3.py>`__
    
    import sys, string
    
    class CodeGeneratorBackend:
        "Simple code generator for Python"
    
        def begin(self, tab="\t"):
            self.code = []
            self.tab = tab
            self.level = 0
    
        def end(self):
            self.code.append("") # make sure there's a newline at the end
            return compile(string.join(self.code, "\n"), " `", "exec")
    
        def write(self, string):
            self.code.append(self.tab * self.level + string)
    
        def indent(self):
            self.level += 1
            # in Python 1.5.2 and earlier, use this instead:
            # self.level = self.level + 1
    
        def dedent(self):
            if self.level == 0:
                raise SyntaxError, "internal error in code generator"
            self.level -= 1
            # in Python 1.5.2 and earlier, use this instead:
            # self.level = self.level - 1
    
    #
    # try it out!
    
    c = CodeGeneratorBackend()
    c.begin()
    c.write("for i in range(5):")
    c.indent()
    c.write("print 'code generation made easy!'")
    c.dedent()
    exec c.end()
    
    `


.. sourcecode:: python

    
    code generation made easy!
    code generation made easy!
    code generation made easy!
    code generation made easy!
    code generation made easy!





Python also provides a function called **execfile**. It’s simply a
shortcut for loading code from a file, compiling it, and executing it.
The following example shows how to use and emulate this function.


**Example: Using the execfile function**

.. sourcecode:: python

    
    # File: `builtin-execfile-example-1.py <builtin-execfile-example-1.py>`__
    
    execfile("hello.py")
    
    def EXECFILE(filename, locals=None, globals=None):
        exec compile(open(filename).read(), filename, "exec") in locals, globals
    
    EXECFILE("hello.py")
    


.. sourcecode:: python

    
    hello again, and welcome to the show
    hello again, and welcome to the show





The **hello.py** file used in this example has the following contents:

**Example: The hello.py script**

.. sourcecode:: python

    
    # File: `hello.py <hello.py>`__
    
    print "hello again, and welcome to the show"




Overloading functions from the __builtin__ module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Since Python looks among the built-in functions after it has checked
the local and module namespace, there may be situations when you need
to explicitly refer to the **__builtin__** module. For example, the
following script overloads the **open** function with a version that
opens an ordinary file and checks that it starts with a “magic”
string. To be able to use the original **open** function, it
explicitly refers to it using the module name.

**Example: Explicitly accessing functions in the __builtin__ module**

.. sourcecode:: python

    
    # File: `builtin-open-example-1.py <builtin-open-example-1.py>`__
    
    def open(filename, mode="rb"):
        import __builtin__
        file = __builtin__.open(filename, mode)
        if file.read(5) not in("GIF87", "GIF89"):
            raise IOError, "not a GIF file"
        file.seek(0)
        return file
    
    fp = open("samples/sample.gif")
    print len(fp.read()), "bytes"
    
    fp = open("samples/sample.jpg")
    print len(fp.read()), "bytes"
    


.. sourcecode:: python

    
    3565 bytes
    Traceback (innermost last):
      File "builtin-open-example-1.py", line 12, in ?
      File "builtin-open-example-1.py", line 5, in open
    IOError: not a GIF file



