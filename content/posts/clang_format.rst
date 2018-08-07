Coding standards gone wrong
===========================

:Date: 2018-08-07 21:00
:Category: QA
:Tags: Quality, Management, C++


Summary
-------

I personally believe in standards insofar they magically get rid of the
petty stuff.  So here is ``clang-format`` for you.  Nothing can go wrong,
right?  Or can it?

Here are some more things to consider when adopting a formatting tool.

.. PELICAN_END_SUMMARY

We are adopting a standard!
---------------------------

It was hard enough to convince every body that ``clang-format`` is better
than what we have now (aka nothing).  There is no way adopting a
configuration from a foreign company will cut it.  So we democratically
adopt our own configuration.  After some deliberation, it is finally done:
Every body is happy.  We finally have a way to enforce conformance to
*something* and this is a step up, quality-wise.

What can go wrong?
------------------

Well something is wrong when ``clang-format`` is responsible for the
majority of the changes for *every* pull request.

It is wrong because it makes ``git blame`` useless.  It is wrong
because it is now a policy that whitespace changes and code changes
are merged into one commit.  Finally it is wrong because it adds
noise to the code review and not only does this cost time but
mistakes are going to be overlooked.


What went wrong?
----------------

Something went wrong in the requirements.  It is important to have
standards. *Per se.*  And that includes formatting standards because
some people do care and format their code properly and some people
don't.  Adopting a formatting standard is therefore a first
measurable step toward quality.

It just is not enough.  If code is read more than written, this most
obviously holds for code reviews where it *must* be read.  Formatting
standards should therefore be *required* to minimize changes.

So forget about aligning those equal signs and putting as much as possible
on a single line.  The former will reformat *everything* when the size of
the longest line changes.  The latter will reformat the code once the line
exceeds the maximum line length.

Conclusion
----------

Go for a big name standard like LLVM or Google.  Whatever they do it is
good enough for us.  Even if some contradict this post.  If this is not
possible, aim at invariance under refactoring and you will actually do
better than the big names.

This is a fictitious story by the way.
