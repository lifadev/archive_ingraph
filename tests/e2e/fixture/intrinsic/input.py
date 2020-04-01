from typing import List

from ingraph import aws
from ingraph.aws import aws_cloudformation, aws_iam


class Entrypoint:
    attr: str
    join0: str
    join1: str
    join2: str
    join3: str
    join4: str
    ref: str
    select_int: int
    select_str: str
    split: str
    sub0: str
    sub1: str
    sub2: str
    base64: str
    cidr: str
    static: str

    def __init__(self, ps: str, pli: List[int], pls: List[str]) -> None:
        wch = aws_cloudformation.WaitConditionHandle()
        grp = aws_iam.Group()

        index = 0
        self.attr = grp.Arn
        self.join0 = wch.Ref + grp.Arn + wch.Ref
        self.join1 = wch.Ref + grp.Arn + "foo"
        self.join2 = "-".join([wch.Ref, grp.Arn])
        self.join3 = grp.Arn.replace(":", "-")
        self.join4 = ",".join(pls) + wch.Ref
        self.ref = wch.Ref
        self.select_int = pli[0]
        self.select_str = aws.AVAILABILITY_ZONES[index]
        self.split = grp.Arn.split(":")[0]
        self.sub0 = f"{wch.Ref} {grp.Arn}"
        self.sub1 = f"{wch.Ref + grp.Arn}"
        self.sub2 = "{} {} {}".format(wch.Ref, grp.Arn, ps)
        self.base64 = aws.b64encode("foo")
        self.cidr = aws.cidr(block=ps, count=4, bits=2)[0]
        self.static = ["foo", "bar"][1]
