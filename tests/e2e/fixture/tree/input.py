from ingraph.aws import aws_cloudformation, aws_ec2, aws_iam


class Entrypoint:
    def __init__(self) -> None:
        foo = Foo()
        bar = Bar()


class Foo:
    def __init__(self) -> None:
        wch = aws_cloudformation.WaitConditionHandle()


class Bar:
    def __init__(self) -> None:
        baz = Baz()
        qux = Qux()


class Baz:
    def __init__(self) -> None:
        neti = aws_ec2.NetworkInterface(SubnetId="subnet_id")


class Qux:
    def __init__(self, group: str = "qux") -> None:
        grp = aws_iam.Group(GroupName=group)
