---
title: Introducing InGraph
tags:
    [
        aws,
        cloudformation,
        domain-specific-language,
        infrastructure-as-code,
        infrastructure-graph,
    ]
author: Farzad Senart
author_title: Co-Chief Frog Officer at lifa.dev
author_url: https://twitter.com/fsenart
author_image_url: https://graph.facebook.com/749433322/picture/?height=200&width=200
---

Lionel and I are pleased to announce the open-source release of our
abstraction on top of AWS CloudFormation: InGraph!

<!--truncate-->

And before leaping to any conclusions, we solemnly promise it is not yet
another template generator. Put simply, InGraph is:

**CloudFormation like it is 2020. A familiar syntax, editor support,
modularity and composability, and way more while rigorously following
the semantic of CloudFormation.**

If you’re a CloudFormation aficionado, you’ll feel immediately
comfortable and sense a free upgrade. At first sight, InGraph is an
updated syntax that still tastes CloudFormation but also deeply
integrates with the tooling you’re used to (e.g., auto-completion,
typing, packaging, etc.).

If you’re new to the world of Infrastructure as Code on AWS, you’ll find
a companion who will teach you the ins and outs of CloudFormation while
assisting you in your journey. InGraph is CloudFormation stripped of its
quirks and dirtiness. It is similar in all aspects to modern programming
languages but also makes a point of not disconnecting from
CloudFormation.

Sounds like a fit? Continue reading!

# The Challenge of Infrastructure Management

If you haven’t yet watch [Ben Kehoe][twitter-ben]'s [talk][talk-ben] at
Serverlessconf New York City ’19, stop here, do so and come back only
after. It’s a foundational talk that makes a strong statement about what
should be the right abstraction on top of AWS CloudFormation. By the
way, it is also the backbone of InGraph.

Using the AWS CloudFormation language is painful. To be convinced, we
only need to look at the various attempts made both by AWS itself and
the broader open-source community to overcome the difficulties and
frustration. In fact, the pain is so deep that all the alternatives
ended up, invariably, disconnecting from it or ignoring it altogether.
We all do agree with the problem. However, let’s take a closer look at
the path chosen toward the solution.

There is, at least, a cognitive bias accentuated by the fact that, as
software engineers, we have power. We can resolve problems with more and
more elaborated concepts and tools. So why stick with something that
annoys us? Let’s say that this question is too philosophical for this
post.

Moreover, and Ben’s talk brings this up, there is also a misconception,
firmly anchored in the collective sub-consciousness, that CloudFormation
is the assembly language of the cloud. And this very statement is enough
to comfort us in need of high-level constructs that have nothing to do
with the low-level CloudFormation language. After all, this is precisely
what we’ve been used to do with the assembly languages of processors.

> The AWS CloudFormation language is not the assembly language of the
> cloud.

To better understand these misunderstandings, let’s define what exactly
is AWS CloudFormation. It is an infrastructure graph management service
of a two-prong nature. On the one hand, it is a _language_ that allows,
via the YAML syntax, to describe an infrastructure graph. On the other,
it is a deployment engine that interprets the description, extracts the
infrastructure graph, and then creates and executes a plan to
materialize that graph.

<p align="center"> 
  <img src="/img/blog/2020-03-31-introducing-ingraph/cloudformation.png" 
       alt="CloudFormation"/>
</p>

It turns out that the actual assembly language is not the description
but the deployment plan. And we, as CloudFormation users, don’t have
access to it. What does that mean is we cannot simply disconnect from or
ignore the CloudFormation language. We have to play the game of the
interpreter. Because, in case of any problems, our understanding of the
CloudFormation language is our only way to salvation.

> Learning the AWS CloudFormation language is a necessity.

Finally, the desire to get rid of the CloudFormation language is also
incentivized by the legitimate willingness to manipulate infrastructure
graphs at a higher level (e.g., packaging up related resources, reusing
patterns, etc.). And general-purpose programming languages and
frameworks _inside_ them seem perfect candidates. However, they come at
the expense of the comparability of the desired and the actual graph.

<p align="center"> 
  <img src="/img/blog/2020-03-31-introducing-ingraph/comparison.png" 
       alt="Comparing Graphs"/>
</p>

Indeed, as these abstractions occur _outside_ the AWS CloudFormation
language, they not only disconnect you from the input of the interpreter
(i.e., the desired graph) but from its output as well (i.e., the actual
graph of deployed resources on the cloud environment). This points out a
fundamental problem as our capacity to effectively manage
infrastructures is closely related to our ability to compare these two
graphs meaningfully and understand how the same or different they are.

<p align="center"> 
  <img src="/img/blog/2020-03-31-introducing-ingraph/external_abstraction.png"
       alt="External Abstraction"/>
</p>

# Toward Better Infrastructure Management

