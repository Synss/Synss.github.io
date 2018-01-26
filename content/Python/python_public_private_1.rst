Read-only attributes in Python
==============================

:Date: 2018-01-30 21:30
:Slug: python-public-private-1
:Category: Python
:Tags: Python, object-oriented programming


Summary
-------

There is a case for having some immutable (read only) attributes in a
class.  But adding a ``value`` property to return a protected ``_value``
attribute is not satisfying.  Let us review a few ways to make read-only
attributes on classes and conclude with completely hiding an attribute
in a closure.

Introduction
------------

   Given the success of Haskell, one might argue that encapsulation is
   somewhat overrated.

   William R. Cook, *On Understanding Data Abstraction, Revisited*,
   OOPSLA 2009.

C++ or Java developers are taught to make every attribute private by
default and to set accessors to control the access.  C++ may further
enforce the constness of attributes.  Although Python has no such
mechanism, it is still possible to declare immutable attributes in a
class.

The bad way
-----------

The way I see it accomplished most often (I have done it in the past) is
to define a private variable ``_protected`` and a ``property`` for the
same variable::

    >>> class Point:
    ...     def __init__(self, x, y):
    ...         self._x = x
    ...         self._y = y
    ...
    ...     @property
    ...     def x(self):
    ...         return self._x
    ...
    ...     @property
    ...     def y(self):
    ...         return self._y
    ...
    ...     def __str__(self):
    ...         return "%s(%r, %r)" % (type(self).__name__, self.x, self.y)
    ...
    >>> p = Point(5, 7)
    >>> print(p)
    Point(5, 7)
    >>> p.x = 3
    Traceback (most recent call last):
       ...
    AttributeError: can't set attribute

and this is bad.  From the point of view of the user of ``Point``, ``x``
and ``y`` have two names: with ``_`` and without.  What is even more
confusing, the two names are not equal.  One can mutate the values and
the other not.  So which one should I use...  And what about derived
classes: is ``class Point3D(Point)`` allowed to mutate ``x`` and ``y``?

``x`` and ``y`` may look like strange protected variables but they are
most definitely mutable.

There must be a better way.

Use a namedtuple if the class only has immutable attributes
-----------------------------------------------------------

Should the class contain only read-only attributes, then the best
solution is simply to use a ``namedtuple`` (examples in the `official
doc
<https://docs.python.org/3.6/library/collections.html?highlight=namedtuple#collections.namedtuple>`_).
A ``namedtuple`` can be derived and extended, and methods like
``__str__()`` are defined with better defaults than a regular ``class``.

But ``namedtuple`` does not allow mutable attributes *at all*.


One step back: read-write attributes
------------------------------------

Let us first do one step back and look at read-write (mutable)
attributes on a class.  Then we can see how to instrument Python to drop
the "write" part to get immutability.

Setting an attribute on a class adds an entry to the ``__dict__`` the
class and binds the name of the attribute to its value::

    >>> class K:
    ...     pass
    ...
    >>> obj = K()
    >>> obj.__dict__["value"] = 42  # The same as obj.value = 42
    >>> obj.__dict__
    {'value': 42}
    >>> obj.__dict__["value"] is obj.value
    True
    >>> obj.value
    42
    >>> obj.__dict__["value"] = "meaning of life"
    >>> obj.value
    'meaning of life'

Properties are checked before ``__dict__`` during the attribute lookup
so that defining a getter property gets us where we want::

    >>> class Point:
    ...     def __init__(self, x, y):
    ...         self.__dict__["x"] = x
    ...         self.__dict__["y"] = y
    ...
    ...     @property
    ...     def x(self):
    ...         return self.__dict__["x"]
    ...
    ...     @property
    ...     def y(self):
    ...         return self.__dict__["y"]
    ...
    ...     def __str__(self):
    ...         return "%s(%r, %r)" % (type(self).__name__, self.x, self.y)
    ...
    >>> p = Point(5, 7)
    >>> print(p)
    Point(5, 7)
    >>> p.x
    5
    >>> p.x = 7
    Traceback (most recent call last):
       ...
    AttributeError: can't set attribute

This way does not waste a name such as ``_x`` and simply uses the
already existing Python machinery for attributes.  It disables the
*setter* by... defining a *getter*!

This is the way I would actually do it in production code but your C++
or Java affine colleague might argue that ``Point`` is not protected
from ill-intentioned users accessing ``__dict__`` directly.

This is true but `we are all consenting adults here
<https://mail.python.org/pipermail/tutor/2003-October/025932.html>`_.
Anyway.

Truly immutable attribute
-------------------------

I will start with a disclaimer: This is just a fun exercise.  Don't do
that in real code!

Even if Python does not typically enforce hiding information (or hiding
anything for that matter) it is still possible to use lexical scoping to
hide attributes.

Actually, the idea comes from Douglas Crockford's *JavaScript: The Good
Parts*.  JavaScript uses closures for encapsulation and this is also
perfectly applicable to Python.  A closure is a function that accesses
data defined in its enclosing scope.  This data may in turn be invisible
to the outermost scope.  So it can be used to hide things.

::

    >>> def encapsulate(value, *, readonly=False):
    ...     def getter(self):
    ...         return value
    ...     def setter(self, newvalue):
    ...         nonlocal value
    ...         value = newvalue
    ...     return property(getter, setter) if not readonly else property(getter)
    ...
    >>> class Point:
    ...     def __new__(cls, x, y, z, color):
    ...         cls.x = encapsulate(x, readonly=True)
    ...         cls.y = encapsulate(y, readonly=True)
    ...         cls.z = encapsulate(z, readonly=True)
    ...         cls.color = encapsulate(color)
    ...         return super().__new__(cls)
    ...
    ...     def __init__(self, x, y, z, color):
    ...         super().__init__()
    ...
    ...     def __str__(self):
    ...         return "%s(%s, %s, %s, color=%r)" % (
    ...                type(self).__name__, self.x, self.y, self.z,
    ...                self.color)
    ...
    >>> p = Point(5, 7, 13, "red")
    >>> print(p)
    Point(5, 7, 13, color='red')
    >>> p.x
    5
    >>> p.color = "green"
    >>> p.color
    'green'
    >>> print(p)
    Point(5, 7, 13, color='green')
    >>> p.z = 42
    Traceback (most recent call last):
       ...
    AttributeError: can't set attribute

Actually, there is another way to access the data from the closure::

    >>> p.__class__.x.fget.__closure__[0].cell_contents
    5

but it is not writable either.

Bonus: The other way around: read-write attribute on a namedtuple
-----------------------------------------------------------------

Disclaimer again: really, don't do that!

::

    >>> from collections import namedtuple
    >>> class Point(namedtuple("Point", "x y z")):
    ...     def __new__(cls, x, y, z, color):
    ...         cls.color = encapsulate(color)
    ...         return super().__new__(cls, x, y, z)
    ...
    ...     def __str__(self):
    ...         return "%s(x=%r, y=%r, z=%r, color=%r)" % (
    ...             type(self).__name__, self.x, self.y, self.z, self.color)
    ...
    >>> p = Point(128, 64, 32, "green")
    >>> print(p)
    Point(x=128, y=64, z=32, color='green')
    >>> p.x = 12
    Traceback (most recent call last):
       ...
    AttributeError: can't set attribute
    >>> p.color = "red"
    >>> print(p)
    Point(x=128, y=64, z=32, color='red')
