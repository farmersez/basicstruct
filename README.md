[![Build Status](https://travis-ci.org/Nurdok/basicstruct.svg?branch=master)](https://travis-ci.org/Nurdok/basicstruct)
[![Coverage Status](https://coveralls.io/repos/Nurdok/basicstruct/badge.svg?branch=master&service=github)](https://coveralls.io/github/Nurdok/basicstruct?branch=master)

# basicstruct

A simple struct-like object for Python.  
Compatible with Python 2.6+, 3.x, pypy and pypy3.

## Installation

    pip install basicstruct
    
## Usage

 To create your own struct, inherit from `BasicStruct` and define the field with the `__slots__` class member.
 `BasicStruct` are efficient objects that are automatically comparable, hashable, picklable, printable and reprable.

    from basicstruct import BasicStruct
    
    class Point(BasicStruct):
        __slots__ = ('x', 'y')
        
    p1 = Point(2, 3)
    p2 = Point(1, y=6)
    p3 = Point(x=0, y=0)
    
    print(p1)  # prints: Point(x=2, y=3)
    
