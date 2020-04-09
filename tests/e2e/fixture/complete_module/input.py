from ingraph.aws import Asset, aws_iam, aws_lambda

from complete_module.sidecar import assets, input

from . import submodule


class Entrypoint:
    asset_uri: str
    asset_url: str

    def __init__(self) -> None:
        sub = submodule.Entrypoint()
        handler = Asset(name="handler.js")
        func_plain = aws_lambda.Function(
            Code=aws_lambda.Function.Code(ZipFile=handler.text),
            Handler="index.handle",
            Role=sub.role_arn,
            Runtime="nodejs12.x",
        )
        archive = Asset(name="handler.js", compress=True)
        func_zip = aws_lambda.Function(
            Code=aws_lambda.Function.Code(S3Bucket=archive.bucket, S3Key=archive.key),
            Handler="handler.handle",
            Role=sub.role_arn,
            Runtime="nodejs12.x",
        )
        self.asset_uri = archive.uri
        same_archive = Asset(name="handler.js", compress=True)
        self.asset_url = same_archive.url
        side = input.Entrypoint()
        asset_side = Asset(name="handler.js", package=assets)
        func_side = aws_lambda.Function(
            Code=aws_lambda.Function.Code(
                ZipFile=asset_side.text.replace("sidecar", "inside")
            ),
            Handler="index.handle",
            Role=sub.role_arn,
            Runtime="nodejs12.x",
        )
