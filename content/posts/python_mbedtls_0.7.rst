python-mbedtls 0.7 released
===========================

:Date: 2018-02-17 17:00
:Category: Python
:Tags: Python, TLS

`python-mbedtls <https://github.com/Synss/python-mbedtls>`_ is a free
cryptographic library for Python that uses `mbed TLS <https://tls.mbed.org>`_
for back end.

`python-mbedtls` API follows the recommendations from `PEP 452: API for
Cryptographic Hash Functions v2.0 <https://www.python.org/dev/peps/pep-0452/>`_
and `PEP 272 API for Block Encryption Algorithms v1.0
<https://www.python.org/dev/peps/pep-0272/>`_ and can therefore be used as a
drop-in replacements to `PyCrypto  <https://www.dlitz.net/software/pycrypto/>`_
or Python's `hashlib <https://docs.python.org/3.6/library/hashlib.html>`_ and
`hmac <https://docs.python.org/3.6/library/hmac.html>`_.

`python-mbedtls` 0.7 features:

- `mbedtls.hash` and `mbedtls.hmac`: message digest algorithms with MD5,
  SHA-1, SHA-2, and RIPEMD-160.
- `mbedtls.cipher`: symmetric encryption with AES, ARC4, Blowfish, Camellia,
  and DES.
- `mbedtls.pk`: RSA cryptosystem with support for PEM and DER formats.

The library is available on `pypi 
<https://pypi.python.org/pypi/python-mbedtls/0.7>`_ and is installed after
mbed TLS with

.. code-block:: console

   $ pip install python-mbedtls


Release notes
-------------

- `python-mbedtls 0.7 <https://pypi.python.org/pypi/python-mbedtls/0.7>`_ adds
  support for Python 2.7 and was further tested with Python 3.4, 3.5, and 3.6.
  The bindings are known to work with a few more versions.
- A short script `install-mbedtls.sh` is available for download and installs a
  local copy of mbed TLS with ``install-mbedtls.sh [VERSION] [DESTDIR]``, for
  example,

.. code-block:: console

   # ./install-mbedtls.sh 2.4.2 /usr/local

Miscellaneous
-------------

- The tests were ported from nosetests to pytest.
- The code is tested automatically on Circle CI.

Links
-----

- Source code: https://github.com/Synss/python-mbedtls
- Documentation: https://synss.github.io/python-mbedtls/
