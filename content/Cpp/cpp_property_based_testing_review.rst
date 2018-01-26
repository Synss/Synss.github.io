Review of property-based testing libraries for C++
==================================================

:Date: 2016-04-15 23:29
:Modified: 2018-01-26 22:06
:Category: C++
:Tags: C++, Testing


Introduction
------------

I first heard of property-based testing in `Bryan O'Sullivan's talk`_ on
"Running a startup on Haskell" where he said that even non-Haskell
programmers should know about property-based testing (PBT).  PBT is

   designed to assist in software testing by generating test cases for
   test suites.  (`wikipedia`_)

The idea behind PBT is to run the test suite against a set of lose
assumptions specified by the programmer.  The test suite generates tests
to falsify these assumptions and eventually presents a minimal failing
case for further investigation.

So here is what I found regarding PBT libraries in the C++ world.  Note
that this is strictly a review of the libraries I found as I have not
(yet) used any of the libraries presented here.


Review
------

Apparently the first PBT library for C++ was `QuickCheck++`_ (GPLv3)
developed between 2009 and 2012 by Cyril Soldani at LegiaSoft.  It
features extensive documentation and is a header-only library.  The
licensing of a testing library does not impose too much on the software
being tested because the tests are not usually linked into the programs.

The next effort is seen in `CppQuickCheck`_ (BSD, github) started in
2010 by Greg Rogers and still accepting patches with the latest
contribution from 2015.  The author acknowledges QuickCheck++ and adds
support for *generator combinators* and *shrinking*.

`autocheck`_ (MIT, github) was developed in 2012-2013 by John Freeman
and is still accepting patches with the latest contribution from 2015.
Also a header-only library, it acknowledges the first two for
inspiration and proposes "numerous improvements with C++11 features"
(quote from the `wiki
<https://github.com/thejohnfreeman/autocheck/wiki>`_).

The last one I could find is `rapidcheck`_ (BSD, github) developed by
Emil Erikson for Spotify from 2014 on and still active in 2016.  The
author acknowledges `autocheck` in a discussion on `reddit
<https://www.reddit.com/r/cpp/comments/342jtv/rapidcheck_property_based_testing_for_c/>`_
but adds support for *generator combinators* and *shrinking* making the
case that shrinking is the most valuable.  `rapidcheck` further
advertises integration with Boost Test, Google Test, and Google Mock.
Examples of such are presented in a further `blog post
<https://labs.spotify.com/2015/06/25/rapid-check/>`_ by the author.


Conclusion
----------

I would probably go with the latest one first as it is still being
actively developed and seems to be the most modern and feature-complete.


.. _wikipedia: https://en.wikipedia.org/wiki/QuickCheck
.. _Bryan O'Sullivan's talk: https://www.youtube.com/watch?v=ZR3Jirqk6W8
.. _QuickCheck++: http://software.legiasoft.com/quickcheck/
.. _CppQuickCheck: https://github.com/grogers0/CppQuickCheck
.. _autocheck: https://github.com/thejohnfreeman/autocheck.git
.. _rapidcheck: https://github.com/emil-e/rapidcheck
