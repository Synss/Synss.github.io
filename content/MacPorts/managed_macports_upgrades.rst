Managed MacPorts upgrades: Deciding what upgrades are needed
============================================================

:Date: 2014-10-07 21:00
:Slug: managed-macports-upgrades-1
:Tags: MacPorts, shell


Upgrading a full MacPorts install (the package manager for OS X) install can be
time consuming.  Here, I will show how ``port echo requested and outdated``
helps limiting the upgrade to the program that are really important to you.

.. PELICAN_END_SUMMARY

Introdution
-----------

MacPorts is a package manager for OS X.  It facilitates the installation of a
large amount of open source applications.  It was modeled after BSD's ports and
compiles everything from source.  The recommended upgrade process is ``port
upgrade outdated`` but upgrades may pull new dependencies and install more
packages than listed under ``port echo outdated``, requiring erratic upgrade
times.

On the way to managed MacPorts upgrade, I will show how you can make an educated
choice on what should be upgraded now and what can wait.  In the next post, I
will introduce ``port_deptree``, a program displaying what MacPorts is actually
about to do.  And in a third post, I will show that ``port_deptree`` can help
making educated guesses on the choice of variants.

Requested and outdated
----------------------

After updating MacPorts' base with ``port selfupdate``, `port` invites the user
to run ``port upgrade outdated``.  This may not be the most time-efficient
solution, especially if you do not upgrade the ports very often.

Is upgrading every outdated port necessary?  Probably not.  As one can see from

.. code-block:: bash

   $ echo '1+3,$-3d\n%p' | ed -s <(port echo outdated | nl)
     1	atk                            @2.12.0_0 
     2	gcc48                          @4.8.2_2 
     3	gdk-pixbuf2                    @2.30.8_0 
    26	vala                           @0.24.0_0 
    27	webp                           @0.4.0_0 
    28	yasm                           @1.2.0_0 

many of the proposed upgrades are dependencies of the ports we are actually
interested in.  Upgrading them is very unlikely to have direct benefits.

For example, `gcc48` takes a *really* long time to compile and it is a build
dependency: no package relies on it being up to date.  It is only used to
compile other packages.

It would be simpler to only upgrade the packages we need *now*, eventually with
their dependencies as they may contain bug fixes, security fixes, etc.

Since MacPorts 1.9.0, ports have a `requested` flag that indicates whether ports
were installed explicitly or as dependencies.  These are the ports that we
actually care for.  One can list them with

.. code-block:: bash

   $ echo '1+3,$-3d\n%p' | ed -s <(port echo requested | nl)
     1	ack                            @2.120.0_0 
     2	autoconf                       @2.69_2 
     3	automake                       @1.14.1_2 
    56	unrar                          @4.2.4_1 
    57	watch                          @3.3.6_0 
    58	yasm                           @1.2.0_0 

The list is maintained with ``port setrequested`` and ``port unsetrequested``.

The list of outdated requested ports can thus be obtained from the shell

.. code-block:: bash

   $ comm -12 <(port echo outdated | sort -n) <(port echo requested | sort -n)

or with `port`

.. code-block:: bash

   $ port echo requested and outdated | nl
     1	gcc48                          @4.8.2_2 
     2	git                            @2.1.1_0+credential_osxkeychain+doc+pcre+perl5_16+python27 
     3	gnupg                          @1.4.16_0 
     4	ImageMagick                    @6.8.9-1_0+no_x11 
     5	py27-networkx                  @1.9_0 
     6	py27-virtualenv                @1.11.4_1 
     7	texinfo                        @5.2_0 
     8	yasm                           @1.2.0_0 

8 ports that I know because I explicitly requested their installation.  So out
of the 28 outdated ports reported, I can now reduced the choice to 8.  It is now
up to me to decide which of these should be upgraded.

So now we have decided what *we* want to upgrade.  In the next post, we will see
what *MacPorts* will want to do from here.

Notes
-----

- Link to the `MacPorts <https://www.macports.org>`_ project official homepage.
- ``comm(1)`` is used to select the lines common to two files.
- ``nl(1)`` numbers the lines.
- with zsh, an alternative to ``echo '1+3,$-3d\n%p' | ed -s <( CMD )`` is
  ``CMD | tee <(head -3) | tail -3``. In any case, it selects the first and
  last three lines of a file or stdin.
