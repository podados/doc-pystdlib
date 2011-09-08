






The formatter module
=====================




This module provides formatter classes that can be used together with
the **`htmllib <htmllib.htm>`__** module.



This module provides two class families, formatters and writers . The
former convert a stream of tags and data strings from the HTML parser
into an event stream suitable for an output device, and the latter
renders that event stream on an output device.



In most cases, you can use the **AbstractFormatter** class to do the
formatting. It calls methods on the writer object, representing
different kinds of formatting events. The **AbstractWriter** class
simply prints a message for each method call.

**Example: Using the formatter module to convert HTML to an event
stream**

.. sourcecode:: python

    
    # File: `formatter-example-1.py <formatter-example-1.py>`__
    
    import formatter
    import htmllib
    
    w = formatter.AbstractWriter()
    f = formatter.AbstractFormatter(w)
    
    file = open("samples/sample.htm")
    
    p = htmllib.HTMLParser(f)
    p.feed(file.read())
    p.close()
    
    file.close()
    


.. sourcecode:: python

    
    $ python formatter-example-1.py
    send_paragraph(1)
    new_font(('h1', 0, 1, 0))
    send_flowing_data('A Chapter.')
    send_line_break()
    send_paragraph(1)
    new_font(None)
    send_flowing_data('Some text. Some more text. Some')
    send_flowing_data(' ')
    new_font((None, 1, None, None))
    send_flowing_data('emphasised')
    new_font(None)
    send_flowing_data(' text. A')
    send_flowing_data(' link')
    send_flowing_data('[1]')
    send_flowing_data('.')




In addition to the **AbstractWriter** class, the **formatter** module
provides an **NullWriter** class, which ignores all events passed to
it, and a **DumbWriter** class that converts the event stream to a
plain text document:

**Example: Using the formatter module convert HTML to plain text**

.. sourcecode:: python

    
    # File: `formatter-example-2.py <formatter-example-2.py>`__
    
    import formatter
    import htmllib
    
    w = formatter.DumbWriter() # plain text
    f = formatter.AbstractFormatter(w)
    
    file = open("samples/sample.htm")
    
    # print html body as plain text
    p = htmllib.HTMLParser(f)
    p.feed(file.read())
    p.close()
    
    file.close()
    
    # print links
    print
    print
    i = 1
    for link in p.anchorlist:
        print i, "=>", link
        i = i + 1
    


.. sourcecode:: python

    
    $ python formatter-example-2.py
    
    A Chapter.
    
    Some text. Some more text. Some emphasised text. A link[1].
    
    1 => http://www.python.org




The following example provides a custom **Writer**, which in this case
is subclassed from the **DumbWriter** class. This version keeps track
of the current font style, and tweaks the output somewhat depending on
the font.


**Example: Using the formatter module with a custom writer**

.. sourcecode:: python

    
    # File: `formatter-example-3.py <formatter-example-3.py>`__
    
    import formatter
    import htmllib, string
    
    class Writer(formatter.DumbWriter):
    
        def __init__(self):
            formatter.DumbWriter.__init__(self)
            self.tag = ""
            self.bold = self.italic = 0
            self.fonts = []
    
        def new_font(self, font):
            if font is None:
                font = self.fonts.pop()
                self.tag, self.bold, self.italic = font
            else:
                self.fonts.append((self.tag, self.bold, self.italic))
                tag, bold, italic, typewriter = font
                if tag is not None:
                    self.tag = tag
                if bold is not None:
                    self.bold = bold
                if italic is not None:
                    self.italic = italic
    
        def send_flowing_data(self, data):
            if not data:
                return
            atbreak = self.atbreak or data[0] in string.whitespace
            for word in string.split(data):
                if atbreak:
                    self.file.write(" ")
                if self.tag in ("h1", "h2", "h3"):
                    word = string.upper(word)
                if self.bold:
                    word = "*" + word + "*"
                if self.italic:
                    word = "_" + word + "_"
                self.file.write(word)
                atbreak = 1
            self.atbreak = data[-1] in string.whitespace
    
    w = Writer()
    f = formatter.AbstractFormatter(w)
    
    file = open("samples/sample.htm")
    
    # print html body as plain text
    p = htmllib.HTMLParser(f)
    p.feed(file.read())
    p.close()
    


.. sourcecode:: python

    
    $ python formatter-example-3.py
    
    _A_ _CHAPTER._
    
    Some text. Some more text. Some *emphasised* text. A link[1].


