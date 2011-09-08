






Network Protocols
==================






.. toctree::

    socket
    select
    asyncore
    asynchat
    urllib
    urlparse
    cookie
    robotparser
    ftplib
    gopherlib
    httplib
    poplib
    imaplib
    smtplib
    telnetlib
    nntplib
    socketserver
    basehttpserver
    simplehttpserver
    cgihttpserver
    cgi
    webbrowser


This chapter describes Python’s socket protocol support, and the
networking modules built on top of the socket module. This includes
client handlers for most popular Internet protocols, as well as
several frameworks that can be used to implement Internet servers.



For the low-level examples in this chapter I’ll use two protocols
for illustration; the Internet Time Protocol , and the Hypertext
Transfer Protocol .



Internet Time Protocol
~~~~~~~~~~~~~~~~~~~~~~


The Internet Time Protocol (RFC 868, Postel and Harrenstien 1983) is a
simple protocol which allows a network client to get the current time
from a server.



Since this protocol is relatively light weight, many (but far from
all) Unix systems provide this service. It’s also about as easy to
implement as a network protocol can possibly be. The server simply
waits for a connection request, and immediately returns the current
time as a 4-byte integer, containing the number of seconds since
January 1st, 1900.



In fact, the protocol is so simple that I can include the entire
specification:




“Increasingly, people seem to misinterpret complexity as
sophistication, which is baffling — the incomprehensible should
cause suspicion rather than admiration. Possibly this trend results
from a mistaken belief that using a somewhat mysterious device confers
an aura of power on the user” — Niklaus Wirth




.. sourcecode:: python

    
    # File: rfc868.txt
    
    Network Working Group                                    J. Postel - ISI
    Request for Comments: 868                           K. Harrenstien - SRI
                                                                    May 1983
    
                                 Time Protocol
    
    This RFC specifies a standard for the ARPA Internet community.  Hosts on
    the ARPA Internet that choose to implement a Time Protocol are expected
    to adopt and implement this standard.
    
    This protocol provides a site-independent, machine readable date and
    time.  The Time service sends back to the originating source the time in
    seconds since midnight on January first 1900.
    
    One motivation arises from the fact that not all systems have a
    date/time clock, and all are subject to occasional human or machine
    error.  The use of time-servers makes it possible to quickly confirm or
    correct a system's idea of the time, by making a brief poll of several
    independent sites on the network.
    
    This protocol may be used either above the Transmission Control Protocol
    (TCP) or above the User Datagram Protocol (UDP).
    
    When used via TCP the time service works as follows:
    
       S: Listen on port 37 (45 octal).
    
       U: Connect to port 37.
    
       S: Send the time as a 32 bit binary number.
    
       U: Receive the time.
    
       U: Close the connection.
    
       S: Close the connection.
    
       The server listens for a connection on port 37.  When the connection
       is established, the server returns a 32-bit time value and closes the
       connection.  If the server is unable to determine the time at its
       site, it should either refuse the connection or close it without
       sending anything.
    
    When used via UDP the time service works as follows:
    
       S: Listen on port 37 (45 octal).
    
       U: Send an empty datagram to port 37.
    
       S: Receive the empty datagram.
    
       S: Send a datagram containing the time as a 32 bit binary number.
    
       U: Receive the time datagram.
    
       The server listens for a datagram on port 37.  When a datagram
       arrives, the server returns a datagram containing the 32-bit time
       value.  If the server is unable to determine the time at its site, it
       should discard the arriving datagram and make no reply.
    
    The Time
    
    The time is the number of seconds since 00:00 (midnight) 1 January 1900
    GMT, such that the time 1 is 12:00:01 am on 1 January 1900 GMT; this
    base will serve until the year 2036.
    
    For example:
    
       the time  2,208,988,800 corresponds to 00:00  1 Jan 1970 GMT,
    
                 2,398,291,200 corresponds to 00:00  1 Jan 1976 GMT,
    
                 2,524,521,600 corresponds to 00:00  1 Jan 1980 GMT,
    
                 2,629,584,000 corresponds to 00:00  1 May 1983 GMT,
    
            and -1,297,728,000 corresponds to 00:00 17 Nov 1858 GMT.




Hypertext Transfer Protocol
~~~~~~~~~~~~~~~~~~~~~~~~~~~


The Hypertext Transfer Protocol (HTTP, Fielding et al., RFC 2616) is
something completely different. The most recent specification (version
1.1), is over 100 pages.



However, in its simplest form, this protocol is very straightforward.
To fetch a document, the client connects to the server, and sends a
request like:


.. sourcecode:: python

    
    GET /hello.txt HTTP/1.0
    Host: hostname
    User-Agent: name
    
    [optional request body]



In return, the server returns a response like this:


.. sourcecode:: python

    
    HTTP/1.0 200 OK
    Content-Type: text/plain
    Content-Length: 7
    
    Hello



Both the request and response headers usually contains more fields,
but the **Host** field in the request header is the only one that must
always be present.



The header lines are separated by “ **\r\n**“, and the header must
be followed by an empty line, even if there is no body (this applies
to both the request and the response).



The rest of the HTTP specification deals with stuff like content
negotiation, cache mechanics, persistent connections, and much more.
For the full story, see ` Hypertext Transfer Protocol — HTTP/1.1
<http://www.w3.org/Protocols>`__.



Contents
~~~~~~~~


`The socket module <socket.htm>`__



`The select module <select.htm>`__



`The asyncore module <asyncore.htm>`__



`The asynchat module <asynchat.htm>`__



`The urllib module <urllib.htm>`__



`The urlparse module <urlparse.htm>`__



`The Cookie module <cookie.htm>`__



`The robotparser module <robotparser.htm>`__



`The ftplib module <ftplib.htm>`__



`The gopherlib module <gopherlib.htm>`__



`The httplib module <httplib.htm>`__



`The poplib module <poplib.htm>`__



`The imaplib module <imaplib.htm>`__



`The smtplib module <smtplib.htm>`__



`The telnetlib module <telnetlib.htm>`__



`The nntplib module <nntplib.htm>`__



`The SocketServer module <socketserver.htm>`__



`The BaseHTTPServer module <basehttpserver.htm>`__



`The SimpleHTTPServer module <simplehttpserver.htm>`__



`The CGIHTTPServer module <cgihttpserver.htm>`__



`The cgi module <cgi.htm>`__



`The webbrowser module <webbrowser.htm>`__


