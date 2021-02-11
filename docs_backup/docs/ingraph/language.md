---
id: language
title: Language
---

InGraph steps away from the YAML syntax to supersede its limitations
but preserves the benefits of its declarative programming model. It
uses a very basic flavor of Python for two reasons:

- Python is known to have one of the most beginner-friendly syntaxes.
- Python comes with tons of tooling off the shelf to help developers.

Hereafter is an example of what you can write in InGraph.

```python
from ingraph.aws import Asset, aws_iam, aws_lambda

class HelloWorld:
  func_arn: str

  def __init__(self, memory_size: int = 128):
    role = aws_iam.Role(
      AssumeRolePolicyDocument={
        "Version": "2012-10-17",
        "Statement": {
          "Effect": "Allow",
          "Principal": {"Service": "lambda.amazonaws.com"},
          "Action": "sts:AssumeRole",
        },
      },
      ManagedPolicyArns=[
        "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
      ],
    )
    handler = Asset(name="handler.js")
    function = aws_lambda.Function(
      Code=aws_lambda.Function.Code(ZipFile=handler.text),
      Role=role.Arn,
      MemorySize=memory_size,
      Handler="index.handle",
      Runtime="nodejs12.x",
    )
    self.func_arn = function.Arn
```

If you come from the imperative world of template generators, one of
the most surprising aspects of InGraph is the fact that the code is not
a program but the actual data. You don't have to execute it to produce
the template because the syntax already encodes all the information. You
indeed use declarations to describe what is the infrastructure graph
instead of instructions to convey how to build it.

Take a moment to compare it with the translation into the YAML syntax.

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Parameters:
  MemorySize:
    Type: Number
    Default: 128
Resources:
  RoleMW2CSPSW:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          Effect: Allow
          Principal:
            Service: lambda.amazonaws.com
          Action: sts:AssumeRole
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
  FunctionODIWTV6H:
    Type: AWS::Lambda::Function
    Properties:
      Code:
        ZipFile: |
          exports.handle = async () => "Hello, World!";
      Role: !GetAtt RoleMW2CSPSW.Arn
      Handler: index.handle
      Runtime: nodejs12.x
      MemorySize: !Ref MemorySize
Outputs:
  FuncArn:
    Value: !GetAtt FunctionODIWTV6H.Arn
```

As you can see, the DSL is very similar to its YAML counterpart, so that
if you already know CloudFormation, then you also know InGraph, and vice
versa. Nevertheless, InGraph has more than a simple syntactic sugar to
offer, so let's deep dive into its other features.

### Resource Definitions

A resource definition is the most fundamental concept in InGraph. On the
one hand, it is akin to the notion of a stack in CloudFormation and
seamlessly translates into its YAML counterpart. On the other, it is the
unit of composability in the infrastructure graph. It allows grouping
together related sub-definitions, whether it be low-level AWS
CloudFormation definitions (like a role or a function), or other
high-level definitions.

Syntactically, a resource definition is a Python class. However, don't
be fooled by the notation; it's only about a handy syntax. You are not
allowed play around the general concept of classes in Python. Also, as
one would expect with a regular CloudFormation stack, InGraph classes
can have parameters, attributes, and a body of one or several other
resources.

#### Parameters

From a Python programmer's point of view, a class naturally comes with a
constructor called `__init__`, where its signature specifies the
parameters and their types.

```python
from typing import List

class MyResource:

  def __init__(
    self,
    foo: int = 42,
    bar: str = 'foo',
    foo_list: List[int] = [4, 2],
    bar_list: List[str] = ["f", "o", "o"],
  ):
    ...
```

By now, you should be used to it; there are some restrictions in
comparison with regular Python:

- You can only have one `__init__` method inside a class. Other methods
  are not allowed.

  ```python
  def __init__      # OK
  def anything_else # ERROR
  ```

- The first parameter must always be there and named `self`. It is the
  current instance of the class.

  ```python
  def __init__(self) # OK
  def __init__()     # ERROR
  ```

- If there is no other parameter than `self`, then the method must have
  `None` as its return type to satisfy Mypy.

  ```python
  def __init__(self) -> None: ...
  def __init__(self, foo: int): ...
  ```

- Each parameter must have a type among `int`, `float`, `str`,
  `List[int]`, `List[float]`, or `List[str]` and may have a static
  default value.

  ```python
  def __init__(self, p1: int, p2: List[str] = ["foo", "bar"]): ... # OK
  def __init__(self, p1, p2): ...                                  # ERROR
  ```

InGraph parameters are the exact equivalent of AWS CloudFormation
parameters.

```python
def __init__(self, p1: int, p2: List[str] = ["foo", "bar"]): ...
```

```yaml
Parameters:
  P1:
    Type: Number
  P2:
    Type: CommaDelimitedList
    Default: foo,bar
