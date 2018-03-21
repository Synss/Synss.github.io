==============================================
How to install PyQt5 for Python 2.7 on Windows
==============================================

:Date: 2018-03-21 20:00
:Modified: 2018-03-22 00:00
:Category: Python
:Tags: Python, Qt

Summary
-------

Installing PyQt5 for Python 3 on Linux is as easy as ``pip install pyqt5`` but
Python 2.7 on Windows is a completely different story.  Here is a step by step
installation guide for the latest PyQt5 on Python 2.7 for Windows.

After the necessary prerequisites, we set up a virtual environment
where to install PyQt5 *from source*.  We then test our installation with a
simple GUI application.  Finally, we build the GUI app to make sure that it is
usable outside of the virtual environment.


Necessary libraries and programs
--------------------------------

Visual Studio Express
~~~~~~~~~~~~~~~~~~~~~

Visual Studio Express gives us MSVC and nmake that are necessary to compile
PyQt5.

* Download from `visualstudio.com <https://www.visualstudio.com/vs/visual-studio-express/>`_
* Complete a default installation.


Latest Python 2.7 32-bits
~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: SIP is not available for Python 2.7 64-bits.

* Download from `python.org <https://www.python.org/downloads/>`_
* Install to ``C:\Python27`` (the default location).


Qt
~~

* Download `qt-unified-windows-x86-online <https://download.qt.io/official_releases/online_installers/>`_
* Run the installer.
* Install::

  | ├─ Qt 5.10.1
  |    ├─ msvc2015 32-bits

SIP and PyQt5 sources
~~~~~~~~~~~~~~~~~~~~~

* Download the latest version of SIP and extract the archive to ``%HOMEPATH%``.
* Download the latest PyQt5 and extract the archive to ``%HOMEPATH%``.

Virtual environment and PyQt5
-----------------------------

All the steps in this section should be performed *in a single session* in the
developer command prompt installed with Visual Studio.  The developer command
prompt can be found by searching for `dev` in the Start Menu.  See
`docs.microsoft.com
<https://docs.microsoft.com/en-us/dotnet/framework/tools/developer-command-prompt-for-vs>`_
for details.


virtualenv
~~~~~~~~~~

Make sure that `pip` is available and create a virtual environment in
``%HOMEPATH%\venv``.

.. code-block:: doscon

   C:\> C:\Python27\python -m ensurepip
   C:\> C:\Python27\python -m pip install virtualenv
   C:\> C:\Python27\python -m virtualenv --always-copy %HOMEPATH%\venv

Activate the virtual env and verify that it uses python 2.7.

.. code-block:: doscon

   C:\> %HOMEPATH%\venv\Scripts\activate
   C:\> python --version
   Python 2.7.14

SIP 4.19.8
~~~~~~~~~~

In the same session, change the directory to the SIP sources.

.. code-block:: doscon

   C:\> cd %HOMEPATH%\sip-4.19.8
   C:\...\sip-4.19.8> set LIB=%LIB%;c:\Python27\libs;
   C:\...\sip-4.19.8> python configure.py --platform=win32-msvc2015
   C:\...\sip-4.19.8> set CL=/MP
   C:\...\sip-4.19.8> nmake
   C:\...\sip-4.19.8> nmake install

The `/MP` switch enables parallel builds to speed up the installation.


PyQt5 5.10.1
~~~~~~~~~~~~

In the same session, change directory to the PyQt sources.

.. code-block:: doscon

   C:\...\sip-4.19.8> cd ..\PyQt5_gpl-5.10.1
   C:\...\PyQt5_gpl-5.10.1> set _QTVERSION=5.10.1
   C:\...\PyQt5_gpl-5.10.1> set LIB=%LIB%;C:\Qt\%_QTVERSION%\msvc2015\lib;
   C:\...\PyQt5_gpl-5.10.1> set PATH=%PATH%;c:\Qt\%_QTVERSION%\msvc2015\bin;
   C:\...\PyQt5_gpl-5.10.1> python configure.py ^
       --confirm-license ^
       --no-designer-plugin ^
       --no-qml-plugin ^
       --assume-shared ^
       --disable=QtNfc ^
       --qmake=C:\Qt\%_QTVERSION%\msvc2015\bin\qmake.exe ^
       --sip=%VIRTUAL_ENV%\Scripts\sip.exe
   C:\...\PyQt5_gpl-5.10.1> nmake
   C:\...\PyQt5_gpl-5.10.1> nmake install

QtNfc does not build and *must* be disabled.

.. note:: Once SIP and PyQt5 have been built, they can be installed in a
   different virtual env with `nmake install` only.

Test the installation
---------------------

We can now test the installation with a simple GUI application.

Simple GUI application
~~~~~~~~~~~~~~~~~~~~~~

Copy the following program to ``%HOMEPATH%\testgui\testgui.py``.

.. code-block:: python

   # testgui\testgui.py
   import sys

   from PyQt5 import QtWidgets


   def main(argv):
      app = QtWidgets.QApplication(argv)
      app.lastWindowClosed.connect(app.quit)
      gui = QtWidgets.QWidget()
      gui.show()
      sys.exit(app.exec_())


   if __name__ == "__main__":
      main(sys.argv)


In the same session as above, start `testgui` from the command prompt with:

.. code-block:: doscon

   C:\...\testgui> python testgui.py

You should see something like this:

.. image:: /images/testgui.png
   :alt: The TestGui app with an empty window.


Freeze and create a redistributable executable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now we also want to make sure that we can build a GUI application and
redistribute it outside of our local virtual environment.  Let us adapt the
`example for PyQt5 <https://github.com/anthony-tuininga/cx_Freeze/tree/master/cx_Freeze/samples/PyQt5>`_
from `cx_Freeze <https://github.com/anthony-tuininga/cx_Freeze>`_.

.. code-block:: python

   # testgui/setup.py
   from cx_Freeze import setup, Executable


   __version__ = "0.0.0"

   options = dict(
      build_exe=dict(
         packages=[],
         excludes=["Tkinter"],
         includes=["atexit"]
      )
   )
   executables = [Executable("testgui.py", base="Win32GUI")]


   setup(name="TestGui",
         version=__version__,
         author="",
         author_email="",
         python_requires="==2.7.*",
         requires=["PyQt5"],
         options=options,
         executables=executables)

and build

.. code-block:: doscon

   C:\...\testgui> python -m pip install cx_freeze
   C:\...\testgui> python setup.py build

Now, open the explorer at ``%HOMEPATH%\testgui\`` and navigate to
``build\exe.win3202.7\``.  `testgui.exe` should open the same window as above.


Conclusion
----------

We did it!  We installed PyQt5 for Python 2.7 under Windows and created a
useless but working GUI application.
