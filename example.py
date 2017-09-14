#!/usr/bin/env python
"""example.py: This is an example of documenting a Python module.

This part is called a docstring.  It can be multiple lines, or
a single line ended with the triple quote.  Generally there should be
docstrings for all public modules, functions, classes, and methods.
Non-public methods should at least have a comment that describes what
the method does.  (See https://www.python.org/dev/peps/pep-0008/ for more information.)

When a doc string is used, this will be information will be available as the __doc__
attribute for this module.  

On the python command line, you could type
>>> import example
>>> help(example)
and it would print out this docstring.
"""
import sys
import os
import datetime

__author__ = "Bruce Montgomery and Bhallaji Venkatesankulathusundaram"
__copyright__ = "Copyright (C) 2017 by Bruce Montgomery and Bhallaji Venkatesankulathusundaram"
#
# Redistribution, modification or use of this software in source or binary
# forms is permitted as long as the files maintain this copyright. Users are
# permitted to modify this and use it to learn about the field of embedded
# software. Gaurav Gandhi, and the University of Colorado
# are not liable for any misuse of this material.
#

class Dog(object):
    """Dog: an example of a Python class from https://docs.python.org/3/tutorial/classes.html"""
    kind = 'canine'			# class variable for all dogs

    def __init__(self, name):
        """Returns a Dog object with a name and an empty list of tricks"""
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        """Adds a new trick to a Dog's list of tricks"""
        self.tricks.append(trick)

def walker(name):
    """walker: an example of a python function"""
    dog1 = Dog(name)
    dog1.add_trick("Catch the Ball")
    print("Walking a new dog:")
    print("  The kind of this thing is ",dog1.kind)
    print("  This dog is ",dog1.name)
    print("  It knows these tricks - ",dog1.tricks)
			
# You can run this code from a command line - something like
# C:\Source> python example.py Fido
#    ...runs walker on the name Fido...
# or you can run it inside Python by importing example
# >>> import example
# >>> help(example)
#    ...shows all the docstrings...
# >>> example.walker("Fred")
#    ...runs walker on the name Fred...

if __name__ == "__main__":
    walker((sys.argv[1]))