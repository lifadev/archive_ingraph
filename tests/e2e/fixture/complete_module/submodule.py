from ingraph.aws import aws_iam


class Entrypoint:
    """A Multiline
    Entrypoint documentation"""

    role_arn: str

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
        self.role_arn = role.Arn
