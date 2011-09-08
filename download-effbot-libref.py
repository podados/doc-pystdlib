

from urllib2 import urlopen
import re
import sys
import os
import codecs
from rattlebag.html2rest import html2rest, readsoup

MAIN_PREAMBLE = '''
===========================
The Python Standard Library
===========================

:author: Fredrik Lundh
:copyright: Copyright (c) 1999-2005 by Fredrik Lundh
:www: http://effbot.org/librarybook/

Based in part on 3,000 newsgroup articles written by Python veteran Fredrik
Lundh over the last four and half years, this book provides sample scripts for
all standard modules in the Python library.

This book provides extensive coverage of:

        * networking
        * file formats
        * data conversions
        * data storage
        * threads and processes 

and much, much more.

The book is also available in German.

'''

TOC_HEADER = '''

.. toctree::

'''

URLROOT = 'http://effbot.org/librarybook/'
INDEX_PATTERN = re.compile(r'<a\s+href="([-a-z]+-index).htm">')
PAGE_PATTERN = re.compile(r'<a\s+href="([-a-z]+).htm">')
IGNORESECTIONS = ['tools-and-utilities-index']
FORCEDOWNLOAD = '-f' in sys.argv[1:]

def write_index(titles):
    print 'writing index.rst...',
    fd = open('index.rst', 'wb')
    fd.write(MAIN_PREAMBLE)
    fd.write(TOC_HEADER)
    for title in titles:
        fd.write('    ' + title)
        fd.write('\n')
    fd.write('\n')
    fd.close()
    print 'done.'

def get_html(title):
    url = '%s%s.htm' % (URLROOT, title)
    print 'downloading %s...' % url,
    html = readsoup(urlopen(url))
    print 'done.'
    return html

def write_page(title, html):
    outfile = title + '.rst'
    fdout = open(outfile, 'wb')
    try:
        print 'writing %s...' % outfile,
        html2rest(html, fdout)
    finally:
        fdout.close()
    print 'done.'

def update_section_index(section, pages):
    if not pages:
        return
    infile = section + '.rst'
    outfile = infile + '.tmp'
    fdin = open(infile)
    fdout = open(outfile, 'wb')
    try:
        for line in fdin:
            if section == 'implementation-support-modules-index' and \
                    line.strip().lower().startswith('contents'):
                fdout.write(TOC_HEADER)
                for page in pages:
                    fdout.write('    %s\n' % page)
                fdout.write('\n')
                break
            if line.strip().lower().startswith('overview'):
                # write toc
                fdout.write(TOC_HEADER)
                for page in pages:
                    fdout.write('    %s\n' % page)
                fdout.write('\n')
                fdin.next()
                fdin.next()
                continue
            fdout.write(line)
    finally:
        fdin.close()
        fdout.close()
    os.remove(infile)
    os.rename(outfile, infile)

def write_section(section):
    html = get_html(section)
    pages = []
    for pagename in PAGE_PATTERN.findall(html):
        if pagename.endswith('-index'):
            continue
        pages.append(pagename)
        if os.path.exists(pagename + '.rst') and not FORCEDOWNLOAD:
            continue
        print '    ' + pagename
        page = get_html(pagename)
        write_page(pagename, page)
    write_page(section, html)
    update_section_index(section, pages)

def main():
    index = urlopen(URLROOT).read()
    sections = []
    for section in INDEX_PATTERN.findall(index):
        if section in IGNORESECTIONS:
            continue
        print '++++++ %s ++++++' % section
        sections.append(section)
        write_section(section)
    #write_index(sections)
    print 'done.'

if __name__ == '__main__':
    sys.exit(main())

