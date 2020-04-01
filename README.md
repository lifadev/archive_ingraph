<p align="center"> 
  <img src="https://lifa.dev/img/ingraph/ingraph.png" alt="InGraph"/>
</p>

# [InGraph][website] &middot; [![Version][badge-version]][version] [![License][badge-license]][license]

> InGraph ain't template generator :stuck_out_tongue_winking_eye:

InGraph is a Declarative Infrastructure Graph DSL for AWS
CloudFormation.

-   **Declarative**: Never again abstract away from CloudFormation.
    Simply declare your infrastructure components, without the hassle of
    YAML, and preserve the strict semantic of the AWS CloudFormation
    language. Veterans, build on top of your knowledge. Newbies, learn
    CloudFormation effectively.

-   **Composable**: Create encapsulated components with their assets and
    dependencies, then share or compose them to build more complex
    infrastructures. From simple nodes to your whole graph, everything
    is a deployable infrastructure unit.

-   **Integrated**: Leverage the evergrowing Python ecosystem. Benefit
    from static type checking, take advantage of autocompletion in your
    editor, or even consume open infrastructure components via the
    Python Package Index, among others.

[Learn how to use InGraph in your own project][overview].

## Installation

InGraph requires [Python 3.8][python] or newer. Feel free to use your
favorite tool or [`pip`][pip] to install the
[`ingraph` package][version].

```
python3.8 -m pip install --user ingraph
```

Verify your installation by invoking the `ig` command. You should see
a welcome screen.

## Example

We have several examples on the [website][website]. Here is the first
one to whet your appetite.

```
ig cfn -i example.py -r HelloWorld -o example.yaml
```

![InGraph Example](https://lifa.dev/img/ingraph/example.png)

This example creates a simple AWS Lambda function that returns a
"Hello, World!" message.

You'll notice that CloudFormation parameters, along with their types and
default values are simple constructor parameters, or that CloudFormation
outputs are class attributes, or even that CloudFormation resource names
are derived from variable names. It's only a taste of
[what is in store][overview] for you.

## Contributing

The primary purpose of this project is to continue to evolve the core of
InGraph. We are grateful to the community for any contribution. You may,
for example, proof-read the documentation, submit bugs and fixes,
provide improvements, discuss new axes of evolution, or spread the word
around you.

## Thanks

We want to thank and express our gratitude to [Ben Kehoe][ben]. Without
his guidance and support, this project wouldn't have been possible.

## License

Unless otherwise stated, the source code of the project is released
under the [GNU Affero General Public License Version 3][agplv3]. Please
note, however, that all public interfaces subject to be embedded within
the source code of your infrastructure are released under the [Apache
License Version 2][apachev2]. Refer to the header of each file or to the
LICENSE file present in the parent directory where appropriate.

[badge-version]: https://img.shields.io/badge/version-0.1.0-blue?style=flat-square
[version]: https://pypi.org/project/ingraph/0.1.0/
[badge-license]: https://img.shields.io/badge/license-AGPL3%2FApache2-blue?style=flat-square
[license]: https://github.com/lifadev/ingraph#license
[website]: https://lifa.dev/ingraph
[agplv3]: https://www.gnu.org/licenses/agpl-3.0.txt
[apachev2]: http://www.apache.org/licenses/LICENSE-2.0.txt
[overview]: https://lifa.dev/docs/ingraph/overview
[example]: https://raw.githubusercontent.com/lifadev/ingraph/master/example.png
[python]: https://www.python.org/downloads/
[pip]: https://pip.pypa.io/en/stable/
[ben]: https://twitter.com/ben11kehoe
