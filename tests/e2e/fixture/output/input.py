from ingraph.aws import aws_cloudformation


class Entrypoint:
    oi: int
    os: str

    def __init__(self) -> None:
        wch = aws_cloudformation.WaitConditionHandle()
        self.oi = -42
        self.os = "foo"
