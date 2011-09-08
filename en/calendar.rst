






The calendar module
====================




This is a Python reimplementation of the Unix **cal** command. It
simply prints the calendar for any given month or year to standard
output.



**prmonth(year, month)** prints the calendar for a given month.

**Example: Using the calender module**

.. sourcecode:: python

    
    # File: `calendar-example-1.py <calendar-example-1.py>`__
    
    import calendar
    calendar.prmonth(1999, 12)
    


.. sourcecode:: python

    
        December 1999
    Mo Tu We Th Fr Sa Su
           1  2  3  4  5
     6  7  8  9 10 11 12
    13 14 15 16 17 18 19
    20 21 22 23 24 25 26
    27 28 29 30 31




**prcal(year)** prints the calendar for a given year.


**Example: Using the calender module**

.. sourcecode:: python

    
    # File: `calendar-example-2.py <calendar-example-2.py>`__
    
    import calendar
    calendar.prcal(2000)
    


.. sourcecode:: python

    
                                      2000
    
           January                  February                    March
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                    1  2          1  2  3  4  5  6             1  2  3  4  5
     3  4  5  6  7  8  9       7  8  9 10 11 12 13       6  7  8  9 10 11 12
    10 11 12 13 14 15 16      14 15 16 17 18 19 20      13 14 15 16 17 18 19
    17 18 19 20 21 22 23      21 22 23 24 25 26 27      20 21 22 23 24 25 26
    24 25 26 27 28 29 30      28 29                     27 28 29 30 31
    31
    
            April                      May                      June
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                    1  2       1  2  3  4  5  6  7                1  2  3  4
     3  4  5  6  7  8  9       8  9 10 11 12 13 14       5  6  7  8  9 10 11
    10 11 12 13 14 15 16      15 16 17 18 19 20 21      12 13 14 15 16 17 18
    17 18 19 20 21 22 23      22 23 24 25 26 27 28      19 20 21 22 23 24 25
    24 25 26 27 28 29 30      29 30 31                  26 27 28 29 30
    
            July                     August                   September
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                    1  2          1  2  3  4  5  6                   1  2  3
     3  4  5  6  7  8  9       7  8  9 10 11 12 13       4  5  6  7  8  9 10
    10 11 12 13 14 15 16      14 15 16 17 18 19 20      11 12 13 14 15 16 17
    17 18 19 20 21 22 23      21 22 23 24 25 26 27      18 19 20 21 22 23 24
    24 25 26 27 28 29 30      28 29 30 31               25 26 27 28 29 30
    31
    
           October                  November                  December
    Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                       1             1  2  3  4  5                   1  2  3
     2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10
     9 10 11 12 13 14 15      13 14 15 16 17 18 19      11 12 13 14 15 16 17
    16 17 18 19 20 21 22      20 21 22 23 24 25 26      18 19 20 21 22 23 24
    23 24 25 26 27 28 29      27 28 29 30               25 26 27 28 29 30 31
    30 31





Note that the calendars are printed using European conventions; in
other words, Monday is the first day of the week.



This module contains a number of support functions which can be useful
if you want to output calendars in other formats. It’s probably
easiest to copy the entire file, and tweak it to suit your needs.


