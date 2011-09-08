






The MimeWriter module
======================




This module can be used to write “multipart” messages, as defined
by the MIME mail standard.

**Example: Using the MimeWriter module**

.. sourcecode:: python

    
    # File: `mimewriter-example-1.py <mimewriter-example-1.py>`__
    
    import MimeWriter
    
    # data encoders
    import quopri
    import base64
    import StringIO
    
    import sys
    
    TEXT = """
    here comes the image you asked for.  hope
    it's what you expected.
    
    """
    
    FILE = "samples/sample.jpg"
    
    file = sys.stdout
    
    #
    # create a mime multipart writer instance
    
    mime = MimeWriter.MimeWriter(file)
    mime.addheader("Mime-Version", "1.0")
    
    mime.startmultipartbody("mixed")
    
    # add a text message
    
    part = mime.nextpart()
    part.addheader("Content-Transfer-Encoding", "quoted-printable")
    part.startbody("text/plain")
    
    quopri.encode(StringIO.StringIO(TEXT), file, 0)
    
    # add an image
    
    part = mime.nextpart()
    part.addheader("Content-Transfer-Encoding", "base64")
    part.startbody("image/jpeg")
    
    base64.encode(open(FILE, "rb"), file)
    
    mime.lastpart()




The output looks something like:




.. sourcecode:: python

    
    Content-Type: multipart/mixed;
        boundary='host.1.-852461.936831373.130.24813'
    
    --host.1.-852461.936831373.130.24813
    Content-Type: text/plain
    Context-Transfer-Encoding: quoted-printable
    
    here comes the image you asked for.  hope
    it's what you expected.
    
    
    
    --host.1.-852461.936831373.130.24813
    Content-Type: image/jpeg
    Context-Transfer-Encoding: base64
    
    /9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0a
    HBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIy
    ...
    1e5vLrSYbJnEVpEgjCLx5mPU0qsVK0UaxjdNlS+1U6pfzTR8IzEhj2HrVG6m8m18xc8cIKSCAysl
    tCuFyC746j/Cq2pTia4WztfmKjGBXTCmo6IUptn/2Q==
    
    --host.1.-852461.936831373.130.24813--




Here’s a larger example, which uses a helper class that stores each
subpart in the most suitable way:


**Example: A helper class for the MimeWriter module**

.. sourcecode:: python

    
    # File: `mimewriter-example-2.py <mimewriter-example-2.py>`__
    
    import MimeWriter
    import string, StringIO, sys
    import re, quopri, base64
    
    # check if string contains non-ascii characters
    must_quote = re.compile("[\177-\377]").search
    
    
    #
    # encoders
    
    def encode_quoted_printable(infile, outfile):
        quopri.encode(infile, outfile, 0)
    
    class Writer:
    
        def __init__(self, file=None, blurb=None):
            if file is None:
                file = sys.stdout
            self.file = file
            self.mime = MimeWriter.MimeWriter(file)
            self.mime.addheader("Mime-Version", "1.0")
    
            file = self.mime.startmultipartbody("mixed")
            if blurb:
                file.write(blurb)
    
        def close(self):
            "End of message"
            self.mime.lastpart()
            self.mime = self.file = None
    
        def write(self, data, mimetype="text/plain"):
            "Write data from string or file to message"
    
            # data is either an opened file or a string
            if type(data) is type(""):
                file = StringIO.StringIO(data)
            else:
                file = data
                data = None
    
            part = self.mime.nextpart()
    
            typ, subtyp = string.split(mimetype, "/", 1)
    
            if typ == "text":
    
                # text data
                encoding = "quoted-printable"
                encoder = lambda i, o: quopri.encode(i, o, 0)
    
                if data and not must_quote(data):
                    # copy, don't encode
                    encoding = "7bit"
                    encoder = None
    
            else:
    
                # binary data (image, audio, application, ...)
                encoding = "base64"
                encoder = base64.encode
    
            #
            # write part headers
    
            if encoding:
                part.addheader("Content-Transfer-Encoding", encoding)
    
            part.startbody(mimetype)
    
            #
            # write part body
    
            if encoder:
                encoder(file, self.file)
            elif data:
                self.file.write(data)
            else:
                while 1:
                    data = infile.read(16384)
                    if not data:
                        break
                    outfile.write(data)
    
    #
    # try it out
    
    BLURB = "if you can read this, your mailer is not MIME-aware\n"
    
    mime = Writer(sys.stdout, BLURB)
    
    # add a text message
    mime.write("""\
    here comes the image you asked for.  hope
    it's what you expected.
    """, "text/plain")
    
    # add an image
    mime.write(open("samples/sample.jpg", "rb"), "image/jpeg")
    
    mime.close()


