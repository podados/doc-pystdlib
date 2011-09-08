






The parser module
==================




(Optional). The parser module provides an interface to Python’s
built-in parser and compiler.



The following example compiles a simple expression into an abstract
syntax tree (AST), turns the AST into a nested list, dumps the
contents of the tree (where each node contains either a grammar symbol
or a token), increments all numbers by one, and finally turns the list
back into a code object. At least that’s what I think it does.

**Example: Using the parser module**

.. sourcecode:: python

    
    # File: `parser-example-1.py <parser-example-1.py>`__
    
    import parser
    import symbol, token
    
    def dump_and_modify(node):
        name = symbol.sym_name.get(node[0])
        if name is None:
            name = token.tok_name.get(node[0])
        print name,
        for i in range(1, len(node)):
            item = node[i]
            if type(item) is type([]):
                dump_and_modify(item)
            else:
                print repr(item)
                if name == "NUMBER":
                    # increment all numbers!
                    node[i] = repr(int(item)+1)
    
    ast = parser.expr("1 + 3")
    
    list = ast.tolist()
    
    dump_and_modify(list)
    
    ast = parser.sequence2ast(list)
    
    print eval(parser.compileast(ast))
    


.. sourcecode:: python

    
    $ python parser-example-1.py
    eval_input testlist test and_test not_test comparison
    expr xor_expr and_expr shift_expr arith_expr term factor
    power atom NUMBER '1'
    PLUS '+'
    term factor power atom NUMBER '3'
    NEWLINE ''
    ENDMARKER ''
    6



