






The exceptions module
======================




This module provides the standard exception hierarchy. It’s
automatically imported when Python starts, and the exceptions are
added to the **`__builtin__ <builtin.htm>`__** module. In other words,
you usually don’t need to import this module.



This is a Python module in 1.5.2, and a built-in module in 2.0 and
later.



The following standard exceptions are defined by this module:



+ **Exception** is used as a base class for all exceptions. It’s
  strongly recommended (but not yet required) that user exceptions are
  derived from this class too.

+ **SystemExit(Exception)** is raised by the **sys.exit** function. If
  it propagates to the top level without being caught by a **try-
  except** clause, the interpreter is terminated without a traceback
  message.

+ **StandardError(Exception)** is used as a base class for all standard
  exceptions (except **SystemExit**, that is).

+ **KeyboardInterrupt(StandardError)** is raised when the user presses
  Control-C (or any other interrupt key). Note that this may cause
  strange errors if you use “catch all” **try-except** statements.

+ **ImportError(StandardError)** is raised when Python fails to import a
  module.

+ **EnvironmentError** is used as a base class for exceptions that can
  be caused by the interpreter’s environment (that is, they’re
  usually not caused by bugs in the program).

+ **IOError(EnvironmentError)** is used to flag I/O-related errors.

+ **OSError(EnvironmentError)** is used to flag errors by the **os**
  module.

+ **WindowsError(OSError)** is used to flag Windows-specific errors from
  the **os** module.

+ **NameError(StandardError)** is raised when Python fails to find a
  global or local name.

+ **UnboundLocalError(NameError)** is raised if your program attempts to
  access a local variable before it has been assigned a value. This
  exception is only used in 2.0 and later; earlier versions raise a
  plain **NameError** exception instead.

+ **AttributeError(StandardError)** is raised when Python fails to find
  (or assign to) an instance attribute, a method, a module function, or
  any other qualified name.

+ **SyntaxError(StandardError)** is raised when the compiler stumbles
  upon a syntax error.

+ (2.0 and later) **IndentationError(SyntaxError)** is raised for syntax
  errors caused by bad indentation. This exception is only used in 2.0
  and later; earlier versions raise a plain **SyntaxError** exception
  instead.

+ (2.0 and later) **TabError(IndentationError)** is raised by the
  interpreter when the **-tt** option is used to check for inconsistent
  indentation. This exception is only used in 2.0 and later; earlier
  versions raise a plain **SyntaxError** exception instead.

+ **TypeError(StandardError)** is raised when an operation cannot be
  applied to an object of the given type.

+ **AssertionError(StandardError)** is raised when an **assert**
  statement fails (if the expression is false, that is).

+ **LookupError(StandardError)** is used as a base class for exceptions
  raised when a sequence or dictionary type doesn’t contain a given
  index or key.

+ **IndexError(LookupError)** is raised by sequence objects when the
  given index doesn’t exist.

+ **KeyError(LookupError)** is raised by dictionary objects when the
  given key doesn’t exist.

+ **ArithmeticError(StandardError)** is used as a base class for math-
  related exceptions.

+ **OverflowError(ArithmeticError)** is raised when an operations
  overflows (for example, when an integer is too large to fit in the
  given type).

+ **ZeroDivisionError(ArithmeticError)** is raised when you try to
  divide a number by zero.

+ **FloatingPointError(ArithmeticError)** is raised when a floating
  point operation fails.

+ **ValueError(StandardError)** is raised if an argument has the right
  type, but an invalid value.

+ (2.0 and later) **UnicodeError(ValueError)** is raised for type
  problems related to the Unicode string type. This is only used in 2.0
  and later.

+ **RuntimeError(StandardError)** is used for various run-time problems,
  including attempts to get outside the box when running in restricted
  mode, unexpected hardware problems, etc.

+ **NotImplementedError(RuntimeError)** can be used to flag functions
  that hasn’t been implemented yet, or methods that should be
  overridden.

+ **SystemError(StandardError)** is raised if the interpreter messes up,
  and knows about it. The exception value contains a more detailed
  description (usually something cryptic, like **“eval_code2: NULL
  globals”** or so). I cannot recall ever seeing this exception in
  over five years of full-time Python programming, but maybe that’s
  just me.

+ **MemoryError(StandardError)** is raised when the interpreter runs out
  of memory. Note that this only happens when the underlying memory
  allocation routines complain; you can often send your poor computer
  into a mindless swapping frenzy before that happens.




You can create your own exception classes. Just inherit from the
built-in **Exception** class (or a proper standard exception), and
override the constructor and/or **__str__** method as necessary.


**Example: Using the exceptions module**

.. sourcecode:: python

    
    # File: `exceptions-example-1.py <exceptions-example-1.py>`__
    
    # python imports this module by itself, so the following
    # line isn't really needed
    # import exceptions
    
    class HTTPError(Exception):
        # indicates an HTTP protocol error
        def __init__(self, url, errcode, errmsg):
            self.url = url
            self.errcode = errcode
            self.errmsg = errmsg
        def __str__(self):
            return (
                "" %
                (self.url, self.errcode, self.errmsg)
                )
    
    try:
        raise HTTPError("http://www.python.org/foo", 200, "Not Found")
    except HTTPError, error:
        print "url", "=>", error.url
        print "errcode", "=>", error.errcode
        print "errmsg", "=>", error.errmsg
        raise # reraise exception
    


.. sourcecode:: python

    
    $ python exceptions-example-1.py
    url => http://www.python.org/foo
    errcode => 200
    errmsg => Not Found
    Traceback (innermost last):
      File "exceptions-example-1", line 16, in ?
    HTTPError: 


