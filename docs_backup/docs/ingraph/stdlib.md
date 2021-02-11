---
id: stdlib
title: Standard Library
---

This library reference describes the standard library that is
distributed with InGraph.

## Pseudo Parameters

Pseudo parameters are parameters that are predefined by AWS
CloudFormation.

### Module

`ingraph.aws`

### Constants

#### `ACCOUNT_ID: str`

The AWS account ID of the account of the current stack.

#### `AVAILABILITY_ZONES: List[str]`

The list of Availability Zones for the region of the current stack.

```python
from ingraph.aws import AVAILABILITY_ZONES
from ingraph.aws.aws_ec2 import Subnet

class Example:
  def __init__(self, vpc_id: str):
    subnet = Subnet(
      VpcId=vpc_id,
      CidrBlock="10.0.0.0/24",
      AvailabilityZone=AVAILABILITY_ZONES[0],
    )
```

#### `NOTIFICATION_ARNS: List[str]`

The list of notification Amazon Resource Names (ARNs) for the current
stack.

```python
from ingraph.aws import NOTIFICATION_ARNS
from ingraph.aws.aws_autoscaling import AutoScalingGroup

class Example:
  def __init__(self, launch_config_name: str):
    asg = AutoScalingGroup(
      AvailabilityZones=["us-east-1a"],
      LaunchConfigurationName=launch_config_name,
      MinSize="0",
      MaxSize="0",
      NotificationConfigurations=[
        AutoScalingGroup.NotificationConfiguration(
          TopicARN=NOTIFICATION_ARNS[0],
          NotificationTypes=[
            "autoscaling:EC2_INSTANCE_LAUNCH",
            "autoscaling:EC2_INSTANCE_LAUNCH_ERROR",
          ],
        )
      ],
    )
```

#### `PARTITION: str`

For standard AWS regions, the partition is `aws`. For other regions, the
partition is `aws-partitionname`. For example, the partition in the
China (Beijing and Ningxia) region is `aws-cn` and the partition in the
AWS GovCloud (US-West) region is `aws-us-gov`.

#### `REGION: str`

The AWS Region of the current stack.

```python
from ingraph import aws

class Example:
  region: str

  def __init__(self) -> None:
    ...
    self.region = aws.REGION
```

#### `STACK_ID: str`

The ID of the current stack.

#### `STACK_NAME: str`

The name of the current stack.

#### `URL_SUFFIX: str`

The suffix for a domain. The suffix is typically `amazonaws.com`, but
might differ by region. For example, the suffix for the China (Beijing)
region is `amazonaws.com.cn`.

## Intrinsic Functions

Intrinsic functions are functions that are predefined by AWS
CloudFormation.

### Module

`ingraph.aws`

### Functions

#### `b64encode(target: str) -> str`

Returns the Base64 representation of the input string.

#### `cidr(block: str, count: int, bits: int) -> List[str]`

Returns an array of CIDR address blocks.

```python
from ingraph.aws import aws_ec2, cidr

class Example:
  def __init__(self) -> None:
    vpc = aws_ec2.VPC(CidrBlock="10.0.0.0/16")
    vpcblock6 = aws_ec2.VPCCidrBlock(
      AmazonProvidedIpv6CidrBlock=True,
      VpcId=vpc.Ref,
    )
    subblock4 = cidr(block=vpc.CidrBlock, count=1, bits=8)[0]
    subblock6 = cidr(block=vpc.Ipv6CidrBlocks[0], count=1, bits=64)[0]
    subnet = aws_ec2.Subnet(
      AssignIpv6AddressOnCreation=True,
      CidrBlock=subblock4,
      Ipv6CidrBlock=subblock6,
      VpcId=vpc.Ref,
      DependsOn=[vpcblock6],
    )
```

## Assets

### Module

`ingraph.aws`

### Functions

#### `Asset(name: str, package: Optional[ModuleType], compress: Optional[bool])`

Returns an artifact within a package.

```python
from ingraph.aws import Asset, aws_iam, aws_lambda

class InlineExample:
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
```

```python
from ingraph.aws import Asset, aws_iam, aws_lambda

class ZipExample:
  uri: str
  url: str

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
    handler = Asset(name="handler.js", compress=True)
    function = aws_lambda.Function(
      Code=aws_lambda.Function.Code(
        S3Bucket=handler.bucket,
        S3Key=handler.key
      ),
      Handler="index.handle",
      Role=role.Arn,
      Runtime="nodejs12.x",
    )
    self.uri = handler.uri
    self.url = handler.url
```

##### Attributes

###### `url: str`

The S3 URL of the asset.

`https://{BUCKET}.s3.amazonaws.com/{PREFIX}{HASH}`

###### `uri: str`

The S3 URI of the asset.

`s3://{BUCKET}/{PREFIX}{HASH}`

###### `bucket: str`

The S3 bucket of all assets. It is automatically injected in the
parameters section of the final YAML template.

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Parameters:
  AssetsS3Bucket:
    Type: String
```

###### `key: str`

The concatenation of the S3 prefix (if any) with the deterministic hash
of the asset. The S3 prefix is automatically injected in the parameters
section of the final YAML template.

```yaml
AWSTemplateFormatVersion: "2010-09-09"
Parameters:
  AssetsS3Prefix:
    Type: String
