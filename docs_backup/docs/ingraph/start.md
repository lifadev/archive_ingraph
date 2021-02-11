---
id: start
title: Getting Started
---

## Installation

InGraph requires [Python 3.8][python] or newer. Feel free to use your
favorite tool or [pip][pip] to install the [`ingraph` package][pypi].

```
python3.8 -m pip install --upgrade --user ingraph
```

> Note that it will also install InGraph's dependencies, which might
> cause conflicts with other packages. You can also jump to the next
> section for a more streamlined experience.

Once the `ingraph` package installed, you can verify your installation
by running the `ig` command.

```
ig
```

You should see the following welcome screen.

```
Usage: ig [OPTIONS] COMMAND [ARGS]...

   ___        ____                 _
  |_ _|_ __  / ___|_ __ __ _ _ __ | |__
   | || '_ \| |  _| '__/ _` | '_ \| '_ \
   | || | | | |_| | | | (_| | |_) | | | |
  |___|_| |_|\____|_|  \__,_| .__/|_| |_|
  https://lifa.dev/ingraph  |_|    v0.2.1

  Infrastructure Graph DSL for AWS CloudFormation.

Options:
  -v, --version  Show the version and exit.
  -h, --help     Show this message and exit.

Commands:
  cfn  Translate infrastructure graphs to CloudFormation templates.
```

## Usage

For a better experience, we provide a [ready-to-use scaffold][scaffold]
you can download to get started quickly and to adapt it to your needs.

Start by unzipping it, and you should see the following content.

```
tree
.
├── COPYING
├── Makefile
├── poetry.lock
├── pyproject.toml
├── README.md
├── setup.cfg
└── src
    └── helloworld
        ├── example.py
        ├── handler.js
        └── __init__.py

2 directories, 9 files
```

It is a minimal Python package fine-tuned for [Poetry][poetry] (a
high-level tool that assists you in the Python packaging ceremony) and
[Visual Studio Code Remote Containers][remotedev] (a Docker powered
development environment).

> The usage of the [Visual Studio Code][vscode] editor is optional.
> If you decide to use another editor, you need, at least, to
> [install Poetry][poetrydoc] for the rest of the tutorial. Otherwise,
> feel free to adapt the `pyproject.toml` file to your tool of choice.

When you open the scaffold inside VS Code, a prompt asks you if you
want to continue developing in a container. Choose `Reopen in Container`
and wait for it to become ready.

The scaffold comes with an `example.py` file located in `src/helloworld`
that contains the following infrastructure description.

```python
from ingraph.aws import Asset, aws_iam, aws_lambda


class Example:
  arn: str

  def __init__(self) -> None:
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
      Handler="index.handle",
      Role=role.Arn,
      Runtime="nodejs12.x",
    )
    self.arn = function.Arn
```

It creates an AWS Lambda function that returns a "Hello, World!"
message. To provide the actual code of the Lambda function, we use an
asset to reference the content of the `handler.js` file located in
`src/helloworld`.

```js
exports.handle = async () => "Hello, World!";
```

We can use the InGraph CLI to translate from the InGraph DSL to the
AWS CloudFormation YAML template.

```
ig cfn -i helloworld.example -r Example -o build/example.yaml
```

> In `helloworld.example`, `helloworld` is the name of your package
> located in `src` and `example` is the name of your module located in
> `src/helloworld/example.py`.

The CLI creates a `build` folder with a file named `example.yaml` that
contains your AWS CloudFormation template.

```
tree build/
build/
└── example.yaml

0 directories, 1 file
```

```yaml
AWSTemplateFormatVersion: "2010-09-09"
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
      Handler: index.handle
      Role: !GetAtt RoleMW2CSPSW.Arn
      Runtime: nodejs12.x
Outputs:
  Arn:
    Value: !GetAtt FunctionODIWTV6H.Arn
```

Finally, you can use your tool of choice or the AWS CLI to deploy the
AWS CloudFormation template.

```
aws cloudformation deploy \
  --template-file build/example.yaml \
  --stack-name ingraph-helloworld \
  --capabilities CAPABILITY_IAM
```

Also, you can inspect the output of the freshly deployed stack to
retrieve the identifier of your function.

```
aws cloudformation describe-stacks \
  --stack-name ingraph-helloworld
```

```
{
  "Stacks": [
    {
      "Outputs": [
        {
          "OutputKey": "Arn",
          "OutputValue": "arn:aws:lambda:..."
        }
      ],
    }
  ]
}
```

To delete your stack, run the following command.

```
aws cloudformation delete-stack \
  --stack-name ingraph-helloworld
```

That's it. Welcome to InGraph!

[python]: https://www.python.org/downloads/
[pip]: https://pip.pypa.io/en/stable/
[pypi]: https://pypi.org/project/ingraph
[poetry]: https://python-poetry.org/
[poetrydoc]: https://python-poetry.org/docs/
[vscode]: https://code.visualstudio.com/
[remotedev]: https://code.visualstudio.com/docs/remote/containers
[scaffold]: https://github.com/lifadev/ingraph/releases/download/v0.2.1/ingraph-helloworld.zip
