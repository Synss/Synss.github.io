Public, private, and contracts
==============================

:Date: 2018-03-19 00:00
:Category: OOP
:Tags: Python, object-oriented programming


Summary
-------

Here, I want to show that good design dictates that the arguments passed to a
class initializer (constructor) should be publicly accessible.  This simple
rule has an interesting corollary:  The default initializer should not take
anything more that what the class requires to function.

.. PELICAN_END_SUMMARY


Introduction
------------

There is not simple rule as to making a class attribute public or not.  Authors
advocate [XXX Scott Meyers?] for private by default because making a private
attribute public later does not break the API.

This is true but some attributes must nevertheless be public.

There is a very simple an pragmatic reason for this rule: An object passed to a
class initializer was instantiated in the caller.  That is, the caller may
already hold a reference to it.  There is therefore little reason to hide it.

But this simple rule can be rooted in [Bertrand Meyer]'s `design by contract`_.


Desing by contract
------------------

Function contracts
~~~~~~~~~~~~~~~~~~

Class contract
~~~~~~~~~~~~~~

By extension, the contract precondition of a class is the absolute minimum that
the class requires to honor its postcondition contract.  That is the essence of
the object.  As such, the user of an object from this class may want to know
the value of these attributes,

for example the port of a socket or the seed of a random number generator.


Args passed to ``__init__()`` public: part of the contract of the class;
every other private: not part of the contract of the class.

Contract => expected to exist, essence of the object.

If not, should not be passed to ``__init__()``

It is still OK to have default values to ``__init__()``


.. note:: Defining ``__repr__()`` in Python encourages this design principle.
   It is considered good practice to define ``__repr__()`` so that its result
   evaluates equally to the object::

     >>> eval(repr(obj)) == obj
     True

   This implies that the name of the class of `obj`
   (``obj.__class__.__name__``) and the arguments to ``__init__()`` entirely
   define `obj`.


Therefore/example: do not pass a filename where a file is needed.


Example: Message class


class Message:
   def __init__(self, length, payload):
       super().__init__()
       self.payload = payload

   @property
   def length(self):
      return len(self.payload)

   @classmethod
   def from_bytes(cls, stream):
      length = int.from_bytes(stream.read(4), byteorder="big")
      payload = stream.read(length)
      return cls(length, payload)

   def to_bytes(self):
      return b"".join((self.length.to_bytes(4, byteorder="big"), self.payload))

   __bytes__ = to_bytes


Conclusion
----------

This article gives a simple OOP design principle regarding both the arguments
that should be passed to the initializer or constructor of a class and which
attributes should be public or private.

# The default initializer or the constructor should take what the class must
  receive to be instantiated, and nothing more.  Anything else is syntactic
  sugar and may be offered as default arguments to ``__init__()``, alternative
  constructors, ``classmethod``...
# Any argument passed to the default initializer or constructor must be made
  publicly available on the class.  The public attribute may be immutable when
  required like the seed of a random number generator.


References
----------

.. _design by contract: https://en.wikipedia.org/wiki/Design_by_contract
