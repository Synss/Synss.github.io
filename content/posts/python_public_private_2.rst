Which attributes to make public and which protected?


Args passed to ``__init__()`` public: part of the contract of the class;
every other private: not part of the contract of the class.

Passed to ``__init__()`` normally publicly visible in ``__str__()``
anyway.

Contract => expected to exist, essence of the object.

If not, should not be passed to ``__init__()``

It is still OK to have default values to ``__init__()``


Therefore/example: do not pass a filename where a file is needed.
