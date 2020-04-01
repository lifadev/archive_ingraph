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
