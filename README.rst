yayarl
======

This library is a fork of [aio-libs/yarl](https://github.com/aio-libs/yarl).
This fork adds HTTP verbs to the URL object via `requests`.
Since yarl.URL is marked as `@final`, subclassing it with this added functionality was not possible, thus this clone was born.


Features added in this fork
---------------------------
All HTTP verbs from `requests` were added to the `URL` object. This allows you to easily perform actions on the url:

.. code-block:: pycon

   >>> from yayarl import URL
   >>> url = URL('https://www.python.org/~guido?arg=1#frag')
   >>> url
   URL('https://www.python.org/~guido?arg=1#frag')
   # new:
   >>> url.get() # performs a GET request, returns requests.Response

You can also bind a `requests.Session` to the `URL`:

.. code-block:: pycon

   >>> with requests.Session() as session:
   >>>     url &= session
   # all requests will now be performed in the same session.

Typing: before, passing a `URL` to `requests.get()` would lead to a type warning, since requests expected a simple str.
All keyword arguments for each HTTP verb are added in a pyi file, so your editor should give hints about possibile parameters.

*The original documentation follows below:*

yarl
====

The module provides handy URL class for URL parsing and changing.

Introduction
------------

Url is constructed from ``str``:

.. code-block:: pycon

   >>> from yayarl import URL
   >>> url = URL('https://www.python.org/~guido?arg=1#frag')
   >>> url
   URL('https://www.python.org/~guido?arg=1#frag')

All url parts:
   >>> from yayarl import URL
   >>> url = URL('https://www.python.org/~guido?arg=1#frag')
   >>> url
   URL('https://www.python.org/~guido?arg=1#frag')

All url parts:
   >>> from yarl import URL
   >>> url = URL('https://www.python.org/~guido?arg=1#frag')
   >>> url
   URL('https://www.python.org/~guido?arg=1#frag')

All url parts: *scheme*, *user*, *password*, *host*, *port*, *path*,
*query* and *fragment* are accessible by properties:

.. code-block:: pycon

   >>> url.scheme
   'https'
   >>> url.host
   'www.python.org'
   >>> url.path
   '/~guido'
   >>> url.query_string
   'arg=1'
   >>> url.query
   <MultiDictProxy('arg': '1')>
   >>> url.fragment
   'frag'

All url manipulations produce a new url object:

.. code-block:: pycon

   >>> url = URL('https://www.python.org')
   >>> url / 'foo' / 'bar'
   URL('https://www.python.org/foo/bar')
   >>> url / 'foo' % {'bar': 'baz'}
   URL('https://www.python.org/foo?bar=baz')

Strings passed to constructor and modification methods are
automatically encoded giving canonical representation as result:

.. code-block:: pycon

   >>> url = URL('https://www.python.org/путь')
   >>> url
   URL('https://www.python.org/%D0%BF%D1%83%D1%82%D1%8C')

Regular properties are *percent-decoded*, use ``raw_`` versions for
getting *encoded* strings:

.. code-block:: pycon

   >>> url.path
   '/путь'

   >>> url.raw_path
   '/%D0%BF%D1%83%D1%82%D1%8C'

Human readable representation of URL is available as ``.human_repr()``:

.. code-block:: pycon

   >>> url.human_repr()
   'https://www.python.org/путь'

For full documentation please read https://yarl.readthedocs.org.


Installation
------------

::

   $ pip install yarl

The library is Python 3 only!

PyPI contains binary wheels for Linux, Windows and MacOS.  If you want to install
``yarl`` on another operating system (like *Alpine Linux*, which is not
manylinux-compliant because of the missing glibc and therefore, cannot be
used with our wheels) the the tarball will be used to compile the library from
the source code. It requires a C compiler and and Python headers installed.

To skip the compilation you must explicitly opt-in by setting the `YARL_NO_EXTENSIONS`
environment variable to a non-empty value, e.g.:

.. code-block:: bash

   $ YARL_NO_EXTENSIONS=1 pip install yarl

Please note that the pure-Python (uncompiled) version is much slower. However,
PyPy always uses a pure-Python implementation, and, as such, it is unaffected
by this variable.

Dependencies
------------

YARL requires multidict_ library.


API documentation
------------------

The documentation is located at https://yarl.readthedocs.org


Why isn't boolean supported by the URL query API?
-------------------------------------------------

There is no standard for boolean representation of boolean values.

Some systems prefer ``true``/``false``, others like ``yes``/``no``, ``on``/``off``,
``Y``/``N``, ``1``/``0``, etc.

``yarl`` cannot make an unambiguous decision on how to serialize ``bool`` values because
it is specific to how the end-user's application is built and would be different for
different apps.  The library doesn't accept booleans in the API; a user should convert
bools into strings using own preferred translation protocol.


Comparison with other URL libraries
------------------------------------

* furl (https://pypi.python.org/pypi/furl)

  The library has rich functionality but the ``furl`` object is mutable.

  I'm afraid to pass this object into foreign code: who knows if the
  code will modify my url in a terrible way while I just want to send URL
  with handy helpers for accessing URL properties.

  ``furl`` has other non-obvious tricky things but the main objection
  is mutability.

* URLObject (https://pypi.python.org/pypi/URLObject)

  URLObject is immutable, that's pretty good.

  Every URL change generates a new URL object.

  But the library doesn't do any decode/encode transformations leaving the
  end user to cope with these gory details.


Source code
-----------

The project is hosted on GitHub_

Please file an issue on the `bug tracker
<https://github.com/aio-libs/yarl/issues>`_ if you have found a bug
or have some suggestion in order to improve the library.

The library uses `Azure Pipelines <https://dev.azure.com/aio-libs/yarl>`_ for
Continuous Integration.

Discussion list
---------------

*aio-libs* google group: https://groups.google.com/forum/#!forum/aio-libs

Feel free to post your questions and ideas here.


Authors and License
-------------------

The ``yarl`` package is written by Andrew Svetlov.

It's *Apache 2* licensed and freely available.


.. _GitHub: https://github.com/aio-libs/yarl

.. _multidict: https://github.com/aio-libs/multidict
