Historical perspective on software management: Winston Royce and the waterfall
==============================================================================

:Date: 2018-06-16 09:00
:Category: MNGMT
:Tags: Agile development, Waterfall, Management
:Slug: historical-perspective-on-software-management-1
:Status: draft

Summary
-------

  In the beginning was the waterfall.

  Kent Beck, Embracing Change with Extreme Programming (1999) Computer, 70--77.

.. PELICAN_BEGIN_SUMMARY

What is the waterfall software development model *really*?  Is it that bad?

Let us summarize and review the original Winston Royce paper from 1970 and
compare it to modern methodologies.

.. PELICAN_END_SUMMARY

Introduction
------------

This is part one of a series of articles on the management of software projects.

In "Managing the development of large software systems" (1970) IEEE WESCON,
Winston Royce reviews successful management strategies he developed in the
1960s at Lockheed when working on various space projects.

Interestingly, WR names his process "the five-step process".  "Waterfall"
appears in other papers that reference this paper.

In this article, we keep the structure of the original paper.

Introduction of the paper
-------------------------

The goal of the method is to arrive "at an operational state, on time, and
within costs".

.. Note:: This is the every standing problem of software development.  The
   cost of development increases with time.  This is the 1970 version of the
   solution.  In the 90s, OOP was the solution (Bertrand Meyer, Object-Oriented
   Software Construction, 1988).  In 2000s, agile methodologies Kent Beck first
   book --- cite pages!

It is important here to put the paper in perspective.  A computer in the
1960s ... Simula ... C did not exist yet ...

[image of waterfall as seen everywhere --- not waterfall]


  In my experience, however, the simpler method has never worked on large
  software development efforts and the costs to recover far exceeded those
  required to finance the five-step process listed.

To motivate his new approach, WR presents an iterative process where each phase
produces feedback to the previous phase.

.. continue here

WR writes that the steps identified (including feedback) are useful but that
following this plan exclusively is "risky and invites failure".  The reason is
the lack of flexibility as any problem occurring late in the development may
require a rewrite and double the costs.

.. Note:: This addresses the usual criticism to this model here right in 1970.

WR then goes through five extra steps required to reduce the costs.

Step 1: Program design comes first
----------------------------------

WR writes that a "preliminary program design phase" should occur between
"requirements generation" and "the analysis phase".  The goal of this
preliminary design is to provide feedback to the analysts and foster
communication between analysts and designers.

A minimal, working program is written to verifies the preliminary design and
controls the requirements on the hardware ("storage, timing, and data flux").

.. Note:: This is the "walking skeleton" from agile methodologies like A.
   Cockburns's Crystal.

Finally, this preliminary design comes before the analysis.  In other words,
development starts before analysis and it is the designers who give an early
feedback to the analysts and not the other way around.

Step 2: Document the design
---------------------------

To WR, documentation is crucial.

 If the documentation is in serious default my first recommendation is simple.
 Replace project management.

And for a budget of 5 million dollars, he expects a 30 page specification for a
hardware device but a 1500 page specification for software.

This is a lot and probably something that we would not like doing.  However,
we should review the motivations for that much documentation:

 1. Communication with interface designers, management, and customers.
 2. Document the design as the design is the specification.
 3. Communicate the specifications to the testers.

The last point is further detailed: The documentation allows the identification
of errors and prove the correctness of the design as well as permit "effective
redesign, updating, and retrofitting in the field."


.. Note:: It is clear that the huge amount of documentation has the same goal
   as the huge amount of automated tests produced by test-driven development
   or XP.  That is, permit redesign (refactoring), find bugs, or make sure that
   bugs are not software bugs, or prove operations, permit updates and
   maintenance, and prevent regressions.

   When written correctly, tests have advantages over documentation.  They
   consist in working code and running a test suite is typically faster than
   insuring that a program is consistent with 1500 pages of documentation.

   It is also easier to modify working code (the tests) to accomodate changes
   in the requirements.

Step 3: Do it twice
-------------------

Here, WR proposes to use 1/4 of the allowed time to write a "pilot model".
This pilot model is to be done by developers with "a very special kind of broad
competence. [...] They must have an intuitive feel for analysis, coding, and
program design.

So the "pilot model" is done first and is a complete design with
documentation and tests.  This step should provide feedback to every one of the
following development steps.  It is also not required to be the final design.

Here, WR precises Step 1.  One of the early steps is also used throughout the
development.

.. Note:: At this point, the WR model is everything but a strictly linear
   process.  WR also introduces iterations where a program (complete with
   documentation and tests) is obtained and built upon in the following steps.

Step 4: Plan, control and monitor testing
-----------------------------------------

WR states that the goal of the previous steps is to facilitate testing.  One
role of the testers is to control that the documentation is correct and the
role of the documentation is to help testers (in short: testers provide
feedback to the developers and the designers).

WR further writes that 

  most errors [...] can be easily spotted by visual inspection.  Every bit of
  [...] code should be subjected to a simple visual scan by a second party

.. Note:: Here simply we have peer review and *lightweight code review*.

Then

   test every logic path in the computer program at least once with some kind
   of numerical check [...] with controlled values of input.

.. Note:: And now we have unit testing and coverage measurement.

Step 5: Involve the customer
----------------------------

Let me quote again:

  Involve the customer in a format way so that he has committed himself at
  earlier points before final delivery. [...] The involvement should be formal,
  in-depth, and continuing.

.. Note:: And here again, we have points that are crucial to SCRUM, XP, or lean
   development.

Conclusion
----------

Far from being the opposite of lightweight methodologies, the waterfall model
is a precursor in many aspects.  Indeed, it recommends small staffing for the
establishment of a prototype as the very first step.  Feedback loops at every
stage, and precise interface definition.  Or involving the customer and the
user from the very beginning.  Presents that lightweight code reviews are the
best way to find simple errors.  Discusses testing and test coverage.  He also
insists that the design should be kept flexible.  WR actually introduces an
iterative process to software development.

In any case, the waterfall model as presented by WR is still of relevance
nearly 50 years after its introduction.  And it is not presented fairly by many
agile enthusiasts.

I am too young to know how this model was actually implemented but the early
literature from the agilist does not strongly criticise this model.

- "Lean Software Development: An Agile Toolkit", 1st edition (2003) Mary and
  Tom Poppendieck, mentions the model positively but comment that it was
  typically implemented more rigidly.
- The first edition of "Extreme Programming Explained: Embrace Change" does not
  mention the model at all.
- The original SCRUM paper from 1995 uses waterfall as extended by Boehm in his
  "A spiral model of software development and enhancement" (1988).  Schwaber
  and Sutherland further picture the waterfall methodology as a linear but
  complex process.

On the other hand, the model heavily criticized in this early literature
is CMMI.

I can only encourage developers, managers, or agile coaches to actually read
this article instead of using "waterfall" for name calling.

Finally, I do not think that using the "waterfall" model as the example of what
not to do is a very good motivation as a complete lack of process and quality
standards is equally damaging to software development as the excess of it.
Smaller organizations are further more likely to be facing difficulties of the
first kind so that presenting modern techniques as even lighter is simply
missing the point.

In the next article, I will quickly review "Software Requirements: Are They
Really A Problem?" that, according to Wikipedia, gave the waterfall model its
name.
