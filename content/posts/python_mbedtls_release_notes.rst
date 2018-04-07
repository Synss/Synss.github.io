============================
python-mbedtls release notes
============================

:Date: 2018-02-17 17:00
:Modified: 2018-04-07 10:30
:Category: Python
:Tags: Python, TLS, SSL, Cryptography
:Slug: python-mbedtls-release-notes

`python-mbedtls <https://github.com/Synss/python-mbedtls>`_ is a free
cryptographic library for Python 2.7, 3.4, 3.5, and 3.6 that uses `mbed TLS
<https://tls.mbed.org>`_ for back end.

`python-mbedtls` API follows the recommendations from `PEP 452
<https://www.python.org/dev/peps/pep-0452/>`_ and `PEP 272
<https://www.python.org/dev/peps/pep-0272/>`_ and can therefore be used as a
drop-in replacements to `PyCrypto  <https://www.dlitz.net/software/pycrypto/>`_
or Python's `hashlib <https://docs.python.org/3.6/library/hashlib.html>`_ and
`hmac <https://docs.python.org/3.6/library/hmac.html>`_.


Release notes
=============

Installation
------------

The library is available on `pypi
<https://pypi.python.org/pypi/python-mbedtls/0.8>`_ and is installed after mbed
TLS with

.. code-block:: console

   $ pip install python-mbedtls


Links
-----

- Source code: https://github.com/Synss/python-mbedtls
- Documentation: https://synss.github.io/python-mbedtls/

python-mbedtls 0.9.0 released
=============================

This is a bug fix release.

What's new
----------

This release fixes the source distribution.  Installing with pip
should now work!

API changes
-----------

- X.509 certificates now have a `next()` method returning the next certificate
  from a chain.
- `md` implements the `block_size` property.


python-mbedtls 0.8 released [withdrawn]
=======================================

`python-mbedtls` 0.8 features:

- `mbedtls.hash` and `mbedtls.hmac`: message digest algorithms with MD5,
  SHA-1, SHA-2, and RIPEMD-160.
- `mbedtls.cipher`: symmetric encryption with AES, ARC4, Blowfish, Camellia,
  and DES.
- `mbedtls.pk`: RSA cryptosystem with support for PEM and DER formats.
- `mbedtls.x509`: X.509 certificate writing and parsing.

What's new
----------

`python-mbedtls 0.8 <https://pypi.python.org/pypi/python-mbedtls/0.8>`_
features a new `mbedtls.x509` module for parsing and writing X.509
certificates.  The API complies to PEP 543.

- X.509 certificate parsing and writing.
- X.509 certificate signing request parsing and writing.
- X.509 certificate revocation list parsing.

API changes
-----------

The `import_()` and `export()` methods from `mbedtls.pk.RSA` are now called
`from_buffer()`, `from_DER()`, `from_PEM()`, and `to_DER()`, `to_DER()` to be
closer to PEP 543.

This is a breaking change.


python-mbedtls 0.7 released
===========================

What's new
----------

- `python-mbedtls 0.7 <https://pypi.python.org/pypi/python-mbedtls/0.7>`_ adds
  support for Python 2.7 and was further tested with Python 3.4, 3.5, and 3.6.
  The bindings are known to work with a few more versions.
- A short script `install-mbedtls.sh` is available for download and installs a
  local copy of mbed TLS with ``install-mbedtls.sh [VERSION] [DESTDIR]``, for
  example,

.. code-block:: console

   # ./install-mbedtls.sh 2.4.2 /usr/local

API changes
-----------

- `mbedtls.hash` and `mbedtls.hmac`: message digest algorithms with MD5,
  SHA-1, SHA-2, and RIPEMD-160.
- `mbedtls.cipher`: symmetric encryption with AES, ARC4, Blowfish, Camellia,
  and DES.
- `mbedtls.pk`: RSA cryptosystem with support for PEM and DER formats.

Miscellaneous
-------------

- The tests were ported from nosetests to pytest.
- The code is tested automatically on Circle CI.
