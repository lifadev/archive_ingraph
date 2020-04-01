from typing import List

from ingraph.aws import aws_cloudformation


class Entrypoint:
    def __init__(
        self,
        i: int,
        s: str,
        li: List[int],
        ls: List[str],
        id: int = 42,
        sd: str = "foo",
        lid: List[int] = [4, 2],
        lsd: List[str] = ["f", "o", "o"],
    ):
        wch = aws_cloudformation.WaitConditionHandle()
