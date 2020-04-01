# Copyright 2020 Farzad Senart and Lionel Suss. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from pathlib import Path

import jinja2

from ingraph.engine.importer import aws_hook, import_module

# https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html
# JSON.stringify($$(".highlights a").map(d => ({
#     [d.pathname.split('/').slice(-1)[0].split(".")[0].toLowerCase()]: d.text
# })).reduce((a, c) => Object.assign(a, c)))

INFO = {
    "aws_accessanalyzer": "AccessAnalyzer",
    "aws_acmpca": "ACMPCA",
    "alexa_ask": "ASK",
    "aws_amazonmq": "AmazonMQ",
    "aws_amplify": "Amplify Console",
    "aws_apigateway": "API Gateway",
    "aws_apigatewayv2": "API Gateway V2",
    "aws_appconfig": "AppConfig",
    "aws_applicationautoscaling": "Application Auto Scaling",
    "aws_appmesh": "App Mesh",
    "aws_appstream": "AppStream 2.0",
    "aws_appsync": "AppSync",
    "aws_athena": "Athena",
    "aws_autoscalingplans": "AWS Auto Scaling",
    "aws_autoscaling": "Amazon EC2 Auto Scaling",
    "aws_backup": "AWS Backup",
    "aws_batch": "AWS Batch",
    "aws_budgets": "AWS Budgets",
    "aws_cassandra": "Cassandra",
    "aws_certificatemanager": "Certificate Manager",
    "aws_chatbot": "Chatbot",
    "aws_cloud9": "AWS Cloud9",
    "aws_cloudformation": "CloudFormation",
    "aws_cloudfront": "CloudFront",
    "aws_servicediscovery": "AWS Cloud Map",
    "aws_cloudtrail": "CloudTrail",
    "aws_cloudwatch": "CloudWatch",
    "aws_logs": "CloudWatch Logs",
    "aws_events": "Amazon EventBridge",
    "aws_codebuild": "CodeBuild",
    "aws_codecommit": "CodeCommit",
    "aws_codedeploy": "CodeDeploy",
    "aws_codeguruprofiler": "CodeGuruProfiler",
    "aws_codepipeline": "CodePipeline",
    "aws_codestar": "CodeStar",
    "aws_codestarconnections": "CodeStarConnections",
    "aws_codestarnotifications": "CodeStarNotifications",
    "aws_cognito": "Amazon Cognito",
    "aws_config": "Config",
    "aws_datapipeline": "AWS Data Pipeline",
    "aws_dax": "DAX",
    "aws_detective": "Detective",
    "aws_directoryservice": "Directory Service",
    "aws_dlm": "DLM",
    "aws_dms": "DMS",
    "aws_docdb": "Amazon DocumentDB",
    "aws_dynamodb": "DynamoDB",
    "aws_ec2": "EC2",
    "aws_ecr": "Amazon ECR",
    "aws_ecs": "ECS",
    "aws_efs": "EFS",
    "aws_eks": "EKS",
    "aws_elasticache": "ElastiCache",
    "aws_elasticsearch": "Elasticsearch",
    "aws_elasticbeanstalk": "Elastic Beanstalk",
    "aws_elasticloadbalancing": "Elastic Load Balancing",
    "aws_elasticloadbalancingv2": "ElasticLoadBalancingV2",
    "aws_emr": "Amazon EMR",
    "aws_eventschemas": "EventSchemas",
    "aws_fms": "FMS",
    "aws_fsx": "FSx",
    "aws_gamelift": "GameLift",
    "aws_glue": "AWS Glue",
    "aws_groundstation": "GroundStation",
    "aws_guardduty": "GuardDuty",
    "aws_iam": "IAM",
    "aws_inspector": "Inspector",
    "aws_iot": "IoT",
    "aws_iot1click": "IoT1Click",
    "aws_iotanalytics": "IoT Analytics",
    "aws_iotevents": "IoTEvents",
    "aws_greengrass": "AWS IoT Greengrass",
    "aws_iotthingsgraph": "AWS IoT Things Graph",
    "aws_kinesis": "Amazon Kinesis",
    "aws_kinesisanalytics": "KinesisAnalytics",
    "aws_kinesisanalyticsv2": "Amazon Kinesis Data Analytics V2",
    "aws_kinesisfirehose": "Amazon Kinesis Data Firehose",
    "aws_kms": "KMS",
    "aws_lakeformation": "LakeFormation",
    "aws_lambda": "Lambda",
    "aws_managedblockchain": "ManagedBlockchain",
    "aws_mediaconvert": "MediaConvert",
    "aws_medialive": "MediaLive",
    "aws_mediastore": "MediaStore",
    "aws_msk": "MSK",
    "aws_neptune": "Amazon Neptune",
    "aws_networkmanager": "NetworkManager",
    "aws_opsworks": "OpsWorks",
    "aws_opsworkscm": "OpsWorks-CM",
    "aws_pinpoint": "Pinpoint",
    "aws_pinpointemail": "PinpointEmail",
    "aws_qldb": "QLDB",
    "aws_ram": "RAM",
    "aws_rds": "RDS",
    "aws_redshift": "Amazon Redshift",
    "aws_resourcegroups": "ResourceGroups",
    "aws_robomaker": "RoboMaker",
    "aws_route53": "Route 53",
    "aws_route53resolver": "Route 53 Resolver",
    "aws_s3": "Amazon S3",
    "aws_sagemaker": "Amazon SageMaker",
    "aws_secretsmanager": "Secrets Manager",
    "aws_servicecatalog": "Service Catalog",
    "aws_securityhub": "SecurityHub",
    "aws_ses": "SES",
    "aws_sdb": "Amazon SimpleDB",
    "aws_sns": "Amazon SNS",
    "aws_sqs": "Amazon SQS",
    "aws_stepfunctions": "Step Functions",
    "aws_ssm": "Systems Manager",
    "aws_transfer": "AWS SFTP",
    "aws_waf": "WAF",
    "aws_wafv2": "WAFv2",
    "aws_wafregional": "WAF Regional",
    "aws_workspaces": "WorkSpaces",
}

TEMPLATE = """
{% for service, spec in data.items() %}
### {{ service }}

#### Module

`{{ spec.module }}`

#### Resources

{% for name, resc in spec.resources.items() %}
- {{ name }} - [{{ resc.type }}]({{ resc.url }})
{% endfor %}

{% endfor %}
"""

if __name__ == "__main__":
    base = Path(__file__).parent.parent.parent / "src" / "ingraph" / "aws"
    data = {}
    with aws_hook():
        for file in list(base.glob("[a-z]*_*.pyi")):
            mod = import_module(f"ingraph.aws.{file.stem}")
            rescs = {
                k: {"type": v._ig_kind, "url": v.__doc__.split(" ")[-1]}
                for k, v in vars(mod).items()
                if not k.startswith("_")
            }
            data[INFO[mod.__name__.rpartition(".")[-1]]] = {
                "module": mod.__name__,
                "resources": rescs,
            }
    tpl = jinja2.Template(TEMPLATE)
    print(tpl.render(data=data))
