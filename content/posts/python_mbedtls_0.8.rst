:Date: 2018-02-25 00:15
:Modified: 2018-02-25 00:15
:Category: Python
:Tags: Python, TLS, SSL, Cryptography
:Slug: python-mbedtls-08-released

===========================
python-mbedtls 0.8 released
===========================

`python-mbedtls <https://github.com/Synss/python-mbedtls>`_ is a free
cryptographic library for Python 2.7, 3.4, 3.5, and 3.6 that uses `mbed TLS
<https://tls.mbed.org>`_ for back end.

`python-mbedtls` API follows the recommendations from `PEP 452
<https://www.python.org/dev/peps/pep-0452/>`_ and `PEP 272
<https://www.python.org/dev/peps/pep-0272/>`_ and can therefore be used as a
drop-in replacements to `PyCrypto  <https://www.dlitz.net/software/pycrypto/>`_
or Python's `hashlib <https://docs.python.org/3.6/library/hashlib.html>`_ and
`hmac <https://docs.python.org/3.6/library/hmac.html>`_.

`python-mbedtls` 0.8 features:

- `mbedtls.hash` and `mbedtls.hmac`: message digest algorithms with MD5,
  SHA-1, SHA-2, and RIPEMD-160.
- `mbedtls.cipher`: symmetric encryption with AES, ARC4, Blowfish, Camellia,
  and DES.
- `mbedtls.pk`: RSA cryptosystem with support for PEM and DER formats.
- `mbedtls.x509`: X.509 certificate writing and parsing.

Release notes
=============

API change
----------

The `import_()` and `export()` methods from `mbedtls.pk.RSA` are now called
`from_buffer()`, `from_DER()`, `from_PEM()`, and `to_DER()`, `to_DER()` to be
closer to PEP 543.

This is a breaking change.

What's new
----------

`python-mbedtls 0.8 <https://pypi.python.org/pypi/python-mbedtls/0.8>`_
features a new `mbedtls.x509` module for parsing and writing X.509
certificates.  The API complies to PEP 543.

- X.509 certificate parsing and writing.
- X.509 certificate signing request parsing and writing.
- X.509 certificate revocation list parsing.

Installation
------------

The library is available on `pypi
<https://pypi.python.org/pypi/python-mbedtls/0.8>`_ and is installed after mbed
TLS with

.. code-block:: console

   $ pip install python-mbedtls

.. code-block:: console

   # ./install-mbedtls.sh 2.4.2 /usr/local

Links
=====

- Source code: https://github.com/Synss/python-mbedtls
- Documentation: https://synss.github.io/python-mbedtls/
