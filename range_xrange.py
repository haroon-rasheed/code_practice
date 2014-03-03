#!/usr/bin/env python
"""
One difference is that from versions of Python 3.0 and later,  xrange
doesn't exist, and range takes over the behavior of what was formerly
xrange.

So presumably you're asking about Python 2.x


In Python 2.x, range() generates a list, possibly a very large one. 
Sometimes that's exactly what you need.  But other times, you're just
using the list as an iterable, perhaps as a counter, or simply as a way
to make a loop go a fixed number of times.

xrange(), usually more efficient for speed, and certainly for space,
generates an iterable.  So it's interchangeable in a for loop, for example.

In general, if you're going to discard the list immediately after using
it, you should be using the iterable form, not the list form.


In Python 3.x, if you really need a list, you can trivially convert an
iterable into a list with the list "function."
"""

for item in xrange(5):
  print "Range ==>", item()

for item in range(5):
  print "XRange ==>", item
