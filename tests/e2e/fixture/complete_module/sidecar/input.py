from ingraph.aws import Asset, aws_iam, aws_lambda

from . import assets


class Entrypoint:
    asset_uri: str
    asset_url: str

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
        handler = Asset(name="handler.js", package=assets)
        func_plain = aws_lambda.Function(
            Code=aws_lambda.Function.Code(ZipFile=handler.text),
            Handler="index.handle",
            Role=role.Arn,
            Runtime="nodejs12.x",
        )
        archive = Asset(name="handler.js", package=assets, compress=True)
        func_zip = aws_lambda.Function(
            Code=aws_lambda.Function.Code(S3Bucket=archive.bucket, S3Key=archive.key),
            Handler="handler.handle",
            Role=role.Arn,
            Runtime="nodejs12.x",
            DependsOn=[func_plain, role],
        )
        self.asset_uri = archive.uri
        same_archive = Asset(name="handler.js", package=assets, compress=True)
        self.asset_url = same_archive.url
