Visualizing MacPorts' dependency tree
=====================================

:Date: 2014-12-27 22:50
:Slug: managed-macports-upgrade-2
:Tags: MacPorts, shell, Graphviz


Summary
-------

`port_deptree.py`_ is a free python program that creates the dependency
graphs from MacPorts ports.  It can be used to see the effect of
variants and to show what ports would be upgraded, or installed during
an upgrade.

Story
-----

`Managed MacPorts upgrades <|filename|managed_macports_upgrades.rst>`_
shows how to obtain the list of ports that are both requested and
outdated, i.e., the ports that should be upgraded first.  Visualizing
the dependency tree is the next step towards managed upgrades.

Installation
~~~~~~~~~~~~

`port_deptree.py`_ is a Python program that generates a graphic
representation of the dependency tree.  It actually writes a dot file to
``stdout`` that can be piped to one of the programs from the `graphviz`_
suite, such as ``dot``.  `pydot` is therefore a required dependency that
can be installed with ``port install py-pydot``.  `port_deptree.py` can
be downloaded `here
<https://github.com/Synss/macports_deptree/archive/current.zip>`__.

Now let us see a couple of cases where `port_deptree` might be useful.

View and analyze port upgrades
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``port echo outdated`` now displays 38 ports on a system that I have not
upgraded for some time.  We can therefore expect a large graph for
`requested and outdated` and there is no need to look at it in details.
Very general information is simply obtained by directing the graph to
``/dev/null`` and concentrating on the statistics line that is printed
to ``stderr``.

.. code-block:: console

   $ port_deptree.py $(port echo requested and outdated) 1> /dev/null
   Calculating dependencies for py27-pip
   Calculating dependencies for openconnect
   Calculating dependencies for py27-matplotlib
   Calculating dependencies for git
   Calculating dependencies for ImageMagick
   Calculating dependencies for cairo
   Calculating dependencies for py27-enum34
   Calculating dependencies for yasm
   Calculating dependencies for gnupg
   Calculating dependencies for texinfo
   Calculating dependencies for py27-ipython
   Total: 199 (33 upgrades, 52 new)

33 upgrades available that would pull an extra 52 dependencies, it is
worth looking into before actually upgrading.

Among these 11 requested and outdated ports is `ipython` that I heavily
depend upon and that does not usually pull new dependencies.  Let us now
look at the dependency tree for this one port.

.. code-block:: console

   $ port_deptree.py py27-ipython | dot -Tpdf | open -fa Preview
   Calculating dependencies for py27-ipython
   Total: 57 (5 upgrades, 5 new)

.. image:: /images/20141227/ipython.svg
   :width: 42em

The graph `[enlarge] </images/20141227/ipython.svg>`__ is relatively
large but only the colored nodes are relevant.  The graphs generally
read as follows:

- roots and leaves are enclosed in a double circle;
- green nodes would be upgraded;
- yellow nodes would be newly installed.

Conversely, `ImageMagick` and `py27-matplotlib` are most likely
candidates for the extra dependencies, let us check:

.. code-block:: console

   $ port_deptree.py py27-matplotlib ImageMagick | dot -Tpdf | open -fa Preview
   Calculating dependencies for py27-matplotlib
   Calculating dependencies for ImageMagick
   Total: 138 (23 upgrades, 48 new)

.. image:: /images/20141227/matplotlib_imagemagick.svg
   :width: 42em

The cluster of new (yellow) ports on the left `[enlarge]
</images/20141227/matplotlib_imagemagick.svg>`__ is Xorg, a dependency of
`tk` that comes as a new dependency of `py27-matplotlib`.  The other
cluster results mostly from `gtk-doc` that is a build dependency to
`librsvg`, coming after `ImageMagick`.  One can also notice `boost` on
that side, a port that can take a very long time to build.

Upgrading the other ports is most likely quick.  Let us leave
`ImageMagick` and `matplotlib` out and check.

.. code-block:: console

   $ port_deptree.py $(port echo requested and outdated\
      | grep -ve ImageMagick -e py27-matplotlib)\
      | dot -Tpdf | open -fa Preview
   Calculating dependencies for py27-pip
   Calculating dependencies for openconnect
   Calculating dependencies for git
   Calculating dependencies for cairo
   Calculating dependencies for py27-enum34
   Calculating dependencies for yasm
   Calculating dependencies for gnupg
   Calculating dependencies for texinfo
   Calculating dependencies for py27-ipython
   Total: 116 (15 upgrades, 5 new)

.. image:: /images/20141227/all_but.svg
   :width: 42em

This upgrades 6 dependencies and the 9 ports we have requested
`[enlarge]  </images/20141227/all_but.svg>`__ and the 5 extra
dependencies from ipython.

Help choosing variants
~~~~~~~~~~~~~~~~~~~~~~

We are left with `ImageMagick` and `py27-ipython`, let us see what can
be done with `ImageMagick`.

.. code-block:: console

   $ port_deptree.py ImageMagick | dot -Tpdf | open -fa Preview
   Calculating dependencies for ImageMagick
   Total: 99 (15 upgrades, 29 new)

.. image:: /images/20141227/imagemagick.svg
   :width: 42em

The largest provider of new ports `[enlarge]
</images/20141227/imagemagick.svg>`__ is thus `gtk-doc` from `librsvg`.
We can check whether it is optional.

.. code-block:: console

   $ port variants librsvg
   librsvg has the variants:
   (+)quartz: Support for native Mac OS X graphics
         * conflicts with x11
      universal: Build for multiple architectures
   [+]viewer: Enable the build of the rsvg-view-3 utility.
   (-)x11: Enable X11 support
         * conflicts with quartz

It does not seem so.  Searching the `MacPorts` tracker shows that
`gtk-doc` is a new dependency in 2.20.2.  We can try to compile
`librsvg` without `gtk-doc` and eventually report back to the `MacPorts`
project.

Further inspection of the graph shows that `librsvg` is not a direct
dependency of `ImageMagick`.  `ImageMagick` was compiled without SVG
support.

.. code-block:: console

   $ port variants ImageMagick
   ImageMagick has the variants:
      graphviz: Support Graphviz
      lqr: Support Liquid Rescale (experimental)
      pango: Support Pango
      rsvg: Support SVG using librsvg
      universal: Build for multiple architectures
      wmf: Support the Windows Metafile Format
   (-)x11: Enable X11 support

Since `librsvg` is the dependency of a required dependency, adding SVG
support to `ImageMagick` is free so that enabling the `rsvg` variant is
free.

.. code-block:: console

   $ port_deptree.py ImageMagick +rsvg 1> /dev/null
   Calculating dependencies for ImageMagick +rsvg
   Total: 99 (15 upgrades, 29 new)

As expected, we have the same number of upgrades with or without, we
might as well add it.

Conclusion
----------

We now have the tools to know precisely what changes will be made to the
system when issuing a ``port upgrade``.  This allows us to decide what
upgrades can be safely done now and estimate how long they will take.
We can also decide to upgrade some packages without their dependencies
using the ``-n`` flag.  `port_deptree.py`_ can also be used to decide to
add support for some variants, or not.

.. _`github`: https://github.com/Synss/macports_deptree.git
.. _`graphviz`: http://graphviz.org
.. _`port_deptree.py`: https://github.com/Synss/macports_deptree
