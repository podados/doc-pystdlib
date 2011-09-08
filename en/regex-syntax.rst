






The regex_syntax module
========================




(Obsolete). This module contains a bunch of flags that can be used to
change the behavior of the **`regex <regex.htm>`__** regular
expression module.

**Example: Using the regex_syntax module**

.. sourcecode:: python

    
    # File: `regex-syntax-example-1.py <regex-syntax-example-1.py>`__
    
    import regex_syntax
    import regex
    
    def compile(pattern, syntax):
        syntax = regex.set_syntax(syntax)
        try:
            pattern = regex.compile(pattern)
        finally:
            # restore original syntax
            regex.set_syntax(syntax)
        return pattern
    
    def compile_awk(pattern):
        return compile(pattern, regex_syntax.RE_SYNTAX_AWK)
    
    def compile_grep(pattern):
        return compile(pattern, regex_syntax.RE_SYNTAX_GREP)
    
    def compile_emacs(pattern):
        return compile(pattern, regex_syntax.RE_SYNTAX_EMACS)



