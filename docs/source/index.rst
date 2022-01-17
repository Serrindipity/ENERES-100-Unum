.. unum documentation master file, created by
   sphinx-quickstart on Thu Jan 13 22:13:36 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Unum - units in python
----------------------

.. image:: _static/unum_logo.png
   :alt: Pint: **physical quantities**
   :class: floatingflask   
   :width: 150

In case you make scientific or engineering calculation it is a best practice, always include units when you define variables if they are relevant. For example, if you define velocity to be 100, and time to be 0.5, Python cannot perform unit checking or unit balancing when you calculate the distance. It is a better practice to define the velocity as 100 km/h and the time as 30 min. It can also prevent errors later on. There are few 'Famous Unit Conversion Errors' that occurred because of unit calculation issue.

Since the pure Python has no feature that let you make unit calculation you neeed additional package for that. Unum can handle units for you, there's a large list of built-in units available for the most common applications that could be easily extended by the user. Unum automatically carries units forward throughout calculations, always checking to make sure that the units being used in formulas and equations are dimensionally compatible. It warns you if you try to perform math with quantities in incompatible units. For example, you get an error notification if you try to add quantities of length, temperature, time, and energy together.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   unum




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