```

#### Attributes

A resource definition may expose some class attributes as its public
API.

```python
class MyResource:
  foo: int
  bar: str

  def __init__(self) -> None:
    self.foo = 42
    self.bar = "bar
```

- All attributes are immutable and must be initialized inside the
  `__init__` method.

  ```python
  foo: int
  def __init__(self): ... # ERROR

  resc = MyResource()
  resc.foo = 42           # ERROR
  ```

- Each attribute must have a type among `int`, `float`, or `str` and
  cannot have a default value.

  ```python
  foo: int         # OK
  bar: str = "bar" # ERROR
  ```

InGraph attributes are the exact equivalent of AWS CloudFormation
outputs.

```python
foo: int
bar: str

def __init__(self) -> None:
  self.foo = 42
  self.bar = "bar"
```

```yaml
Outputs:
  Foo:
    Value: 42
  Bar:
    Value: bar
```

#### Instantiation

Resource instantiation is the de facto way to inform InGraph that a
given resource must be part of the infrastructure graph.

```python
from ingraph.aws import aws_lambda

class MyResource:
  def __init__(self) -> None:
    func = aws_lambda.Function(Handler="index.handle", ...)
```

- You can instantiate both low-level AWS CloudFormation resources as
  well as other high-level resources.

  ```python
  from ingraph.aws import aws_lambda
  from company.team import feature

  func = aws_lambda.Function(Handler="index.handle", ...)
  foo = feature(bar="baz", qux=42)
  ```

- Each instance must be assigned to a variable, which name is the name
  of the resource in the infrastructure graph.

  ```python
  foo = Foo(...) # OK
  Foo(...)       # ERROR
  ```

- Each instance is immutable, and within the same scope, two instances
  cannot have the same name (i.e., be assigned to the same variable).

  ```python
  foo = Foo()
  foo = Bar() # ERROR
  ```

- Instantiation parameters must be given as static keywords, and list or
  dictionary expansions are not allowed.

  ```python
  foo = Foo(bar="baz", qux=42)       # OK
  foo = Foo("baz", 42)               # ERROR
  foo = Foo(*some_list, **some_dict) # ERROR
  ```

### Modules and Packages

InGraph relies on the modularisation mechanism provided by Python. It
enables you to split complex infrastructure configurations into several
files for easier maintenance. These files can be versioned, published,
and shared via popular tools offered by the Python ecosystem, such as
PyPI (Python Package Index) and pip (the package installer for Python).

`.py` files constitute modules, and a collection of related modules can
be grouped into a package, as soon as the directory contains an
`__init__.py` file. For instance, here's a possible structure for an
infrastructure package:

```
hello_world/           Top-level package
    __init__.py        Declare the hello_world package
    apis/              Subpackage for apis
        __init__.py
        foo.py
        bar.py
        ...
    buckets/           Subpackage for buckets
        __init__.py
        baz.py
        qux.py
        ...
```

As discussed earlier, InGraph operates at the language level and is not
a framework inside Python. In that respect, most of the well-known
concepts of Python are not available at all, and features are stripped
to the strict minimum needed to express the semantic of the
CloudFormation language.

Hence, top-level statements inside a module are limited:

- You can have import statements.

  ```python
  from hello_world.apis import foo
  ```

- You can have resource definitions.

  ```python
  class MyApi:
      ...
  ```

### Import Statements

InGraph hooks deep into the Python import machinery and conscientiously
verifies each imported module to make sure that the semantic of
CloudFormation is preserved.

The syntax of the import statements is slightly more restricted than
regular Python:

- You can only perform relative imports. Absolute imports are not
  allowed.

  ```python
  from foo import bar # OK
  import foo          # ERROR
  ```

- You can only import public named symbols. Star or private symbols
  imports are not allowed.

  ```python
  from foo import *    # ERROR
  from foo import _bar # ERROR
  ```

- You can alias imports as soon as the alias doesn't start with an
  underscore.

  ```python
  from foo import bar as baz  # OK
  from foo import bar as _baz # ERROR
  ```

Remember that Python is a general-purpose programming language, and its
semantic is way too broad for CloudFormation. Therefore, only a tiny
fraction of its modules is of interest.

- You can import the InGraph standard library for AWS

  ```python
  from ingraph import aws
  from ingraph.aws import aws_lambda
  ```

- You can import relevant symbols from the Python built-in `typing`
  module.

  ```python
  from typing import List          # OK
  from typing import Generics, ... # ERROR
  ```

- You can import any other module written with the InGraph DSL.

  ```python
  from company.team import feature
  from community import awesomeness
  ```

### Assets

With assets, InGraph offers a simple way to embed resources' external
dependencies. For instance, it allows grouping together an AWS Lambda
function with its handler's source code or binary.

- You can reference the textual content of an asset.

  ```python
  from ingraph.aws import Asset, aws_lambda

  handler = Asset(name="handler.js")
  function = aws_lambda.Function(
      Code=aws_lambda.Function.Code(ZipFile=handler.text),
      ...
  )
  ```

- You can reference your assets (files or folders) as a deterministic
  zip archive.

  ```python
  from ingraph.aws import Asset, aws_lambda

  archive = Asset(name="handler.js", compress=True)
  function = aws_lambda.Function(
      Code=aws_lambda.Function.Code(
          S3Bucket=archive.bucket,
          S3Key=archive.key,
      ),
      ...
  )
  ```

Moreover, when one consumes shared components that embed assets (either
privately within a company or publicly from the community), one has the
same experience as if he was consuming a local component. Simply install
the component, and InGraph takes care of the rest.

```python
# pip install awesomeness
from awesomeness import Function

