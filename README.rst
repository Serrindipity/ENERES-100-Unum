Unum - units in python
----------------------

Unum stands for 'unit-numbers'. It is a Python module that allows you to define and manipulate quantities with units attached such as 60 seconds, 500 watts, 42 miles-per-hour, 100 kg per square meter, 14400 bits per second, 30 dollars, and so on.


Changelog
---------
Unum 4.2.1

- source code file structure updated
- reademe updated
- project documentation added

Unum 4.1.3

- installation requires a modern version of setuptools (you may need to update your setuptools *before* installing).
- To support Python 2.5 and higher, the method Unum.as was renamed to Unum.asUnit; this was necessary since "as" became a reserved word. If you are still using old versions of Python, both names are available.
- In addition to unit names in uppercase, unit names in the correct case are now available. So, both "kg" and "KG" refer to the kilogram Unum, and both "eV" and "EV" refer to the electron volt Unum.
- Value types are no longer automatically coerced to floats. This allows the fractions.Fraction standard library type to be used, but may introduce incompatibilities with old code from integer vs. floating point division. In Python 3.x there is no problem.
- Prefixed versions of the 7 base SI units are supplied. So you can use "cm", "ns", "kA", "mK", "pmol", "Mcd", and "g" out of the box.

Prerequisites
----------------

Unum is pure python package. Python 2.2 or higher. Python 3.x should work as well, but please report any bugs

Installation
-------------

Unum is available through PyPI and can be easy installed using ``pip`` command ::

    pip install unum


Usage
-----

Once you have Unum installed you can start make calculations using units. For a simple example, let's can calculate Usain Bolt's average speed during his record-breaking performance in the 2008 Summer Olympics::

    >>> from unum.units import * # Load a number of common units.
    >>> distance = 100*m
    >>> time = 9.683*s
    >>> speed = distance / time
    >>> speed
    10.3273778788 [m/s]
    >>> speed.asUnit(mile/h)
    23.1017437978 [mile/h]

The full documentation of unum can be find at `project website <https://unum-test.readthedocs.io/>`_.

Tests
-----

To run tests : ::

    cd <install-directory>
    python setup.py test

Feedback
--------

Questions, feedback and issues can be repported at `Bitbucket Issues Tracker <https://bitbucket.org/lukaszlaba/unum/issues>`_.

License
-------

Copyright (C) 2000-2003 Pierre Denis

Copyright (C) 2009-2018 Chris MacLeod

Copyright (C) 2022 Lukasz Laba


Unum is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, o (at your option) any later version.

Unum is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Tebe; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

Other information
-----------------

Project website: https://unum.readthedocs.io

Code repository: https://bitbucket.org/lukaszlaba/unum

Contact: Lukasz Laba <lukaszlaba@gmail.pl>



