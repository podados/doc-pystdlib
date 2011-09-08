






Preface
=======




“We’d like to pretend that “Fredrik” is a role, but even
hundreds of volunteers couldn’t possibly keep up. No, “Fredrik”
is the result of crossing an http server with a spam filter with an
emacs whatsit and some other stuff besides”

Gordon McMillan, June 1998


The Python 2.0 distribution comes with an extensive standard library,
comprising over 200 modules. This book provides a brief description of
each module, plus one or more sample scripts showing how to use it.
All in all, this book contains some 350 sample scripts.



About this Book
---------------



“Those people who have nothing better to do than post on the
Internet all day long are rarely the ones who have the most
insights”

Jacob Nielsen, December 1998


Since I first stumbled upon Python some five years ago, I’ve spent
hundreds of hours answering questions on the **comp.lang.python**
newsgroup. Maybe someone found a module that might be exactly what
they want, but they couldn’t really figure out how to use it. Maybe
someone had picked the wrong module for the task. Or maybe someone
tried to reinvent the wheel. Often, a short sample script could be
much more helpful than a pointer to the reference documentation.



And if you post a couple of scripts each week, for a number of years,
you’ll end up with a rather large collection of potentially useful
scripts. What you’ll find in this book are the best parts from over
3,000 newsgroup messages. You’ll also find hundreds of new scripts
added to make sure every little nook and cranny of standard library
has been fully covered.



I’ve worked hard to make the scripts easy to understand and
adaptable. I’ve intentionally kept the annotations as short as
possible. If you want more background, there’s plenty of reference
material shipped with most Python distributions. In this book, the
emphasis is on the code.



Comments, suggestions, and bug reports are welcome. Send them to
fredrik@pythonware.com . I read all mail as soon as it arrives, but it
might take a while until I get around to answer.



For updates, addenda, and other information related to this book,
point your favorite web browser to
http://www.pythonware.com/people/fredrik/librarybook.htm .



What about Tkinter?
~~~~~~~~~~~~~~~~~~~


This book covers the entire standard library, except the (optional)
Tkinter user interface library. There are several reasons for this,
mostly related to time, space, and the fact that I’m working on
several other Tkinter documentation projects.



For current status on these projects, see
http://www.pythonware.com/people/fredrik/tkinterbook.htm .



Production details
~~~~~~~~~~~~~~~~~~


This book was written in DocBook SGML. I used a variety of tools,
including Secret Labs’ PythonWorks, and Excosoft Documentor, James
Clark’s Jade DSSSL processor, and Norm Walsh’s DocBook
stylesheets. And a bunch of Python scripts, of course.



Thanks to my referees: Tim Peters, Guido van Rossum, David Ascher,
Mark Lutz, and Rael Dornfest, and the PythonWare crew: Matthew Ellis,
Håkan Karlsson, and Rune Uhlin.



About the Examples
------------------


Unless otherwise noted, all examples run under Python 1.5.2 and Python
2.0. I’ve tried not to depend on internal details, and I expect most
scripts to work with upcoming 2.X versions as well.



The examples have been tested on Windows, Solaris, and Linux. Except
for a few scripts that depend on platform specific modules, the
examples should work right out of the box on most other platforms as
well.



(If you find something that doesn’t work as expected, let me know!)



All code is `copyrighted </zone/copyright.htm>`__, but you are of
course free to use one or more modules in your own programs. Just
don’t forget where you got them.



Most script files are named after the module they’re using, followed
by the string “ **-example-**” and a unique “serial number” .
Note that the scripts sometimes appear out of order; it’s done this
way on purpose, to match the filenames used in an earlier version of
this book, (the eff-bot guide to) The Standard Python Library .