function = Function(...) # It may contain embeded assets
```

Some restrictions apply though:

- Each asset must be assigned to a variable.

  ```python
  archive = Asset(name="handler.js", compress=True)
  ```

- The name of the asset is relative to the current package or the one
  given as the parameter. It cannot contain any path related part.

  ```python
  handler = Asset(name="handler.js")                    # OK

  from . import handlers
  handler = Asset(name="handler.js", package=handlers)  # OK

  handlers = Asset(name="./handlers/handler.js")        # ERROR
  ```

- The folder containing the asset must also contain an `__init__.py`
  file.

  ```
  hello_world/           Top-level package
      __init__.py        Declare the hello_world package
      handlers/          Subpackage for assets
          __init__.py
          handler.js
  ```

### Typing System

A syntax, alone, would neither be sufficient to unleash all the benefits
of the InGraph DSL nor to rigorously guarantee the semantic of the AWS
CloudFormation language. Hence, InGraph comes with a powerful
type system that seamlessly integrates with Python editors plugins and
static type checkers like Mypy. Among its benefits, you're given
autocompletion and live error reporting from within your editor along
with new and higher-level operations that still preserve the semantic.

InGraph is structured around five basic types; booleans, numbers,
strings, lists, and maps. Note however, that this is where things
diverge the most from regular Python. The set of available operations on
each type and their very expression is limited to what is allowed by
CloudFormation. You cannot overstep the strict frame imposed by this
latter.

#### Booleans

##### Values

- In a plain form.
  ```python
  True
  False
  ```
- As a reference to a native CloudFormation resource's attribute.
  ```python
  dev = aws_iot1click.Device(...)
  dev.Enabled
  ```

> Neither parameters nor attributes of user-defined resources can be of
> type boolean.

##### Operations

:::important NOT YET IMPLEMENTED
There is no operation available on booleans, and more specifically,
there is no conditional statement in the InGraph DSL.
:::

#### Numbers

##### Values

- In plain form.
  ```python
  42  # integer
  4.2 # float
  ```
- As a reference to a native CloudFormation resource's attribute.
  ```python
  cr = aws_ec2.CapacityReservation(...)
  cr.AvailableInstanceCount
  ```
- As a parameter specified in the constructor of a resource definition.
  ```python
  class MyResource:
    def __init__(self, foo: int, bar: float): ...
  ```
- As an attribute specified in a resource definition.
  ```python
  class MyResource:
    foo: int
    bar: float
  ```

##### Operations

There is no operation available on numbers, and more specifically, you
cannot add or subtract two numbers or compare them together.

#### Strings

##### Values

- In a plain form.
  ```python
  "lorem ipsum"
  ```
- As a reference to a native CloudFormation resource's attribute.
  ```python
  eip = aws_ec2.EIP(...)
  eip.AllocationId
  ```
- As a parameter specified in the constructor of a resource definition.
  ```python
  class MyResource:
    def __init__(self, foo: str): ...
  ```
- As an attribute specified in a resource definition.
  ```python
  class MyResource:
    foo: str
  ```

##### Operations

- Concatenation via the `+` operator.

  ```python
  "foo" + bar
  ```

- Concatenation via the `.join` method.

  ```python
  "-".join(["foo", bar])
  ```

  > The separator `"-"` involved in the join operation must be a plain
  > string. More specifically, you cannot use any parameter or attribute
  > as the separator.

- Formatting via the `.format` method.

  ```python
  "{} {}".format("foo", bar)       # expands to "foo bar"
  "{0} {0} {1}".format("foo", bar) # expands to "foo foo bar"
  ```

  > The format specifications `"{} {}"` or `"{0} {0} {1}"` involved in
  > the format operation must be plain strings. More specifically, you
  > cannot use any parameter or attribute as the format specification.

- Formatting via Python f-strings.

  ```python
  f"{foo} {bar}"  # expands to "foo bar"
  ```

- Replacement of a substring by another.

  ```python
  foo.replace("old", "new")
  ```

  > The `"old"` and `"new"` operands involved in the replace operation
  > must be plain strings. More specifically, you cannot use any
  > parameter or attribute as the operands.

- Splitting a string into a list of substrings.

  ```python
  foo.split(":")
  ```

  > The separator `":"` involved in the split operation must be a plain
  > string. More specifically, you cannot use any parameter or attribute
  > as the separator.

#### Lists

##### Values

There are three types of lists in InGraph

1. Lists of primitive values (i.e., list of booleans, numbers, and
   strings).

   - In a plain form.
     ```python
     [4, 2]
     ["foo", "bar"]
     ```
   - As references to other variables or attributes.
     ```python
     [foo, bar, baz.qux]
     ```
   - As a reference to a native CloudFormation resource's attribute.
     ```python
     ni = aws_ec2.NetworkInterface(...)
     ni.SecondaryPrivateIpAddresses
     ```
   - As a parameter specified in the constructor of a resource
     definition.
     ```python
     class MyResource:
       def __init__(self, foo: List[str], bar: List[int]): ...
     ```

   > - Attributes of user-defined resources cannot be be of type list of
   >   primitive values.
   > - Neither parameters nor attributes of user-defined resources can
   >   be of type list of booleans.

2. Lists of heterogeneous values (i.e., lists of any combination of
   primitive values and other lists or maps).

   - In a plain form.
     ```python
     [42, "foo", [True, {"bar": "baz"}]]
     ```
   - As references to other variables or attributes.
     ```python
     [foo, [bar, baz.qux]]
     ```

   > Neither parameters nor attributes can be of type list of
   > heterogeneous values.

3. Lists of native resource instances.
   - It can only contain instances of native CloudFormation resources.
   - It can only be used as the `DependsOn` argument of another native
     CloudFormation resource.
     ```python
     igw = aws_ec2.VPCGatewayAttachment(...)
     instance = aws_ec2.Instance(..., DependsOn=[igw])
     ```

##### Operations

There is no operation available on lists of heterogeneous values and
lists of native resource instances, and more specifically, you cannot
reference a particular element of these lists.

- Referencing an element on lists of primitive values.

  ```python
  foo[42]
  ```

  > The index `42` involved in the operation must be a plain number.
  > More specifically, you cannot use any parameter or attribute as the
  > index.

#### Maps

##### Values

- In a plain form.
  ```python
  {"foo": "bar"}
  ```
- As references to other variables or attributes.
  ```python
  {"foo": bar, "bar": baz.qux}
  ```

> - Maps keys must be plain strings. More specifically, you cannot use
>   any parameter or attribute as a map's key.
> - Neither parameters nor attributes of user-defined resources can be
>   of type map.

##### Operations

There is no operation available on maps, and more specifically, you
cannot reference a particular key of a map.

### Immutability

InGraph promotes a purely declarative view of the infrastructure graph
so that syntactical correctness implies semantical correctness, as much
as possible. With this approach, once you've managed to express what
you wanted to express, it will almost certainly do what you've intended
to do.

Naturally, mutations have no place in a declarative world. Therefore,
while InGraph allows you to leverage the expressivity, conciseness, and
factorization power of variables, it also prevents you from mutating
anything. Inside InGraph, everything is immutable.

- You cannot reassign a parameter.

  ```python
  def __init__(self, foo: int):
    foo = 42     # ERROR
  ```

- You cannot reassign a variable.

  ```python
  def __init__(self) -> None:
    foo = 42
    foo = 24     # ERROR
  ```

- You cannot mutate a resource attribute.

  ```python
  foo = Foo(...)
  foo.bar = 42   # ERROR
  ```

- You cannot mutate an array or a dictionary.

  ```python
  foo = ["bar", "baz"]
  foo[0] = "qux" # ERROR
  ```

If you come from the imperative world of template generators, this
aspect of InGraph will most certainly challenge you at the beginning.
Hang in there; it's worth it.
