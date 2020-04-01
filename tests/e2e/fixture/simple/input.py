from ingraph.aws import aws_cloudformation


class Entrypoint:
    def __init__(self) -> None:
        wch = aws_cloudformation.WaitConditionHandle()
