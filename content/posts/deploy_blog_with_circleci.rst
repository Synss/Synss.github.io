Deploy a static website using continuous integration
====================================================

:Date: 2018-02-17 14:00
:Category: CI
:Tags: Continuous Integration

Summary
-------

Setting up a CI host to deploy a static website like this one is really
easy and makes writing posts about as simple as editing a wiki: write,
read-proof, and save.  CI then takes over and generates the HTML, checks
the links, runs doctest for Python, and deploys the website.

.. PELICAN_END_SUMMARY


Introduction
------------

I started this blog in December 2014 and wrote a few more posts in 2015
or 2016.  I then stopped for a while.  My biggest hindrance (felt or
real) was administrating the website.  However, CI can easily take care
of the publication.

Here is a step by step tutorial on setting up a web server and a CI
server to publish a static website.


Prerequisite
~~~~~~~~~~~~

The prerequisites are that the website builds locally and the web server
is configured.

I am personally using github, Circle CI and a server by Digital Ocean
but this tutorial can be adapted to other services.  For the blog
itself, I am using Pelican but here again, other static website
generators are just as good.


Server: Add a CI user with limited access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CI must have access to the web server in order to copy the generated
HTML files to the webroot.  However, a good safety measure is to give CI
its own limited account.

So, let us install `rssh` (a `restricted shell
<http://www.pizzashack.org/rssh/>`_) on the web server

.. code-block:: console

   # aptitude install rssh rsync

and uncomment `rsync` in ``/etc/rssh.conf``.

Now, we can add a `circleci` user to the web server with

.. code-block:: console

   # useradd --groups www-data --shell /usr/bin/rssh circleci

This user is now able to put files onto the web server over rsync.  Now,
we should authorize `circleci` to write to the web root,

.. code-block:: console

   # chown circleci:www-data /var/www/example.com/public_html
   # chmod g+s /var/www/example.com/public_html

where `example.com` is the website.  That is, `synss.me` in my case.


Local: Generate a new SSH key for the CI user
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Back to our regular computer, we now generate an ssh key pair for
our `circleci` user.

.. code-block:: console

   ssh-keygen -t rsa -b 4096 -C "circleci@example.com"

Save without password to ``$HOME/.ssh/circleci@example.com_rsa``.


Server: Authorize the SSH key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We log in to the web server as root again and copy the public half of
the SSH key to ``/home/circleci/.ssh/authorized_keys``.

.. code-block:: console

   # cd /home/circleci
   # mkdir .ssh
   # chmod 700 .ssh
   # chown circleci:circleci .ssh

Copy-paste the public key from ``$HOME/.ssh/circleci@example.com_rsa.pub``
and set the rights appropriately:

.. code-block:: console

   # # On the web server after copying the key to authorized_keys:
   # chmod 600 /home/circleci/.ssh/authorized_keys
   # chown circleci:circleci /home/circleci/.ssh/authorized_keys

Local: Test SSH access
~~~~~~~~~~~~~~~~~~~~~~

Let us check that everything is working by copying a file to the web
root on behalf of `circleci`:

.. code-block:: console

   $ echo 'ok' >> ok.txt
   $ ssh-add ~/.ssh/circleci@example.com_rsa
   $ rsync -e "ssh" ok.txt circleci@example.com://var/www/example.com/public_html/

Now, ``ok.txt`` should be accessible at ``http://example.com/ok.txt``.


CI: Add the private key
~~~~~~~~~~~~~~~~~~~~~~~

We still need to configure the CI server to use the SSH key.  On
`circleci.com <https://circleci.com/dashboard>`_, go to ``dashboard ->
projects -> <PROJECT> -> SSH Permissions --> Add SSH key`` and add the
private key.  Circle CI should now display the fingerprint of the key.


Local: Edit `.circleci/config`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We let the CI config know about the key.  After something like:

.. code-block:: yaml

   - run:
     name: generate site
     command: |
       . venv/bin/activate
       make html

add (from `add_ssh_keys <https://circleci.com/docs/2.0/configuration-reference/#add_ssh_keys>`_)

.. code-block:: yaml

   - add_ssh_keys:
     fingerprints:
       - "de:ad:be:ef..."  # The actual fingerprint

Note that making the fingerprint public is **not** a security risk.

Let CI deploy the website as we push to the master branch:

.. code-block:: yaml

   - deploy:
     name: publish site
     command: |
       if [ "$CIRCLE_BRANCH" = "master" ]; then
         . venv/bin/activate
         make rsync_upload
       fi

We need to add `-oStrictHostKeyChecking=no` to the `rsync_upload` stanza
of the Pelican Makefile.  Otherwise, SSH would prompt CI to accept the
host.


Conclusion
~~~~~~~~~~

That's it.  After this one time setup, Circle CI automatically deploys
and publishes the articles pushed to the master branch.