As outlined earlier, infrastructure management on AWS is not a new
challenge. Tools like AWS Serverless Application Model (SAM), AWS Cloud
Development Kit (CDK), and AWS Serverless Application Repository (SAR),
to name but a few, are already helping many organizations. When we
undertook to create a new abstraction on top of AWS CloudFormation, we
had two main goals:

1. Have a familiar language that scrupulously respects the semantic of
   AWS CloudFormation.

2. Have a high-level abstraction that unfolds from AWS CloudFormation
   low-level constructs (e.g., resources, stacks, parameters, outputs,
   etc.).

Meet [InGraph][ingraph]!

# InGraph

InGraph is an [open-source][github] and declarative, infrastructure
graph DSL for AWS CloudFormation.

InGraph appears as a subset of Python and, therefore, seamlessly
integrates with its existing ecosystem of tooling. For instance, you're
given autocompletion, type checking, and live support from within your
editor, out-of-the-box. You can also use the Python Package Index (PyPI)
along with pip to share and consume available infrastructure patterns.

<p align="center"> 
  <img src="/img/blog/2020-03-31-introducing-ingraph/autocompletion.png"
       alt="Autocompletion"/>
</p>

<p align="center"> 
  <img src="/img/blog/2020-03-31-introducing-ingraph/assistance.png"
       alt="Error Reporting"/>
</p>

Unlike other tools that run _inside_ general-purpose languages, InGraph
operates _at_ the language level. It doesn't execute the code you write
to produce a CloudFormation template. The syntax already encodes all the
information. This also enables the ability to compare the InGraph
description with its YAML counterpart. You're no more disconnected from
the AWS CloudFormation language. You actually evolve in the same
language but with an updated syntax.

<p align="center"> 
  <a href="/img/ingraph/example.png">
  <img src="/img/ingraph/example.png"
       alt="Example"/>
</a>
</p>

InGraph steps away from the YAML syntax to supersede its limitations but
preserves the benefits of its declarative programming model. Also, under
the hood, InGraph comes with a custom interpretation engine that
rigorously enforces the semantic of the AWS CloudFormation language.

> InGraph uses declarations to describe what is the infrastructure graph
> instead of instructions to convey how to build it.

Naturally, mutations have no place in a declarative world. So, while
InGraph allows you to use variables, it also prevents you from mutating
anything. Within InGraph, everything is immutable.

InGraph highlights the typing system of AWS CloudFormation by providing
five primary types: _booleans_, _numbers_, _strings_, _lists_, and
_maps_. The engine carefully verifies that you don't overstep the frame
imposed by the AWS CloudFormation language. For instance, you are not
allowed to perform numeric operations or to access an item inside a list
with an index that is not known statically. In contrast, where semantic
correctness is not at stake, InGraph frees you from low-level details
that parasitize your intent (e.g., `param.replace(":", "-")` is
translated to `!Join [":", !Split ["-", !Ref param]]`).

Last but not least, InGraph unifies the concepts of CloudFormation
resources and CloudFormation stacks into a new domain-specific resource.
This new kind of resource can carry parameters and outputs, and be used
in place of or along with any other native CloudFormation resource. It
is the very expression of a [multiscale graph][graph] in which nodes are
resources or collection of resources. It also constitutes the primary
unit of composability and share and offers an unprecedented way to
capitalize on knowledge within companies and across the community.

> InGraph unifies the resources and stacks of AWS CloudFormation into
> nodes of a multiscale graph.

<p align="center"> 
  <img src="/img/ingraph/ingraph.png"
       alt="InGraph"/>
</p>

# Getting Started

InGraph is available now on [GitHub][github]. You can
[try it out][start] using Visual Studio Code Remote Containers.
Detailed information about the underlying reasoning, setup, and usage
are also available in [our documentation][ingraph].

# Contributing

InGraph is currently in [MVP][mvp] status. [Lionel][twitter-lionel] and
[I][twitter-farzad] are proud of what we've built and excited to share
it with the community. We hope you find it as useful as we do. InGraph
only has a small portion of features we intend to build, and we are
actively seeking feedback. If you have any ideas, suggestions, or
issues, feel free to reach us on [Twitter][twitter-lifa] or
[GitHub][github].

> **We can't finish this post without a big thanks to Ben Kehoe. His
> theories served as the foundations of InGraph, his guidance and
> support made it possible.**

[twitter-ben]: https://twitter.com/ben11kehoe
[talk-ben]: https://acloud.guru/series/serverlessconf-nyc-2019/view/yaml-better
[ingraph]: /ingraph
[github]: https://github.com/lifadev/ingraph
[graph]: /docs/ingraph/overview#multiscale-graph
[start]: /docs/ingraph/start#usage
[mvp]: https://en.wikipedia.org/wiki/Minimum_viable_product
[twitter-lionel]: https://twitter.com/lion3ls
[twitter-farzad]: https://twitter.com/fsenart
[twitter-lifa]: https://twitter.com/lifadev
