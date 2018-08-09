The Python numeric tower in UML
===============================

:Date: 2018-08-09 20:10
:Category: Python
:Tags: Python, object-oriented programming
:Status: draft

.. PELICAN_BEGIN_SUMMARY

The `numbers <https://docs.python.org/3.7/library/numbers.html>`_ module
contains abstract base classes describing what interface defines a
`Real` or an `Integral` according to `PEP 3141
<https://www.python.org/dev/peps/pep-3141/>`_.  But I do not know of any
attempts at a graphical representation of PEP 3141.

.. PELICAN_END_SUMMARY

Being a visual person, I find that UML helps me think.  So here is the
numerical tower:

.. uml::

   note as N
   r-operations
   indicated with *
   end note


   class object
   class Number
   abstract class Complex {
   {abstract} __complex__()
   __bool__()
   {abstract} real
   {abstract} imag
   {abstract} __add__() *
   {abstract} __neg__()
   __pos__()
   __sub__()
   __rsub__()
   {abstract} __mul__() *
   {abstract} __div__() *
   {abstract} __pow__() *
   {abstract} __abs__()
   {abstract} conjugate()
   {abstract} __eq__()
   }

   abstract class Real {
      {abstract} __float__()
      {abstract} __trunc__()
      {abstract} __floor__()
      {abstract} __ceil__()
      {abstract} __round__()
      __divmod__() *
      {abstract} __floordiv__() *
      {abstract} __mod__() *
      {abstract} __lt__()
      {abstract} __le__()
      __complex__()
      real
      imag
      conjugate()
   }

   abstract class Rational {
      {abstract} numerator
      {abstract} denominator
      __float__()
   }

   abstract class Integral {
      {abstract} __int__()
      __index__()
      __lshift__() *
      __rshift__() *
      __and__() *
      __xor__() *
      __or__() *
      __invert__()
      __float__()
      numerator
      denominator
   }

   object <|-- Number
   Number <|- Complex
   Complex <|- Real
   Real <|- Rational
   Exact <|-- Rational
   Rational <|- Integral

That's it!
