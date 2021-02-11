---
id: overview
title: Overview
---

<p align="center"> 
  <img src="/img/ingraph/ingraph.png" alt="InGraph"/>
</p>

InGraph is an [open-source][github] and declarative, infrastructure
graph DSL for AWS CloudFormation. The key feature is the ability to
create composable infrastructure components while preserving the
rigorous semantic of the AWS CloudFormation language.

## Rationale

During his [talk][talk] at Serverlessconf New York City '19,
[Ben Kehoe][ben] laid the foundations of what should be the adequate
abstraction on top of AWS CloudFormation. Hereafter is an interpretation
of this talk that eventually resulted in the InGraph project.

### CloudFormation

Before going any further, it is crucial to define what exactly is AWS
CloudFormation. It is an [infrastructure graph](#infrastructure-graph)
management service of a two-prong nature. On the one hand, it is a
_language_ that allows, via the YAML _syntax_, to describe an
infrastructure graph. On the other, it is a deployment engine that
interprets the description, extracts the infrastructure graph, and then
creates and executes a plan to materialize that graph.

<p align="center"> 
  <img src="/img/ingraph/cloudformation.png" alt="CloudFormation"/>
</p>

With the above clarification, a deployment becomes the act of passing
some desired infrastructure graph to the interpreter, which in turn
takes care of materializing the resources in the cloud environment.

<p align="center"> 
  <img src="/img/ingraph/deployment.png" alt="Deployment"/>
</p>

### Problem

It's all about infrastructure graphs. On one side, there is the graph
one wants to see it exist, and on the other, the graph that actually
exists. Effectively managing infrastructure can be summed up in the
ability to compare these two graphs meaningfully and understand how the
same or different they are.

<p align="center"> 
  <img src="/img/ingraph/comparison.png" 
       alt="Comparing Graphs"/>
</p>

The fact of the matter is that the abstraction provided by
CloudFormation only ever allows manipulating raw resources at the lowest
level of the infrastructure graph. Moreover, it's not only tricky and
frustrating to use the YAML syntax, but there is also no way to package
up related resources, to reuse patterns, and in sum, to manipulate the
graph at a higher level of abstraction.

Hence, the problem is how to provide better syntax and high-level
abstractions without jeopardizing the ability to compare the two graphs.

### Solutions

#### External Abstraction

The easiest way of reaching a higher level of abstraction is by doing so
from the _outside_ of the graph definition language fed to the
interpreter (i.e., the CloudFormation template in YAML).

<p align="center"> 
  <img src="/img/ingraph/external_abstraction.png" 
       alt="External Abstraction"/>
</p>

Usually, a library created _inside_ a general-purpose programming
language can provide this kind of abstraction. One then has access to
high-level concepts to develop the infrastructure graph, and the tooling
takes care of compiling down into the graph definition language.

However, the initial problem of being able to compare the desired
infrastructure graph with the actual infrastructure graph now shifts to
the more complex, if not impossible, issue of being able to compare the
abstraction with the actual infrastructure graph.

It's worth noting that a more subtle downside also appears. This kind of
abstraction doesn't provide any learning path toward the graph
definition language. And while this faster development experience may
be appealing to mature CloudFormation practitioners, it also disconnects
newcomers from CloudFormation with the consequence of being helpless in
case a problem occurs outside the abstraction.

#### Native Abstraction

To transform external abstractions into a viable solution, one could
combine them with a similar approach at the cloud environment side.

<p align="center"> 
  <img src="/img/ingraph/native_abstraction.png" 
       alt="Native Abstraction"/>
</p>

In theory, it would solve the initial problem by making possible the
comparison of the two sides. However, in practice, it means that one
needs to find a way, given an actual infrastructure graph, to create a
high-level program that generates this graph while preserving syntactic
and semantic correctness with the initial program that generated the
desired infrastructure graph. It is equivalent to finding an automatic
and reliable reverse-engineering process.

#### Internal Abstraction

The truth of the matter is that the comparison of the desired graph with
the actual graph is only possible if these two graphs are expressible in
the same language. Hence, one should not provide abstractions from the
outside. Abstractions must happen within the graph definition language
itself so that they can be passed into the interpreter and persisted in
the actual infrastructure graph.

<p align="center"> 
  <img src="/img/ingraph/internal_abstraction.png" 
       alt="Internal Abstraction"/>
</p>

Nevertheless, this doesn't imply that one needs to stick with the
historical AWS CloudFormation YAML syntax. In effect, any language that
is equivalent to the graph definition language, [up to][upto]
[isomorphism][isomorphism], is acceptable.

Recall the [above definition](#cloudformation) of AWS CloudFormation,
whereby it's a service of a two-prong nature. The language apart, it is
a deployment engine whose main job is to extract the infrastructure
graph to create the deployment plan. This definition points out the fact
that the assembly language of the cloud is not the YAML template but the
deployment plan. As CloudFormation users have no access to the latter,
it prevents one from simply ditching the historical language and limits
alternatives to equivalent languages (i.e., compatible with the
interpreter).

In other words, one needs sort of a program that represents an
infrastructure graph in such a way that if presented to the interpreter,
hypothetically, this one could _parse_ the program, understand it and
extract the infrastructure graph.

## Proposal

For obvious reasons, InGraph chooses to engage in the internal
abstractions' path.

### Domain-Specific Language

The first part of the contract consists of reconsidering the AWS
CloudFormation language from a syntax perspective while paying special
attention to preserve the semantic.

To this end, InGraph started by carefully reconsidering all the quirks
and dirtiness of the original syntax and delineating the semantic of the
CloudFormation language. Some notions are essential to the problem
domain (e.g., the declarative nature of the syntax, the interactions
between the built-in functions, the typing system governing the
parameters, outputs, and resources, etc.). In contrast others are
low-level details that obfuscate the initial intent (e.g.,
`!Join [":", !Split ["-", !Ref param]]` is really
`param.replace(":", "-")`).

That eventually led to a domain-specific language. Its syntax is similar
in all aspects to that of modern programming languages. It comes with
conciseness, expressivity, and tooling, out-of-the-box. And, as it
operates _at_ the language level, it can strictly enforce the semantic.
Moreover, it has enough metadata to tie the very lines of the new syntax
to its counterpart translated into YAML, enabling rich syntactic
introspection capabilities on top of the semantic correctness.

### Domain-Specific Resource

The second part of the contract consists of providing high-level
abstractions without jeopardizing the ability to compare the desired and
the actual infrastructure graphs. It literally means that these
abstractions must unfold from low-level constructs of AWS
CloudFormation.

To this end, InGraph started by analyzing the native units of
composition used by CloudFormation. Resources are parametric and have a
well-defined API. They are also opaque, and one doesn't need to know
about their internals to use them effectively. For their part, stacks
convey the ability to package related resources, to reuse patterns, and
are the de facto unit of share.

That eventually led to a domain-specific resource. It is similar in all
aspects to both a CloudFormation stack and a CloudFormation resource.
It can carry parameters and outputs. It can be used in place of or along
with any other native CloudFormation resource. It is the very expression
of a [multiscale graph](#multiscale-graph) in which nodes are resources
or collection of resources (i.e., an infrastructure graph). Combined
with modules and assets, it offers an unprecedented way to capitalize on
knowledge within companies and across the community.

### Familiar and Effective

With a high-level interface on top of AWS CloudFormation that not only
preserves its underlying semantic but also literally unfolds from it,
InGraph aims to serve both ends of the AWS CloudFormation community, by:

- allowing professionals to leverage their existing knowledge and
  become more productive,
- offering newcomers an effective learning path toward AWS
  CloudFormation.

## Glossary

### Infrastructure

Infrastructure means deployed resources and collection of resources in
contrast with custom code running on the infrastructure (e.g., code
inside a Lambda function). Higher-level abstractions still represent
infrastructure (e.g., a constellation of microservices)

### Infrastructure as Code

Infrastructure as Code (IaC) means an artifact that represents this
infrastructure in contrast with manual configuration (e.g., clicking
through things in a console or doing stuff with a CLI).

### Graph

A graph represents a state of the world, either that exists, or that
should be. It is a declaration (the what, the data) and not an
instruction (the how, the code).

### Multiscale Graph

A multiscale graph is a graph in which the language is the same no
matter the level of zoom. A good analogy is a geographic map and its
graph of connectivity between areas. If one understands how to navigate
the plan, one understands it at all levels of zoom (country, city,
district, etc.).

### Infrastructure Graph

An infrastructure graph is a particular type of multiscale graph in
which nodes are resources or collection of resources. At the lowest
level, it can, for instance, represent an S3 bucket notifying a Lambda
function. At the highest level, it may represent [microservices at
Netflix][netflix].

[github]: https://github.com/lifadev/ingraph
[talk]: https://acloud.guru/series/serverlessconf-nyc-2019/view/yaml-better
[ben]: https://twitter.com/ben11kehoe
[netflix]: https://www.youtube.com/watch?v=-mL3zT1iIKw&feature=youtu.be&t=931
[upto]: https://en.wikipedia.org/wiki/Up_to
[isomorphism]: https://en.wikipedia.org/wiki/Isomorphism
