






The re module
==============




“Some people, when confronted with a problem, think “I know,
I’ll use regular expressions.” Now they have two problems” —
Jamie Zawinski, on comp.lang.emacs [*]




This module provides a set of powerful regular expression facilities.
A regular expression is a string pattern written in a compact (and
quite cryptic) syntax, and this module allows you to quickly check
whether a given string matches a given pattern (using the **match**
function), or contains such a pattern (using the **search** function).



The **match** function attempts to match a pattern against the
beginning of the given string. If the pattern matches anything at all
(including an empty string, if the pattern allows that!), **match**
returns a match object . The **group** method can be used to find out
what matched.

**Example: Using the re module to match strings**

.. sourcecode:: python

    
    # File: `re-example-1.py <re-example-1.py>`__
    
    import re
    
    text = "The Attila the Hun Show"
    
    # a single character
    m = re.match(".", text)
    if m: print repr("."), "=>", repr(m.group(0))
    
    # any string of characters
    m = re.match(".*", text)
    if m: print repr(".*"), "=>", repr(m.group(0))
    
    # a string of letters (at least one)
    m = re.match("\w+", text)
    if m: print repr("\w+"), "=>", repr(m.group(0))
    
    # a string of digits
    m = re.match("\d+", text)
    if m: print repr("\d+"), "=>", repr(m.group(0))
    


.. sourcecode:: python

    
    '.' => 'T'
    '.*' => 'The Attila the Hun Show'
    '\\w+' => 'The'




You can use parentheses to mark regions in the pattern. If the pattern
matched, the **group** method can be used to extract the contents of
these regions. **group(1)** returns the contents of the first group,
**group(2)** the contents of the second, etc. If you pass several
group numbers to the **group** function, it returns a tuple.

**Example: Using the re module to extract matching substrings**

.. sourcecode:: python

    
    # File: `re-example-2.py <re-example-2.py>`__
    
    import re
    
    text ="10/15/99"
    
    m = re.match("(\d{2})/(\d{2})/(\d{2,4})", text)
    if m:
        print m.group(1, 2, 3)
    


.. sourcecode:: python

    
    ('10', '15', '99')




The **search** function searches for the pattern inside the string. It
basically tries the pattern at every possible characters position,
starting from the left, and returns a match object as soon it has
found a match. If the pattern doesn’t match anywhere, it returns
**None**.

**Example: Using the re module to search for substrings**

.. sourcecode:: python

    
    # File: `re-example-3.py <re-example-3.py>`__
    
    import re
    
    text = "Example 3: There is 1 date 10/25/95 in here!"
    
    m = re.search("(\d{1,2})/(\d{1,2})/(\d{2,4})", text)
    
    print m.group(1), m.group(2), m.group(3)
    
    month, day, year = m.group(1, 2, 3)
    print month, day, year
    
    date = m.group(0)
    print date
    


.. sourcecode:: python

    
    10 25 95
    10 25 95
    10/25/95




The **sub** function can be used to replace patterns with another
string.

**Example: Using the re module to replace substrings**

.. sourcecode:: python

    
    # File: `re-example-4.py <re-example-4.py>`__
    
    import re
    
    text = "you're no fun anymore..."
    
    # literal replace (string.replace is faster)
    print re.sub("fun", "entertaining", text)
    
    # collapse all non-letter sequences to a single dash
    print re.sub("[^\w]+", "-", text)
    
    # convert all words to beeps
    print re.sub("\S+", "-BEEP-", text)
    


.. sourcecode:: python

    
    you're no entertaining anymore...
    you-re-no-fun-anymore-
    -BEEP- -BEEP- -BEEP- -BEEP-




You can also use **sub** to replace patterns via a callback function.
The following example also shows how to pre-compile patterns.

**Example: Using the re module to replace substrings via a callback**

.. sourcecode:: python

    
    # File: `re-example-5.py <re-example-5.py>`__
    
    import re
    import string
    
    text = "a line of text\\012another line of text\\012etc..."
    
    def octal(match):
        # replace octal code with corresponding ASCII character
        return chr(string.atoi(match.group(1), 8))
    
    octal_pattern = re.compile(r"\\(\d\d\d)")
    
    print text
    print octal_pattern.sub(octal, text)
    


.. sourcecode:: python

    
    a line of text\012another line of text\012etc...
    a line of text
    another line of text
    etc...




If you don’t compile, the **re** module caches compiled versions for
you, so you usually don’t have to compile regular expressions in
small scripts. In Python 1.5.2, the cache holds 20 patterns. In 2.0,
the cache size has been increased to 100 patterns.



Finally, here’s an example that shows you how to match a string
against a list of patterns. The list of patterns are combined into a
single pattern, and pre-compiled to save time.

**Example: Using the re module to match against one of many patterns**

.. sourcecode:: python

    
    # File: `re-example-6.py <re-example-6.py>`__
    
    import re, string
    
    def combined_pattern(patterns):
        p = re.compile(
            string.join(map(lambda x: "("+x+")", patterns), "|")
            )
        def fixup(v, m=p.match, r=range(0,len(patterns))):
            try:
                regs = m(v).regs
            except AttributeError:
                return None # no match, so m.regs will fail
            else:
                for i in r:
                    if regs[i+1] != (-1, -1):
                        return i
        return fixup
    
    #
    # try it out!
    
    patterns = [
        r"\d+",
        r"abc\d{2,4}",
        r"p\w+"
    ]
    
    p = combined_pattern(patterns)
    
    print p("129391")
    print p("abc800")
    print p("abc1600")
    print p("python")
    print p("perl")
    print p("tcl")
    


.. sourcecode:: python

    
    0
    1
    1
    2
    2
    None






**Note**: comp.lang.emacs doesn’t exist, really. I’m not sure how
that ended up in the book, but it’s interesting to see how the
erronous attribution has propagated through-out the net.