```

###### `text: str`

The textual content of an asset. Note that if an asset is compressed,
you cannot reference its textual content.

## Native Resources

Native resources are AWS resources that are predefined by AWS
CloudFormation.

### Amazon EMR

#### Module

`ingraph.aws.aws_emr`

#### Resources

- Cluster - [AWS::EMR::Cluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html)

- InstanceFleetConfig - [AWS::EMR::InstanceFleetConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html)

- InstanceGroupConfig - [AWS::EMR::InstanceGroupConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html)

- SecurityConfiguration - [AWS::EMR::SecurityConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-securityconfiguration.html)

- Step - [AWS::EMR::Step](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html)

### AWS Auto Scaling

#### Module

`ingraph.aws.aws_autoscalingplans`

#### Resources

- ScalingPlan - [AWS::AutoScalingPlans::ScalingPlan](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html)

### MediaLive

#### Module

`ingraph.aws.aws_medialive`

#### Resources

- Channel - [AWS::MediaLive::Channel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html)

- Input - [AWS::MediaLive::Input](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html)

- InputSecurityGroup - [AWS::MediaLive::InputSecurityGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-inputsecuritygroup.html)

### Amazon DocumentDB

#### Module

`ingraph.aws.aws_docdb`

#### Resources

- DBCluster - [AWS::DocDB::DBCluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html)

- DBClusterParameterGroup - [AWS::DocDB::DBClusterParameterGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html)

- DBInstance - [AWS::DocDB::DBInstance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html)

- DBSubnetGroup - [AWS::DocDB::DBSubnetGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html)

### CodeStarConnections

#### Module

`ingraph.aws.aws_codestarconnections`

#### Resources

- Connection - [AWS::CodeStarConnections::Connection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-connection.html)

### API Gateway V2

#### Module

`ingraph.aws.aws_apigatewayv2`

#### Resources

- Api - [AWS::ApiGatewayV2::Api](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html)

- ApiMapping - [AWS::ApiGatewayV2::ApiMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html)

- Authorizer - [AWS::ApiGatewayV2::Authorizer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html)

- Deployment - [AWS::ApiGatewayV2::Deployment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html)

- DomainName - [AWS::ApiGatewayV2::DomainName](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html)

- Integration - [AWS::ApiGatewayV2::Integration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html)

- IntegrationResponse - [AWS::ApiGatewayV2::IntegrationResponse](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html)

- Model - [AWS::ApiGatewayV2::Model](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html)

- Route - [AWS::ApiGatewayV2::Route](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html)

- RouteResponse - [AWS::ApiGatewayV2::RouteResponse](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html)

- Stage - [AWS::ApiGatewayV2::Stage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html)

### AWS SFTP

#### Module

`ingraph.aws.aws_transfer`

#### Resources

- Server - [AWS::Transfer::Server](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html)

- User - [AWS::Transfer::User](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html)

### IoT

#### Module

`ingraph.aws.aws_iot`

#### Resources

- Certificate - [AWS::IoT::Certificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html)

- Policy - [AWS::IoT::Policy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policy.html)

- PolicyPrincipalAttachment - [AWS::IoT::PolicyPrincipalAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policyprincipalattachment.html)

- Thing - [AWS::IoT::Thing](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thing.html)

- ThingPrincipalAttachment - [AWS::IoT::ThingPrincipalAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thingprincipalattachment.html)

- TopicRule - [AWS::IoT::TopicRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html)

### Amazon Kinesis

#### Module

`ingraph.aws.aws_kinesis`

#### Resources

- Stream - [AWS::Kinesis::Stream](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-stream.html)

- StreamConsumer - [AWS::Kinesis::StreamConsumer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesis-streamconsumer.html)

### RAM

#### Module

`ingraph.aws.aws_ram`

#### Resources

- ResourceShare - [AWS::RAM::ResourceShare](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html)

### Amazon Kinesis Data Analytics V2

#### Module

`ingraph.aws.aws_kinesisanalyticsv2`

#### Resources

- Application - [AWS::KinesisAnalyticsV2::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html)

- ApplicationCloudWatchLoggingOption - [AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html)

- ApplicationOutput - [AWS::KinesisAnalyticsV2::ApplicationOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html)

- ApplicationReferenceDataSource - [AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html)

### ResourceGroups

#### Module

`ingraph.aws.aws_resourcegroups`

#### Resources

- Group - [AWS::ResourceGroups::Group](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourcegroups-group.html)

### DAX

#### Module

`ingraph.aws.aws_dax`

#### Resources

- Cluster - [AWS::DAX::Cluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html)

- ParameterGroup - [AWS::DAX::ParameterGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-parametergroup.html)

- SubnetGroup - [AWS::DAX::SubnetGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-subnetgroup.html)

### Lambda

#### Module

`ingraph.aws.aws_lambda`

#### Resources

- Alias - [AWS::Lambda::Alias](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html)

- EventInvokeConfig - [AWS::Lambda::EventInvokeConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html)

- EventSourceMapping - [AWS::Lambda::EventSourceMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html)

- Function - [AWS::Lambda::Function](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html)

- LayerVersion - [AWS::Lambda::LayerVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html)

- LayerVersionPermission - [AWS::Lambda::LayerVersionPermission](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html)

- Permission - [AWS::Lambda::Permission](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html)

- Version - [AWS::Lambda::Version](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html)

### ElastiCache

#### Module

`ingraph.aws.aws_elasticache`

#### Resources

- CacheCluster - [AWS::ElastiCache::CacheCluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html)

- ParameterGroup - [AWS::ElastiCache::ParameterGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-parameter-group.html)

- ReplicationGroup - [AWS::ElastiCache::ReplicationGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html)

- SecurityGroup - [AWS::ElastiCache::SecurityGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group.html)

- SecurityGroupIngress - [AWS::ElastiCache::SecurityGroupIngress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group-ingress.html)

- SubnetGroup - [AWS::ElastiCache::SubnetGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-subnetgroup.html)

### MediaConvert

#### Module

`ingraph.aws.aws_mediaconvert`

#### Resources

- JobTemplate - [AWS::MediaConvert::JobTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-jobtemplate.html)

- Preset - [AWS::MediaConvert::Preset](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-preset.html)

- Queue - [AWS::MediaConvert::Queue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconvert-queue.html)

### WorkSpaces

#### Module

`ingraph.aws.aws_workspaces`

#### Resources

- Workspace - [AWS::WorkSpaces::Workspace](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspaces-workspace.html)

### CodePipeline

#### Module

`ingraph.aws.aws_codepipeline`

#### Resources

- CustomActionType - [AWS::CodePipeline::CustomActionType](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-customactiontype.html)

- Pipeline - [AWS::CodePipeline::Pipeline](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-pipeline.html)

- Webhook - [AWS::CodePipeline::Webhook](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-webhook.html)

### ElasticLoadBalancingV2

#### Module

`ingraph.aws.aws_elasticloadbalancingv2`

#### Resources

- Listener - [AWS::ElasticLoadBalancingV2::Listener](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listener.html)

- ListenerCertificate - [AWS::ElasticLoadBalancingV2::ListenerCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenercertificate.html)

- ListenerRule - [AWS::ElasticLoadBalancingV2::ListenerRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenerrule.html)

- LoadBalancer - [AWS::ElasticLoadBalancingV2::LoadBalancer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.html)

- TargetGroup - [AWS::ElasticLoadBalancingV2::TargetGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html)

### CloudWatch Logs

#### Module

`ingraph.aws.aws_logs`

#### Resources

- Destination - [AWS::Logs::Destination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html)

- LogGroup - [AWS::Logs::LogGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html)

- LogStream - [AWS::Logs::LogStream](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-logstream.html)

- MetricFilter - [AWS::Logs::MetricFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html)

- SubscriptionFilter - [AWS::Logs::SubscriptionFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html)

### AWS Cloud9

#### Module

`ingraph.aws.aws_cloud9`

#### Resources

- EnvironmentEC2 - [AWS::Cloud9::EnvironmentEC2](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html)

### CodeBuild

#### Module

`ingraph.aws.aws_codebuild`

#### Resources

- Project - [AWS::CodeBuild::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html)

- ReportGroup - [AWS::CodeBuild::ReportGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html)

- SourceCredential - [AWS::CodeBuild::SourceCredential](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.html)

### CloudFront

#### Module

`ingraph.aws.aws_cloudfront`

#### Resources

- CloudFrontOriginAccessIdentity - [AWS::CloudFront::CloudFrontOriginAccessIdentity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-cloudfrontoriginaccessidentity.html)

- Distribution - [AWS::CloudFront::Distribution](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-distribution.html)

- StreamingDistribution - [AWS::CloudFront::StreamingDistribution](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-streamingdistribution.html)

### Service Catalog

#### Module

`ingraph.aws.aws_servicecatalog`

#### Resources

- AcceptedPortfolioShare - [AWS::ServiceCatalog::AcceptedPortfolioShare](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html)

- CloudFormationProduct - [AWS::ServiceCatalog::CloudFormationProduct](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html)

- CloudFormationProvisionedProduct - [AWS::ServiceCatalog::CloudFormationProvisionedProduct](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html)

- LaunchNotificationConstraint - [AWS::ServiceCatalog::LaunchNotificationConstraint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html)

- LaunchRoleConstraint - [AWS::ServiceCatalog::LaunchRoleConstraint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html)

- LaunchTemplateConstraint - [AWS::ServiceCatalog::LaunchTemplateConstraint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html)

- Portfolio - [AWS::ServiceCatalog::Portfolio](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html)

- PortfolioPrincipalAssociation - [AWS::ServiceCatalog::PortfolioPrincipalAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html)

- PortfolioProductAssociation - [AWS::ServiceCatalog::PortfolioProductAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html)

- PortfolioShare - [AWS::ServiceCatalog::PortfolioShare](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html)

- ResourceUpdateConstraint - [AWS::ServiceCatalog::ResourceUpdateConstraint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html)

- StackSetConstraint - [AWS::ServiceCatalog::StackSetConstraint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html)

- TagOption - [AWS::ServiceCatalog::TagOption](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html)

- TagOptionAssociation - [AWS::ServiceCatalog::TagOptionAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html)

### Amazon ECR

#### Module

`ingraph.aws.aws_ecr`

#### Resources

- Repository - [AWS::ECR::Repository](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html)

### Route 53

#### Module

`ingraph.aws.aws_route53`

#### Resources

- HealthCheck - [AWS::Route53::HealthCheck](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html)

- HostedZone - [AWS::Route53::HostedZone](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html)

- RecordSet - [AWS::Route53::RecordSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html)

- RecordSetGroup - [AWS::Route53::RecordSetGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html)

### AppConfig

#### Module

`ingraph.aws.aws_appconfig`

#### Resources

- Application - [AWS::AppConfig::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html)

- ConfigurationProfile - [AWS::AppConfig::ConfigurationProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html)

- Deployment - [AWS::AppConfig::Deployment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html)

- DeploymentStrategy - [AWS::AppConfig::DeploymentStrategy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html)

- Environment - [AWS::AppConfig::Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html)

### EKS

#### Module

`ingraph.aws.aws_eks`

#### Resources

- Cluster - [AWS::EKS::Cluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html)

- Nodegroup - [AWS::EKS::Nodegroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html)

### ManagedBlockchain

#### Module

`ingraph.aws.aws_managedblockchain`

#### Resources

- Member - [AWS::ManagedBlockchain::Member](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-member.html)

- Node - [AWS::ManagedBlockchain::Node](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-node.html)

### GroundStation

#### Module

`ingraph.aws.aws_groundstation`

#### Resources

- Config - [AWS::GroundStation::Config](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html)

- DataflowEndpointGroup - [AWS::GroundStation::DataflowEndpointGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html)

- MissionProfile - [AWS::GroundStation::MissionProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html)

### AmazonMQ

#### Module

`ingraph.aws.aws_amazonmq`

#### Resources

- Broker - [AWS::AmazonMQ::Broker](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html)

- Configuration - [AWS::AmazonMQ::Configuration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html)

- ConfigurationAssociation - [AWS::AmazonMQ::ConfigurationAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configurationassociation.html)

### Amazon SageMaker

#### Module

`ingraph.aws.aws_sagemaker`

#### Resources

- CodeRepository - [AWS::SageMaker::CodeRepository](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html)

- Endpoint - [AWS::SageMaker::Endpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html)

- EndpointConfig - [AWS::SageMaker::EndpointConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html)

- Model - [AWS::SageMaker::Model](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html)

- NotebookInstance - [AWS::SageMaker::NotebookInstance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html)

- NotebookInstanceLifecycleConfig - [AWS::SageMaker::NotebookInstanceLifecycleConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html)

- Workteam - [AWS::SageMaker::Workteam](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html)

### Chatbot

#### Module

`ingraph.aws.aws_chatbot`

#### Resources

- SlackChannelConfiguration - [AWS::Chatbot::SlackChannelConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html)

### OpsWorks

#### Module

`ingraph.aws.aws_opsworks`

#### Resources

- App - [AWS::OpsWorks::App](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html)

- ElasticLoadBalancerAttachment - [AWS::OpsWorks::ElasticLoadBalancerAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-elbattachment.html)

- Instance - [AWS::OpsWorks::Instance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html)

- Layer - [AWS::OpsWorks::Layer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html)

- Stack - [AWS::OpsWorks::Stack](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html)

- UserProfile - [AWS::OpsWorks::UserProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html)

- Volume - [AWS::OpsWorks::Volume](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html)

### SecurityHub

#### Module

`ingraph.aws.aws_securityhub`

#### Resources

- Hub - [AWS::SecurityHub::Hub](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html)

### Route 53 Resolver

#### Module

`ingraph.aws.aws_route53resolver`

#### Resources

- ResolverEndpoint - [AWS::Route53Resolver::ResolverEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html)

- ResolverRule - [AWS::Route53Resolver::ResolverRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html)

- ResolverRuleAssociation - [AWS::Route53Resolver::ResolverRuleAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html)

### IAM

#### Module

`ingraph.aws.aws_iam`

#### Resources

- AccessKey - [AWS::IAM::AccessKey](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html)

- Group - [AWS::IAM::Group](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html)

- InstanceProfile - [AWS::IAM::InstanceProfile](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html)

- ManagedPolicy - [AWS::IAM::ManagedPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html)

- Policy - [AWS::IAM::Policy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html)

- Role - [AWS::IAM::Role](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html)

- ServiceLinkedRole - [AWS::IAM::ServiceLinkedRole](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html)

- User - [AWS::IAM::User](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html)

- UserToGroupAddition - [AWS::IAM::UserToGroupAddition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html)

### Elastic Load Balancing

#### Module

`ingraph.aws.aws_elasticloadbalancing`

#### Resources

- LoadBalancer - [AWS::ElasticLoadBalancing::LoadBalancer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html)

### API Gateway

#### Module

`ingraph.aws.aws_apigateway`

#### Resources

- Account - [AWS::ApiGateway::Account](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-account.html)

- ApiKey - [AWS::ApiGateway::ApiKey](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-apikey.html)

- Authorizer - [AWS::ApiGateway::Authorizer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-authorizer.html)

- BasePathMapping - [AWS::ApiGateway::BasePathMapping](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-basepathmapping.html)

- ClientCertificate - [AWS::ApiGateway::ClientCertificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-clientcertificate.html)

- Deployment - [AWS::ApiGateway::Deployment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-deployment.html)

- DocumentationPart - [AWS::ApiGateway::DocumentationPart](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-documentationpart.html)

- DocumentationVersion - [AWS::ApiGateway::DocumentationVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-documentationversion.html)

- DomainName - [AWS::ApiGateway::DomainName](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html)

- GatewayResponse - [AWS::ApiGateway::GatewayResponse](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-gatewayresponse.html)

- Method - [AWS::ApiGateway::Method](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-method.html)

- Model - [AWS::ApiGateway::Model](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-model.html)

- RequestValidator - [AWS::ApiGateway::RequestValidator](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-requestvalidator.html)

- Resource - [AWS::ApiGateway::Resource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-resource.html)

- RestApi - [AWS::ApiGateway::RestApi](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html)

- Stage - [AWS::ApiGateway::Stage](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html)

- UsagePlan - [AWS::ApiGateway::UsagePlan](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.html)

- UsagePlanKey - [AWS::ApiGateway::UsagePlanKey](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplankey.html)

- VpcLink - [AWS::ApiGateway::VpcLink](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-vpclink.html)

### GameLift

#### Module

`ingraph.aws.aws_gamelift`

#### Resources

- Alias - [AWS::GameLift::Alias](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html)

- Build - [AWS::GameLift::Build](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html)

- Fleet - [AWS::GameLift::Fleet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html)

- GameSessionQueue - [AWS::GameLift::GameSessionQueue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html)

- MatchmakingConfiguration - [AWS::GameLift::MatchmakingConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html)

- MatchmakingRuleSet - [AWS::GameLift::MatchmakingRuleSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html)

- Script - [AWS::GameLift::Script](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html)

### EventSchemas

#### Module

`ingraph.aws.aws_eventschemas`

#### Resources

- Discoverer - [AWS::EventSchemas::Discoverer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html)

- Registry - [AWS::EventSchemas::Registry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html)

- Schema - [AWS::EventSchemas::Schema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html)

### AppSync

#### Module

`ingraph.aws.aws_appsync`

#### Resources

- ApiCache - [AWS::AppSync::ApiCache](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html)

- ApiKey - [AWS::AppSync::ApiKey](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html)

- DataSource - [AWS::AppSync::DataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html)

- FunctionConfiguration - [AWS::AppSync::FunctionConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html)

- GraphQLApi - [AWS::AppSync::GraphQLApi](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html)

- GraphQLSchema - [AWS::AppSync::GraphQLSchema](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html)

- Resolver - [AWS::AppSync::Resolver](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html)

### Amazon SimpleDB

#### Module

`ingraph.aws.aws_sdb`

#### Resources

- Domain - [AWS::SDB::Domain](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-simpledb.html)

### Step Functions

#### Module

`ingraph.aws.aws_stepfunctions`

#### Resources

- Activity - [AWS::StepFunctions::Activity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html)

- StateMachine - [AWS::StepFunctions::StateMachine](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html)

### DLM

#### Module

`ingraph.aws.aws_dlm`

#### Resources

- LifecyclePolicy - [AWS::DLM::LifecyclePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html)

### Systems Manager

#### Module

`ingraph.aws.aws_ssm`

#### Resources

- Association - [AWS::SSM::Association](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html)

- Document - [AWS::SSM::Document](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html)

- MaintenanceWindow - [AWS::SSM::MaintenanceWindow](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html)

- MaintenanceWindowTarget - [AWS::SSM::MaintenanceWindowTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html)

- MaintenanceWindowTask - [AWS::SSM::MaintenanceWindowTask](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html)

- Parameter - [AWS::SSM::Parameter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html)

- PatchBaseline - [AWS::SSM::PatchBaseline](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html)

- ResourceDataSync - [AWS::SSM::ResourceDataSync](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html)

### IoT1Click

#### Module

`ingraph.aws.aws_iot1click`

#### Resources

- Device - [AWS::IoT1Click::Device](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-device.html)

- Placement - [AWS::IoT1Click::Placement](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html)

- Project - [AWS::IoT1Click::Project](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-project.html)

### CloudFormation

#### Module

`ingraph.aws.aws_cloudformation`

#### Resources

- CustomResource - [AWS::CloudFormation::CustomResource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html)

- Macro - [AWS::CloudFormation::Macro](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html)

- Stack - [AWS::CloudFormation::Stack](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html)

- WaitCondition - [AWS::CloudFormation::WaitCondition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html)

- WaitConditionHandle - [AWS::CloudFormation::WaitConditionHandle](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitconditionhandle.html)

### MediaStore

#### Module

`ingraph.aws.aws_mediastore`

#### Resources

- Container - [AWS::MediaStore::Container](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediastore-container.html)

### FSx

#### Module

`ingraph.aws.aws_fsx`

#### Resources

- FileSystem - [AWS::FSx::FileSystem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html)

### FMS

#### Module

`ingraph.aws.aws_fms`

#### Resources

- NotificationChannel - [AWS::FMS::NotificationChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html)

- Policy - [AWS::FMS::Policy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html)

### AWS Data Pipeline

#### Module

`ingraph.aws.aws_datapipeline`

#### Resources

- Pipeline - [AWS::DataPipeline::Pipeline](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html)

### Amazon EC2 Auto Scaling

#### Module

`ingraph.aws.aws_autoscaling`

#### Resources

- AutoScalingGroup - [AWS::AutoScaling::AutoScalingGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html)

- LaunchConfiguration - [AWS::AutoScaling::LaunchConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html)

- LifecycleHook - [AWS::AutoScaling::LifecycleHook](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-lifecyclehook.html)

- ScalingPolicy - [AWS::AutoScaling::ScalingPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html)

- ScheduledAction - [AWS::AutoScaling::ScheduledAction](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-scheduledaction.html)

### AWS Budgets

#### Module

`ingraph.aws.aws_budgets`

#### Resources

- Budget - [AWS::Budgets::Budget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html)

### AWS Backup

#### Module

`ingraph.aws.aws_backup`

#### Resources

- BackupPlan - [AWS::Backup::BackupPlan](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html)

- BackupSelection - [AWS::Backup::BackupSelection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html)

- BackupVault - [AWS::Backup::BackupVault](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html)

### GuardDuty

#### Module

`ingraph.aws.aws_guardduty`

#### Resources

- Detector - [AWS::GuardDuty::Detector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html)

- Filter - [AWS::GuardDuty::Filter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html)

- IPSet - [AWS::GuardDuty::IPSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html)

- Master - [AWS::GuardDuty::Master](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html)

- Member - [AWS::GuardDuty::Member](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html)

- ThreatIntelSet - [AWS::GuardDuty::ThreatIntelSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html)

### Amazon SQS

#### Module

`ingraph.aws.aws_sqs`

#### Resources

- Queue - [AWS::SQS::Queue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-queues.html)

- QueuePolicy - [AWS::SQS::QueuePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.html)

### CodeStarNotifications

#### Module

`ingraph.aws.aws_codestarnotifications`

#### Resources

- NotificationRule - [AWS::CodeStarNotifications::NotificationRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html)

### Directory Service

#### Module

`ingraph.aws.aws_directoryservice`

#### Resources

- MicrosoftAD - [AWS::DirectoryService::MicrosoftAD](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html)

- SimpleAD - [AWS::DirectoryService::SimpleAD](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html)

### DynamoDB

#### Module

`ingraph.aws.aws_dynamodb`

#### Resources

- Table - [AWS::DynamoDB::Table](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html)

### Amazon Kinesis Data Firehose

#### Module

`ingraph.aws.aws_kinesisfirehose`

#### Resources

- DeliveryStream - [AWS::KinesisFirehose::DeliveryStream](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html)

### AWS IoT Things Graph

#### Module

`ingraph.aws.aws_iotthingsgraph`

#### Resources

- FlowTemplate - [AWS::IoTThingsGraph::FlowTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html)

### App Mesh

#### Module

`ingraph.aws.aws_appmesh`

#### Resources

- Mesh - [AWS::AppMesh::Mesh](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html)

- Route - [AWS::AppMesh::Route](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html)

- VirtualNode - [AWS::AppMesh::VirtualNode](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html)

- VirtualRouter - [AWS::AppMesh::VirtualRouter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html)

- VirtualService - [AWS::AppMesh::VirtualService](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html)

### DMS

#### Module

`ingraph.aws.aws_dms`

#### Resources

- Certificate - [AWS::DMS::Certificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.html)

- Endpoint - [AWS::DMS::Endpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html)

- EventSubscription - [AWS::DMS::EventSubscription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html)

- ReplicationInstance - [AWS::DMS::ReplicationInstance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html)

- ReplicationSubnetGroup - [AWS::DMS::ReplicationSubnetGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html)

- ReplicationTask - [AWS::DMS::ReplicationTask](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html)

### CodeGuruProfiler

#### Module

`ingraph.aws.aws_codeguruprofiler`

#### Resources

- ProfilingGroup - [AWS::CodeGuruProfiler::ProfilingGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeguruprofiler-profilinggroup.html)

### RDS

#### Module

`ingraph.aws.aws_rds`

#### Resources

- DBCluster - [AWS::RDS::DBCluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html)

- DBClusterParameterGroup - [AWS::RDS::DBClusterParameterGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbclusterparametergroup.html)

- DBInstance - [AWS::RDS::DBInstance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html)

- DBParameterGroup - [AWS::RDS::DBParameterGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbparametergroup.html)

- DBSecurityGroup - [AWS::RDS::DBSecurityGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group.html)

- DBSecurityGroupIngress - [AWS::RDS::DBSecurityGroupIngress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-security-group-ingress.html)

- DBSubnetGroup - [AWS::RDS::DBSubnetGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbsubnet-group.html)

- EventSubscription - [AWS::RDS::EventSubscription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-eventsubscription.html)

- OptionGroup - [AWS::RDS::OptionGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html)

### CloudTrail

#### Module

`ingraph.aws.aws_cloudtrail`

#### Resources

- Trail - [AWS::CloudTrail::Trail](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html)

### QLDB

#### Module

`ingraph.aws.aws_qldb`

#### Resources

- Ledger - [AWS::QLDB::Ledger](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qldb-ledger.html)

### Elastic Beanstalk

#### Module

`ingraph.aws.aws_elasticbeanstalk`

#### Resources

- Application - [AWS::ElasticBeanstalk::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk.html)

- ApplicationVersion - [AWS::ElasticBeanstalk::ApplicationVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-version.html)

- ConfigurationTemplate - [AWS::ElasticBeanstalk::ConfigurationTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html)

- Environment - [AWS::ElasticBeanstalk::Environment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html)

### RoboMaker

#### Module

`ingraph.aws.aws_robomaker`

#### Resources

- Fleet - [AWS::RoboMaker::Fleet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-fleet.html)

- Robot - [AWS::RoboMaker::Robot](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robot.html)

- RobotApplication - [AWS::RoboMaker::RobotApplication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html)

- RobotApplicationVersion - [AWS::RoboMaker::RobotApplicationVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplicationversion.html)

- SimulationApplication - [AWS::RoboMaker::SimulationApplication](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html)

- SimulationApplicationVersion - [AWS::RoboMaker::SimulationApplicationVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplicationversion.html)

### Amazon Cognito

#### Module

`ingraph.aws.aws_cognito`

#### Resources

- IdentityPool - [AWS::Cognito::IdentityPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html)

- IdentityPoolRoleAttachment - [AWS::Cognito::IdentityPoolRoleAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolroleattachment.html)

- UserPool - [AWS::Cognito::UserPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html)

- UserPoolClient - [AWS::Cognito::UserPoolClient](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html)

- UserPoolDomain - [AWS::Cognito::UserPoolDomain](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooldomain.html)

- UserPoolGroup - [AWS::Cognito::UserPoolGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolgroup.html)

- UserPoolIdentityProvider - [AWS::Cognito::UserPoolIdentityProvider](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolidentityprovider.html)

- UserPoolResourceServer - [AWS::Cognito::UserPoolResourceServer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolresourceserver.html)

- UserPoolRiskConfigurationAttachment - [AWS::Cognito::UserPoolRiskConfigurationAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolriskconfigurationattachment.html)

- UserPoolUICustomizationAttachment - [AWS::Cognito::UserPoolUICustomizationAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluicustomizationattachment.html)

- UserPoolUser - [AWS::Cognito::UserPoolUser](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html)

- UserPoolUserToGroupAttachment - [AWS::Cognito::UserPoolUserToGroupAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolusertogroupattachment.html)

### IoT Analytics

#### Module

`ingraph.aws.aws_iotanalytics`

#### Resources

- Channel - [AWS::IoTAnalytics::Channel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html)

- Dataset - [AWS::IoTAnalytics::Dataset](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html)

- Datastore - [AWS::IoTAnalytics::Datastore](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html)

- Pipeline - [AWS::IoTAnalytics::Pipeline](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-pipeline.html)

### Amazon Redshift

#### Module

`ingraph.aws.aws_redshift`

#### Resources

- Cluster - [AWS::Redshift::Cluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html)

- ClusterParameterGroup - [AWS::Redshift::ClusterParameterGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html)

- ClusterSecurityGroup - [AWS::Redshift::ClusterSecurityGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroup.html)

- ClusterSecurityGroupIngress - [AWS::Redshift::ClusterSecurityGroupIngress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html)

- ClusterSubnetGroup - [AWS::Redshift::ClusterSubnetGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersubnetgroup.html)

### WAFv2

#### Module

`ingraph.aws.aws_wafv2`

#### Resources

- IPSet - [AWS::WAFv2::IPSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html)

- RegexPatternSet - [AWS::WAFv2::RegexPatternSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html)

- RuleGroup - [AWS::WAFv2::RuleGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html)

- WebACL - [AWS::WAFv2::WebACL](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html)

- WebACLAssociation - [AWS::WAFv2::WebACLAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html)

### AppStream 2.0

#### Module

`ingraph.aws.aws_appstream`

#### Resources

- DirectoryConfig - [AWS::AppStream::DirectoryConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-directoryconfig.html)

- Fleet - [AWS::AppStream::Fleet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html)

- ImageBuilder - [AWS::AppStream::ImageBuilder](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html)

- Stack - [AWS::AppStream::Stack](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html)

- StackFleetAssociation - [AWS::AppStream::StackFleetAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackfleetassociation.html)

- StackUserAssociation - [AWS::AppStream::StackUserAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackuserassociation.html)

- User - [AWS::AppStream::User](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-user.html)

### ASK

#### Module

`ingraph.aws.alexa_ask`

#### Resources

- Skill - [Alexa::ASK::Skill](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html)

### Pinpoint

#### Module

`ingraph.aws.aws_pinpoint`

#### Resources

- ADMChannel - [AWS::Pinpoint::ADMChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html)

- APNSChannel - [AWS::Pinpoint::APNSChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html)

- APNSSandboxChannel - [AWS::Pinpoint::APNSSandboxChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html)

- APNSVoipChannel - [AWS::Pinpoint::APNSVoipChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html)

- APNSVoipSandboxChannel - [AWS::Pinpoint::APNSVoipSandboxChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html)

- App - [AWS::Pinpoint::App](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html)

- ApplicationSettings - [AWS::Pinpoint::ApplicationSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html)

- BaiduChannel - [AWS::Pinpoint::BaiduChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html)

- Campaign - [AWS::Pinpoint::Campaign](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html)

- EmailChannel - [AWS::Pinpoint::EmailChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html)

- EmailTemplate - [AWS::Pinpoint::EmailTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html)

- EventStream - [AWS::Pinpoint::EventStream](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html)

- GCMChannel - [AWS::Pinpoint::GCMChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html)

- PushTemplate - [AWS::Pinpoint::PushTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html)

- SMSChannel - [AWS::Pinpoint::SMSChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html)

- Segment - [AWS::Pinpoint::Segment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html)

- SmsTemplate - [AWS::Pinpoint::SmsTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html)

- VoiceChannel - [AWS::Pinpoint::VoiceChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-voicechannel.html)

### Secrets Manager

#### Module

`ingraph.aws.aws_secretsmanager`

#### Resources

- ResourcePolicy - [AWS::SecretsManager::ResourcePolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-resourcepolicy.html)

- RotationSchedule - [AWS::SecretsManager::RotationSchedule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-rotationschedule.html)

- Secret - [AWS::SecretsManager::Secret](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secret.html)

- SecretTargetAttachment - [AWS::SecretsManager::SecretTargetAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secrettargetattachment.html)

### OpsWorks-CM

#### Module

`ingraph.aws.aws_opsworkscm`

#### Resources

- Server - [AWS::OpsWorksCM::Server](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html)

### Amazon SNS

#### Module

`ingraph.aws.aws_sns`

#### Resources

- Subscription - [AWS::SNS::Subscription](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html)

- Topic - [AWS::SNS::Topic](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic.html)

- TopicPolicy - [AWS::SNS::TopicPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html)

### MSK

#### Module

`ingraph.aws.aws_msk`

#### Resources

- Cluster - [AWS::MSK::Cluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html)

### WAF Regional

#### Module

`ingraph.aws.aws_wafregional`

#### Resources

- ByteMatchSet - [AWS::WAFRegional::ByteMatchSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-bytematchset.html)

- GeoMatchSet - [AWS::WAFRegional::GeoMatchSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-geomatchset.html)

- IPSet - [AWS::WAFRegional::IPSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ipset.html)

- RateBasedRule - [AWS::WAFRegional::RateBasedRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html)

- RegexPatternSet - [AWS::WAFRegional::RegexPatternSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-regexpatternset.html)

- Rule - [AWS::WAFRegional::Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html)

- SizeConstraintSet - [AWS::WAFRegional::SizeConstraintSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sizeconstraintset.html)

- SqlInjectionMatchSet - [AWS::WAFRegional::SqlInjectionMatchSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sqlinjectionmatchset.html)

- WebACL - [AWS::WAFRegional::WebACL](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html)

- WebACLAssociation - [AWS::WAFRegional::WebACLAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webaclassociation.html)

- XssMatchSet - [AWS::WAFRegional::XssMatchSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-xssmatchset.html)

### CodeCommit

#### Module

`ingraph.aws.aws_codecommit`

#### Resources

- Repository - [AWS::CodeCommit::Repository](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.html)

### SES

#### Module

`ingraph.aws.aws_ses`

#### Resources

- ConfigurationSet - [AWS::SES::ConfigurationSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html)

- ConfigurationSetEventDestination - [AWS::SES::ConfigurationSetEventDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html)

- ReceiptFilter - [AWS::SES::ReceiptFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptfilter.html)

- ReceiptRule - [AWS::SES::ReceiptRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html)

- ReceiptRuleSet - [AWS::SES::ReceiptRuleSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptruleset.html)

- Template - [AWS::SES::Template](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-template.html)

### Elasticsearch

#### Module

`ingraph.aws.aws_elasticsearch`

#### Resources

- Domain - [AWS::Elasticsearch::Domain](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html)

### Amplify Console

#### Module

`ingraph.aws.aws_amplify`

#### Resources

- App - [AWS::Amplify::App](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html)

- Branch - [AWS::Amplify::Branch](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html)

- Domain - [AWS::Amplify::Domain](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html)

### PinpointEmail

#### Module

`ingraph.aws.aws_pinpointemail`

#### Resources

- ConfigurationSet - [AWS::PinpointEmail::ConfigurationSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html)

- ConfigurationSetEventDestination - [AWS::PinpointEmail::ConfigurationSetEventDestination](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html)

- DedicatedIpPool - [AWS::PinpointEmail::DedicatedIpPool](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html)

- Identity - [AWS::PinpointEmail::Identity](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html)

### Amazon EventBridge

#### Module

`ingraph.aws.aws_events`

#### Resources

- EventBus - [AWS::Events::EventBus](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbus.html)

- EventBusPolicy - [AWS::Events::EventBusPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html)

- Rule - [AWS::Events::Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html)

### ACMPCA

#### Module

`ingraph.aws.aws_acmpca`

#### Resources

- Certificate - [AWS::ACMPCA::Certificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html)

- CertificateAuthority - [AWS::ACMPCA::CertificateAuthority](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html)

- CertificateAuthorityActivation - [AWS::ACMPCA::CertificateAuthorityActivation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html)

### KinesisAnalytics

#### Module

`ingraph.aws.aws_kinesisanalytics`

#### Resources

- Application - [AWS::KinesisAnalytics::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html)

- ApplicationOutput - [AWS::KinesisAnalytics::ApplicationOutput](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html)

- ApplicationReferenceDataSource - [AWS::KinesisAnalytics::ApplicationReferenceDataSource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html)

### LakeFormation

#### Module

`ingraph.aws.aws_lakeformation`

#### Resources

- DataLakeSettings - [AWS::LakeFormation::DataLakeSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html)

- Permissions - [AWS::LakeFormation::Permissions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html)

- Resource - [AWS::LakeFormation::Resource](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html)

### Amazon S3

#### Module

`ingraph.aws.aws_s3`

#### Resources

- AccessPoint - [AWS::S3::AccessPoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-accesspoint.html)

- Bucket - [AWS::S3::Bucket](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html)

- BucketPolicy - [AWS::S3::BucketPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html)

### EC2

#### Module

`ingraph.aws.aws_ec2`

#### Resources

- CapacityReservation - [AWS::EC2::CapacityReservation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html)

- ClientVpnAuthorizationRule - [AWS::EC2::ClientVpnAuthorizationRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.html)

- ClientVpnEndpoint - [AWS::EC2::ClientVpnEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html)

- ClientVpnRoute - [AWS::EC2::ClientVpnRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnroute.html)

- ClientVpnTargetNetworkAssociation - [AWS::EC2::ClientVpnTargetNetworkAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpntargetnetworkassociation.html)

- CustomerGateway - [AWS::EC2::CustomerGateway](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-customer-gateway.html)

- DHCPOptions - [AWS::EC2::DHCPOptions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcp-options.html)

- EC2Fleet - [AWS::EC2::EC2Fleet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html)

- EIP - [AWS::EC2::EIP](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip.html)

- EIPAssociation - [AWS::EC2::EIPAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip-association.html)

- EgressOnlyInternetGateway - [AWS::EC2::EgressOnlyInternetGateway](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-egressonlyinternetgateway.html)

- FlowLog - [AWS::EC2::FlowLog](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html)

- GatewayRouteTableAssociation - [AWS::EC2::GatewayRouteTableAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-gatewayroutetableassociation.html)

- Host - [AWS::EC2::Host](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.html)

- Instance - [AWS::EC2::Instance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html)

- InternetGateway - [AWS::EC2::InternetGateway](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-internetgateway.html)

- LaunchTemplate - [AWS::EC2::LaunchTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html)

- LocalGatewayRoute - [AWS::EC2::LocalGatewayRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroute.html)

- LocalGatewayRouteTableVPCAssociation - [AWS::EC2::LocalGatewayRouteTableVPCAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetablevpcassociation.html)

- NatGateway - [AWS::EC2::NatGateway](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-natgateway.html)

- NetworkAcl - [AWS::EC2::NetworkAcl](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl.html)

- NetworkAclEntry - [AWS::EC2::NetworkAclEntry](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html)

- NetworkInterface - [AWS::EC2::NetworkInterface](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html)

- NetworkInterfaceAttachment - [AWS::EC2::NetworkInterfaceAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface-attachment.html)

- NetworkInterfacePermission - [AWS::EC2::NetworkInterfacePermission](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterfacepermission.html)

- PlacementGroup - [AWS::EC2::PlacementGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-placementgroup.html)

- Route - [AWS::EC2::Route](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html)

- RouteTable - [AWS::EC2::RouteTable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route-table.html)

- SecurityGroup - [AWS::EC2::SecurityGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html)

- SecurityGroupEgress - [AWS::EC2::SecurityGroupEgress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html)

- SecurityGroupIngress - [AWS::EC2::SecurityGroupIngress](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html)

- SpotFleet - [AWS::EC2::SpotFleet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-spotfleet.html)

- Subnet - [AWS::EC2::Subnet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html)

- SubnetCidrBlock - [AWS::EC2::SubnetCidrBlock](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnetcidrblock.html)

- SubnetNetworkAclAssociation - [AWS::EC2::SubnetNetworkAclAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet-network-acl-assoc.html)

- SubnetRouteTableAssociation - [AWS::EC2::SubnetRouteTableAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet-route-table-assoc.html)

- TrafficMirrorFilter - [AWS::EC2::TrafficMirrorFilter](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilter.html)

- TrafficMirrorFilterRule - [AWS::EC2::TrafficMirrorFilterRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilterrule.html)

- TrafficMirrorSession - [AWS::EC2::TrafficMirrorSession](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorsession.html)

- TrafficMirrorTarget - [AWS::EC2::TrafficMirrorTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrortarget.html)

- TransitGateway - [AWS::EC2::TransitGateway](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html)

- TransitGatewayAttachment - [AWS::EC2::TransitGatewayAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayattachment.html)

- TransitGatewayRoute - [AWS::EC2::TransitGatewayRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroute.html)

- TransitGatewayRouteTable - [AWS::EC2::TransitGatewayRouteTable](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetable.html)

- TransitGatewayRouteTableAssociation - [AWS::EC2::TransitGatewayRouteTableAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetableassociation.html)

- TransitGatewayRouteTablePropagation - [AWS::EC2::TransitGatewayRouteTablePropagation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetablepropagation.html)

- VPC - [AWS::EC2::VPC](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html)

- VPCCidrBlock - [AWS::EC2::VPCCidrBlock](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html)

- VPCDHCPOptionsAssociation - [AWS::EC2::VPCDHCPOptionsAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc-dhcp-options-assoc.html)

- VPCEndpoint - [AWS::EC2::VPCEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html)

- VPCEndpointConnectionNotification - [AWS::EC2::VPCEndpointConnectionNotification](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointconnectionnotification.html)

- VPCEndpointService - [AWS::EC2::VPCEndpointService](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservice.html)

- VPCEndpointServicePermissions - [AWS::EC2::VPCEndpointServicePermissions](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservicepermissions.html)

- VPCGatewayAttachment - [AWS::EC2::VPCGatewayAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc-gateway-attachment.html)

- VPCPeeringConnection - [AWS::EC2::VPCPeeringConnection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.html)

- VPNConnection - [AWS::EC2::VPNConnection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection.html)

- VPNConnectionRoute - [AWS::EC2::VPNConnectionRoute](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection-route.html)

- VPNGateway - [AWS::EC2::VPNGateway](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-gateway.html)

- VPNGatewayRoutePropagation - [AWS::EC2::VPNGatewayRoutePropagation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-gatewayrouteprop.html)

- Volume - [AWS::EC2::Volume](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html)

- VolumeAttachment - [AWS::EC2::VolumeAttachment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volumeattachment.html)

### Inspector

#### Module

`ingraph.aws.aws_inspector`

#### Resources

- AssessmentTarget - [AWS::Inspector::AssessmentTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttarget.html)

- AssessmentTemplate - [AWS::Inspector::AssessmentTemplate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html)

- ResourceGroup - [AWS::Inspector::ResourceGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-resourcegroup.html)

### AWS Batch

#### Module

`ingraph.aws.aws_batch`

#### Resources

- ComputeEnvironment - [AWS::Batch::ComputeEnvironment](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-computeenvironment.html)

- JobDefinition - [AWS::Batch::JobDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html)

- JobQueue - [AWS::Batch::JobQueue](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobqueue.html)

### AWS Cloud Map

#### Module

`ingraph.aws.aws_servicediscovery`

#### Resources

- HttpNamespace - [AWS::ServiceDiscovery::HttpNamespace](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html)

- Instance - [AWS::ServiceDiscovery::Instance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html)

- PrivateDnsNamespace - [AWS::ServiceDiscovery::PrivateDnsNamespace](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html)

- PublicDnsNamespace - [AWS::ServiceDiscovery::PublicDnsNamespace](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html)

- Service - [AWS::ServiceDiscovery::Service](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html)

### AccessAnalyzer

#### Module

`ingraph.aws.aws_accessanalyzer`

#### Resources

- Analyzer - [AWS::AccessAnalyzer::Analyzer](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html)

### IoTEvents

#### Module

`ingraph.aws.aws_iotevents`

#### Resources

- DetectorModel - [AWS::IoTEvents::DetectorModel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html)

- Input - [AWS::IoTEvents::Input](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html)

### AWS Glue

#### Module

`ingraph.aws.aws_glue`

#### Resources

- Classifier - [AWS::Glue::Classifier](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-classifier.html)

- Connection - [AWS::Glue::Connection](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-connection.html)

- Crawler - [AWS::Glue::Crawler](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html)

- DataCatalogEncryptionSettings - [AWS::Glue::DataCatalogEncryptionSettings](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-datacatalogencryptionsettings.html)

- Database - [AWS::Glue::Database](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-database.html)

- DevEndpoint - [AWS::Glue::DevEndpoint](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html)

- Job - [AWS::Glue::Job](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html)

- MLTransform - [AWS::Glue::MLTransform](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html)

- Partition - [AWS::Glue::Partition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-partition.html)

- SecurityConfiguration - [AWS::Glue::SecurityConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-securityconfiguration.html)

- Table - [AWS::Glue::Table](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.html)

- Trigger - [AWS::Glue::Trigger](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html)

- Workflow - [AWS::Glue::Workflow](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-workflow.html)

### AWS IoT Greengrass

#### Module

`ingraph.aws.aws_greengrass`

#### Resources

- ConnectorDefinition - [AWS::Greengrass::ConnectorDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html)

- ConnectorDefinitionVersion - [AWS::Greengrass::ConnectorDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinitionversion.html)

- CoreDefinition - [AWS::Greengrass::CoreDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html)

- CoreDefinitionVersion - [AWS::Greengrass::CoreDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinitionversion.html)

- DeviceDefinition - [AWS::Greengrass::DeviceDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html)

- DeviceDefinitionVersion - [AWS::Greengrass::DeviceDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinitionversion.html)

- FunctionDefinition - [AWS::Greengrass::FunctionDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html)

- FunctionDefinitionVersion - [AWS::Greengrass::FunctionDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html)

- Group - [AWS::Greengrass::Group](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html)

- GroupVersion - [AWS::Greengrass::GroupVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html)

- LoggerDefinition - [AWS::Greengrass::LoggerDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html)

- LoggerDefinitionVersion - [AWS::Greengrass::LoggerDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinitionversion.html)

- ResourceDefinition - [AWS::Greengrass::ResourceDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html)

- ResourceDefinitionVersion - [AWS::Greengrass::ResourceDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinitionversion.html)

- SubscriptionDefinition - [AWS::Greengrass::SubscriptionDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html)

- SubscriptionDefinitionVersion - [AWS::Greengrass::SubscriptionDefinitionVersion](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinitionversion.html)

### EFS

#### Module

`ingraph.aws.aws_efs`

#### Resources

- FileSystem - [AWS::EFS::FileSystem](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-filesystem.html)

- MountTarget - [AWS::EFS::MountTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html)

### Athena

#### Module

`ingraph.aws.aws_athena`

#### Resources

- NamedQuery - [AWS::Athena::NamedQuery](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html)

- WorkGroup - [AWS::Athena::WorkGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html)

### ECS

#### Module

`ingraph.aws.aws_ecs`

#### Resources

- Cluster - [AWS::ECS::Cluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html)

- PrimaryTaskSet - [AWS::ECS::PrimaryTaskSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-primarytaskset.html)

- Service - [AWS::ECS::Service](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html)

- TaskDefinition - [AWS::ECS::TaskDefinition](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html)

- TaskSet - [AWS::ECS::TaskSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html)

### Amazon Neptune

#### Module

`ingraph.aws.aws_neptune`

#### Resources

- DBCluster - [AWS::Neptune::DBCluster](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbcluster.html)

- DBClusterParameterGroup - [AWS::Neptune::DBClusterParameterGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbclusterparametergroup.html)

- DBInstance - [AWS::Neptune::DBInstance](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbinstance.html)

- DBParameterGroup - [AWS::Neptune::DBParameterGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbparametergroup.html)

- DBSubnetGroup - [AWS::Neptune::DBSubnetGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-neptune-dbsubnetgroup.html)

### KMS

#### Module

`ingraph.aws.aws_kms`

#### Resources

- Alias - [AWS::KMS::Alias](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-alias.html)

- Key - [AWS::KMS::Key](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html)

### CodeDeploy

#### Module

`ingraph.aws.aws_codedeploy`

#### Resources

- Application - [AWS::CodeDeploy::Application](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html)

- DeploymentConfig - [AWS::CodeDeploy::DeploymentConfig](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html)

- DeploymentGroup - [AWS::CodeDeploy::DeploymentGroup](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html)

### WAF

#### Module

`ingraph.aws.aws_waf`

#### Resources

- ByteMatchSet - [AWS::WAF::ByteMatchSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html)

- IPSet - [AWS::WAF::IPSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html)

- Rule - [AWS::WAF::Rule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html)

- SizeConstraintSet - [AWS::WAF::SizeConstraintSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html)

- SqlInjectionMatchSet - [AWS::WAF::SqlInjectionMatchSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html)

- WebACL - [AWS::WAF::WebACL](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html)

- XssMatchSet - [AWS::WAF::XssMatchSet](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html)

### Application Auto Scaling

#### Module

`ingraph.aws.aws_applicationautoscaling`

#### Resources

- ScalableTarget - [AWS::ApplicationAutoScaling::ScalableTarget](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html)

- ScalingPolicy - [AWS::ApplicationAutoScaling::ScalingPolicy](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html)

### CloudWatch

#### Module

`ingraph.aws.aws_cloudwatch`

#### Resources

- Alarm - [AWS::CloudWatch::Alarm](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html)

- AnomalyDetector - [AWS::CloudWatch::AnomalyDetector](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html)

- CompositeAlarm - [AWS::CloudWatch::CompositeAlarm](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html)

- Dashboard - [AWS::CloudWatch::Dashboard](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.html)

- InsightRule - [AWS::CloudWatch::InsightRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html)

### Certificate Manager

#### Module

`ingraph.aws.aws_certificatemanager`

#### Resources

- Certificate - [AWS::CertificateManager::Certificate](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html)

### Cassandra

#### Module

`ingraph.aws.aws_cassandra`

#### Resources

- Keyspace - [AWS::Cassandra::Keyspace](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html)

- Table - [AWS::Cassandra::Table](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html)

### CodeStar

#### Module

`ingraph.aws.aws_codestar`

#### Resources

- GitHubRepository - [AWS::CodeStar::GitHubRepository](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestar-githubrepository.html)

### NetworkManager

#### Module

`ingraph.aws.aws_networkmanager`

#### Resources

- CustomerGatewayAssociation - [AWS::NetworkManager::CustomerGatewayAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html)

- Device - [AWS::NetworkManager::Device](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html)

- GlobalNetwork - [AWS::NetworkManager::GlobalNetwork](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html)

- Link - [AWS::NetworkManager::Link](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html)

- LinkAssociation - [AWS::NetworkManager::LinkAssociation](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html)

- Site - [AWS::NetworkManager::Site](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html)

- TransitGatewayRegistration - [AWS::NetworkManager::TransitGatewayRegistration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html)

### Config

#### Module

`ingraph.aws.aws_config`

#### Resources

- AggregationAuthorization - [AWS::Config::AggregationAuthorization](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html)

- ConfigRule - [AWS::Config::ConfigRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html)

- ConfigurationAggregator - [AWS::Config::ConfigurationAggregator](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html)

- ConfigurationRecorder - [AWS::Config::ConfigurationRecorder](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html)

- ConformancePack - [AWS::Config::ConformancePack](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html)

- DeliveryChannel - [AWS::Config::DeliveryChannel](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html)

- OrganizationConfigRule - [AWS::Config::OrganizationConfigRule](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html)

- OrganizationConformancePack - [AWS::Config::OrganizationConformancePack](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html)

- RemediationConfiguration - [AWS::Config::RemediationConfiguration](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html)
