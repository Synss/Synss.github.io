PyQt: Loading resource UI files directly
========================================

:Date: 2014-10-07 21:00
:Modified: 2018-02-10 12:00
:Category: Qt
:Tags: Python, Qt


Abtract
-------

Loading Designer's UI files directly is a simple matter of calling
``uic.loadUi(uifile, self)`` from a `QWidget`, where `uifile` is the
path to the file.  If `uifile` is stored as a resource files, however,
it must first be opened in a `QFile` and loaded.

This works with PyQt4, PyQt5, and PySide.


Story
-----

Designing Qt graphical user interfaces (GUI) with Designer presents
several advantages.  GUIs may be written and modified by
non-programmers.  It also naturally enforces a strict separation between
the GUI and the business logic of the application.

The documented way of turning UI files into Python is to run

.. code-block:: console

   $ pyuic4 window.ui -o window.py

and load the ``window.py`` module.  Use ``pyuic5`` for Qt5 GUIs.

Now, the conversion is not strictly necessary as the ``uic`` module can
directly load `ui` files.

.. code-block:: python

   import sys
   from PyQt4 import QtCore, QtGui, uic
   Qt = QtCore.Qt

   def main(uifile):
      app = QtGui.QApplication([])
      app.lastWindowClosed.connect(app.quit)
      w = QtGui.QMainWindow()
      uic.loadUi(uifile, w)
      w.show()
      sys.exit(app.exec_())

   if __name__ == "__main__":
      main(sys.argv[1])

Run with

.. code-block:: console

   $ python ./test.py rsc/ui/window.ui


This has the drawback of requiring a path and it will break if the
program is reorganized.

Files that do not contain code are actually better stored as resources
using the Qt Resource System.  So let us write the resource file,

.. code-block:: xml

   <!DOCTYPE RCC><RCC version="1.0">
   <qresource>
      <file>ui/window.ui</file>
   </qresource>
   </RCC>

save it as ``rsc/rsc.qrc``, and digest it with ``pyrcc4`` or ``pyrcc5``

.. code-block:: console

   $ pyrcc4 -o rsc.py rsc/rsc.qrc

We tell PyQt that we have a resource file by importing `rsc.py`,

.. code-block:: python

   import sys
   import rsc  # This is the new line
   from PyQt4 import QtCore, QtGui, uic

   # the rest as before ...

try to load the resource file,

.. code-block:: console

   $ python ./test.py :ui/window.ui

and **fail**!

Trying to open the file using Python's own ``with open(uifile, "rb") as
uifile:`` fails as well.  Python does not know about Qt's Resource
System.

The solution is therefore to open the file with Qt's `QFile`:

.. code-block:: python

   import sys
   import rsc
   from PyQt4 import QtCore, QtGui, uic
   Qt = QtCore.Qt

   def main(uifile=""):
      app = QtGui.QApplication([])
      app.lastWindowClosed.connect(app.quit)
      w = QtGui.QMainWindow()
      try:
         uic.loadUi(uifile, w)
      except IOError:
         # Fallback
         uifile = QtCore.QFile(":/ui/window.ui")
         uifile.open(QtCore.QFile.ReadOnly)
         uic.loadUi(uifile, w)
         uifile.close()
      w.show()
      sys.exit(app.exec_())

   if __name__ == "__main__":
      main(sys.argv[1:])

And test with

.. code-block:: console

   $ python ./test2.py rsc/ui/window.ui  # load filename
   $ python ./test2.py  # load from resource

Et voilà how to have one's cake and eat it too.


Notes
-----

- Documentation for `the Qt Resource System
  <http://qt-project.org/doc/qt-4.8/resources.html>`_
