from ingraph import aws
from ingraph.aws import aws_cloudformation


class Entrypoint:
    account_id: str
    availability_zone: str
    notification_arn: str
    partition: str
    region: str
    stack_id: str
    stack_name: str
    url_suffix: str

    def __init__(self) -> None:
        wch = aws_cloudformation.WaitConditionHandle()
        self.account_id = aws.ACCOUNT_ID
        self.availability_zone = aws.AVAILABILITY_ZONES[0]
        self.notification_arn = aws.NOTIFICATION_ARNS[0]
        self.partition = aws.PARTITION
        self.region = aws.REGION
        self.stack_id = aws.STACK_ID
        self.stack_name = aws.STACK_NAME
        self.url_suffix = aws.URL_SUFFIX
