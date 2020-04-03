# Copyright 2020 Farzad Senart and Lionel Suss. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any, Dict, Final, List

from . import Tag

_NAMESPACE = "AWS::EC2"

class CapacityReservation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-capacityreservation.html"""

    Tenancy: Final[str]

    AvailableInstanceCount: Final[int]

    AvailabilityZone: Final[str]

    TotalInstanceCount: Final[int]

    InstanceType: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AvailabilityZone: str,
        InstanceCount: int,
        InstancePlatform: str,
        InstanceType: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EbsOptimized: bool = ...,
        EndDate: str = ...,
        EndDateType: str = ...,
        EphemeralStorage: bool = ...,
        InstanceMatchCriteria: str = ...,
        TagSpecifications: List["CapacityReservation.TagSpecification"] = ...,
        Tenancy: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class TagSpecification:
        def __init__(self, *, ResourceType: str = ..., Tags: List["Tag"] = ...): ...

class ClientVpnAuthorizationRule:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnauthorizationrule.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ClientVpnEndpointId: str,
        TargetNetworkCidr: str,
        AccessGroupId: str = ...,
        AuthorizeAllGroups: bool = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class ClientVpnEndpoint:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnendpoint.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        AuthenticationOptions: List["ClientVpnEndpoint.ClientAuthenticationRequest"],
        ClientCidrBlock: str,
        ConnectionLogOptions: "ClientVpnEndpoint.ConnectionLogOptions",
        ServerCertificateArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        DnsServers: List[str] = ...,
        SecurityGroupIds: List[str] = ...,
        SplitTunnel: bool = ...,
        TagSpecifications: List["ClientVpnEndpoint.TagSpecification"] = ...,
        TransportProtocol: str = ...,
        UpdateReplacePolicy: str = ...,
        VpcId: str = ...,
        VpnPort: int = ...
    ): ...
    class CertificateAuthenticationRequest:
        def __init__(self, *, ClientRootCertificateChainArn: str): ...
    class ClientAuthenticationRequest:
        def __init__(
            self,
            *,
            Type: str,
            ActiveDirectory: "ClientVpnEndpoint.DirectoryServiceAuthenticationRequest" = ...,
            MutualAuthentication: "ClientVpnEndpoint.CertificateAuthenticationRequest" = ...
        ): ...
    class ConnectionLogOptions:
        def __init__(
            self,
            *,
            Enabled: bool,
            CloudwatchLogGroup: str = ...,
            CloudwatchLogStream: str = ...
        ): ...
    class DirectoryServiceAuthenticationRequest:
        def __init__(self, *, DirectoryId: str): ...
    class TagSpecification:
        def __init__(self, *, ResourceType: str, Tags: List["Tag"]): ...

class ClientVpnRoute:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpnroute.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ClientVpnEndpointId: str,
        DestinationCidrBlock: str,
        TargetVpcSubnetId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class ClientVpnTargetNetworkAssociation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-clientvpntargetnetworkassociation.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ClientVpnEndpointId: str,
        SubnetId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class CustomerGateway:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-customer-gateway.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        BgpAsn: int,
        IpAddress: str,
        Type: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class DHCPOptions:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcp-options.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DomainName: str = ...,
        DomainNameServers: List[str] = ...,
        NetbiosNameServers: List[str] = ...,
        NetbiosNodeType: int = ...,
        NtpServers: List[str] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class EC2Fleet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        LaunchTemplateConfigs: List["EC2Fleet.FleetLaunchTemplateConfigRequest"],
        TargetCapacitySpecification: "EC2Fleet.TargetCapacitySpecificationRequest",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ExcessCapacityTerminationPolicy: str = ...,
        OnDemandOptions: "EC2Fleet.OnDemandOptionsRequest" = ...,
        ReplaceUnhealthyInstances: bool = ...,
        SpotOptions: "EC2Fleet.SpotOptionsRequest" = ...,
        TagSpecifications: List["EC2Fleet.TagSpecification"] = ...,
        TerminateInstancesWithExpiration: bool = ...,
        Type: str = ...,
        UpdateReplacePolicy: str = ...,
        ValidFrom: str = ...,
        ValidUntil: str = ...
    ): ...
    class CapacityReservationOptionsRequest:
        def __init__(self, *, UsageStrategy: str = ...): ...
    class FleetLaunchTemplateConfigRequest:
        def __init__(
            self,
            *,
            LaunchTemplateSpecification: "EC2Fleet.FleetLaunchTemplateSpecificationRequest" = ...,
            Overrides: List["EC2Fleet.FleetLaunchTemplateOverridesRequest"] = ...
        ): ...
    class FleetLaunchTemplateOverridesRequest:
        def __init__(
            self,
            *,
            AvailabilityZone: str = ...,
            InstanceType: str = ...,
            MaxPrice: str = ...,
            Placement: "EC2Fleet.Placement" = ...,
            Priority: float = ...,
            SubnetId: str = ...,
            WeightedCapacity: float = ...
        ): ...
    class FleetLaunchTemplateSpecificationRequest:
        def __init__(
            self,
            *,
            LaunchTemplateId: str = ...,
            LaunchTemplateName: str = ...,
            Version: str = ...
        ): ...
    class OnDemandOptionsRequest:
        def __init__(
            self,
            *,
            AllocationStrategy: str = ...,
            CapacityReservationOptions: "EC2Fleet.CapacityReservationOptionsRequest" = ...,
            MaxTotalPrice: str = ...,
            MinTargetCapacity: int = ...,
            SingleAvailabilityZone: bool = ...,
            SingleInstanceType: bool = ...
        ): ...
    class Placement:
        def __init__(
            self,
            *,
            Affinity: str = ...,
            AvailabilityZone: str = ...,
            GroupName: str = ...,
            HostId: str = ...,
            HostResourceGroupArn: str = ...,
            PartitionNumber: int = ...,
            SpreadDomain: str = ...,
            Tenancy: str = ...
        ): ...
    class SpotOptionsRequest:
        def __init__(
            self,
            *,
            AllocationStrategy: str = ...,
            InstanceInterruptionBehavior: str = ...,
            InstancePoolsToUseCount: int = ...,
            MaxTotalPrice: str = ...,
            MinTargetCapacity: int = ...,
            SingleAvailabilityZone: bool = ...,
            SingleInstanceType: bool = ...
        ): ...
    class TagSpecification:
        def __init__(self, *, ResourceType: str = ..., Tags: List["Tag"] = ...): ...
    class TargetCapacitySpecificationRequest:
        def __init__(
            self,
            *,
            TotalTargetCapacity: int,
            DefaultTargetCapacityType: str = ...,
            OnDemandTargetCapacity: int = ...,
            SpotTargetCapacity: int = ...
        ): ...

class EIP:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip.html"""

    AllocationId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Domain: str = ...,
        InstanceId: str = ...,
        PublicIpv4Pool: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class EIPAssociation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-eip-association.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        AllocationId: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EIP: str = ...,
        InstanceId: str = ...,
        NetworkInterfaceId: str = ...,
        PrivateIpAddress: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class EgressOnlyInternetGateway:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-egressonlyinternetgateway.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        VpcId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class FlowLog:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-flowlog.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ResourceId: str,
        ResourceType: str,
        TrafficType: str,
        DeletionPolicy: str = ...,
        DeliverLogsPermissionArn: str = ...,
        DependsOn: List[Any] = ...,
        LogDestination: str = ...,
        LogDestinationType: str = ...,
        LogGroupName: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class GatewayRouteTableAssociation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-gatewayroutetableassociation.html"""

    AssociationId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        GatewayId: str,
        RouteTableId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Host:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-host.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        AvailabilityZone: str,
        InstanceType: str,
        AutoPlacement: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        HostRecovery: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Instance:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html"""

    AvailabilityZone: Final[str]

    PrivateDnsName: Final[str]

    PrivateIp: Final[str]

    PublicDnsName: Final[str]

    PublicIp: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AdditionalInfo: str = ...,
        Affinity: str = ...,
        AvailabilityZone: str = ...,
        BlockDeviceMappings: List["Instance.BlockDeviceMapping"] = ...,
        CpuOptions: "Instance.CpuOptions" = ...,
        CreationPolicy: "Instance.CreationPolicy" = ...,
        CreditSpecification: "Instance.CreditSpecification" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DisableApiTermination: bool = ...,
        EbsOptimized: bool = ...,
        ElasticGpuSpecifications: List["Instance.ElasticGpuSpecification"] = ...,
        ElasticInferenceAccelerators: List[
            "Instance.ElasticInferenceAccelerator"
        ] = ...,
        HibernationOptions: "Instance.HibernationOptions" = ...,
        HostId: str = ...,
        HostResourceGroupArn: str = ...,
        IamInstanceProfile: str = ...,
        ImageId: str = ...,
        InstanceInitiatedShutdownBehavior: str = ...,
        InstanceType: str = ...,
        Ipv6AddressCount: int = ...,
        Ipv6Addresses: List["Instance.InstanceIpv6Address"] = ...,
        KernelId: str = ...,
        KeyName: str = ...,
        LaunchTemplate: "Instance.LaunchTemplateSpecification" = ...,
        LicenseSpecifications: List["Instance.LicenseSpecification"] = ...,
        Monitoring: bool = ...,
        NetworkInterfaces: List["Instance.NetworkInterface"] = ...,
        PlacementGroupName: str = ...,
        PrivateIpAddress: str = ...,
        RamdiskId: str = ...,
        SecurityGroupIds: List[str] = ...,
        SecurityGroups: List[str] = ...,
        SourceDestCheck: bool = ...,
        SsmAssociations: List["Instance.SsmAssociation"] = ...,
        SubnetId: str = ...,
        Tags: List["Tag"] = ...,
        Tenancy: str = ...,
        UpdateReplacePolicy: str = ...,
        UserData: str = ...,
        Volumes: List["Instance.Volume"] = ...
    ): ...
    class AssociationParameter:
        def __init__(self, *, Key: str, Value: List[str]): ...
    class BlockDeviceMapping:
        def __init__(
            self,
            *,
            DeviceName: str,
            Ebs: "Instance.Ebs" = ...,
            NoDevice: "Instance.NoDevice" = ...,
            VirtualName: str = ...
        ): ...
    class CpuOptions:
        def __init__(self, *, CoreCount: int = ..., ThreadsPerCore: int = ...): ...
    class CreationPolicy:
        def __init__(self, *, ResourceSignal: "Instance.ResourceSignal" = ...): ...
    class CreditSpecification:
        def __init__(self, *, CPUCredits: str = ...): ...
    class Ebs:
        def __init__(
            self,
            *,
            DeleteOnTermination: bool = ...,
            Encrypted: bool = ...,
            Iops: int = ...,
            KmsKeyId: str = ...,
            SnapshotId: str = ...,
            VolumeSize: int = ...,
            VolumeType: str = ...
        ): ...
    class ElasticGpuSpecification:
        def __init__(self, *, Type: str): ...
    class ElasticInferenceAccelerator:
        def __init__(self, *, Type: str, Count: int = ...): ...
    class HibernationOptions:
        def __init__(self, *, Configured: bool = ...): ...
    class InstanceIpv6Address:
        def __init__(self, *, Ipv6Address: str): ...
    class LaunchTemplateSpecification:
        def __init__(
            self,
            *,
            Version: str,
            LaunchTemplateId: str = ...,
            LaunchTemplateName: str = ...
        ): ...
    class LicenseSpecification:
        def __init__(self, *, LicenseConfigurationArn: str): ...
    class NetworkInterface:
        def __init__(
            self,
            *,
            DeviceIndex: str,
            AssociatePublicIpAddress: bool = ...,
            DeleteOnTermination: bool = ...,
            Description: str = ...,
            GroupSet: List[str] = ...,
            Ipv6AddressCount: int = ...,
            Ipv6Addresses: List["Instance.InstanceIpv6Address"] = ...,
            NetworkInterfaceId: str = ...,
            PrivateIpAddress: str = ...,
            PrivateIpAddresses: List["Instance.PrivateIpAddressSpecification"] = ...,
            SecondaryPrivateIpAddressCount: int = ...,
            SubnetId: str = ...
        ): ...
    class NoDevice:
        def __init__(self) -> None: ...
    class PrivateIpAddressSpecification:
        def __init__(self, *, Primary: bool, PrivateIpAddress: str): ...
    class ResourceSignal:
        def __init__(self, *, Count: int = ..., Timeout: str = ...): ...
    class SsmAssociation:
        def __init__(
            self,
            *,
            DocumentName: str,
            AssociationParameters: List["Instance.AssociationParameter"] = ...
        ): ...
    class Volume:
        def __init__(self, *, Device: str, VolumeId: str): ...

class InternetGateway:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-internetgateway.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class LaunchTemplate:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html"""

    LatestVersionNumber: Final[str]

    DefaultVersionNumber: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        LaunchTemplateData: "LaunchTemplate.LaunchTemplateData" = ...,
        LaunchTemplateName: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class BlockDeviceMapping:
        def __init__(
            self,
            *,
            DeviceName: str = ...,
            Ebs: "LaunchTemplate.Ebs" = ...,
            NoDevice: str = ...,
            VirtualName: str = ...
        ): ...
    class CapacityReservationPreference:
        def __init__(self) -> None: ...
    class CapacityReservationSpecification:
        def __init__(
            self,
            *,
            CapacityReservationPreference: "LaunchTemplate.CapacityReservationPreference" = ...,
            CapacityReservationTarget: "LaunchTemplate.CapacityReservationTarget" = ...
        ): ...
    class CapacityReservationTarget:
        def __init__(self, *, CapacityReservationId: str = ...): ...
    class CpuOptions:
        def __init__(self, *, CoreCount: int = ..., ThreadsPerCore: int = ...): ...
    class CreditSpecification:
        def __init__(self, *, CpuCredits: str = ...): ...
    class Ebs:
        def __init__(
            self,
            *,
            DeleteOnTermination: bool = ...,
            Encrypted: bool = ...,
            Iops: int = ...,
            KmsKeyId: str = ...,
            SnapshotId: str = ...,
            VolumeSize: int = ...,
            VolumeType: str = ...
        ): ...
    class ElasticGpuSpecification:
        def __init__(self, *, Type: str = ...): ...
    class HibernationOptions:
        def __init__(self, *, Configured: bool = ...): ...
    class IamInstanceProfile:
        def __init__(self, *, Arn: str = ..., Name: str = ...): ...
    class InstanceMarketOptions:
        def __init__(
            self,
            *,
            MarketType: str = ...,
            SpotOptions: "LaunchTemplate.SpotOptions" = ...
        ): ...
    class Ipv6Add:
        def __init__(self, *, Ipv6Address: str = ...): ...
    class LaunchTemplateData:
        def __init__(
            self,
            *,
            BlockDeviceMappings: List["LaunchTemplate.BlockDeviceMapping"] = ...,
            CapacityReservationSpecification: "LaunchTemplate.CapacityReservationSpecification" = ...,
            CpuOptions: "LaunchTemplate.CpuOptions" = ...,
            CreditSpecification: "LaunchTemplate.CreditSpecification" = ...,
            DisableApiTermination: bool = ...,
            EbsOptimized: bool = ...,
            ElasticGpuSpecifications: List[
                "LaunchTemplate.ElasticGpuSpecification"
            ] = ...,
            ElasticInferenceAccelerators: List[
                "LaunchTemplate.LaunchTemplateElasticInferenceAccelerator"
            ] = ...,
            HibernationOptions: "LaunchTemplate.HibernationOptions" = ...,
            IamInstanceProfile: "LaunchTemplate.IamInstanceProfile" = ...,
            ImageId: str = ...,
            InstanceInitiatedShutdownBehavior: str = ...,
            InstanceMarketOptions: "LaunchTemplate.InstanceMarketOptions" = ...,
            InstanceType: str = ...,
            KernelId: str = ...,
            KeyName: str = ...,
            LicenseSpecifications: List["LaunchTemplate.LicenseSpecification"] = ...,
            MetadataOptions: "LaunchTemplate.MetadataOptions" = ...,
            Monitoring: "LaunchTemplate.Monitoring" = ...,
            NetworkInterfaces: List["LaunchTemplate.NetworkInterface"] = ...,
            Placement: "LaunchTemplate.Placement" = ...,
            RamDiskId: str = ...,
            SecurityGroupIds: List[str] = ...,
            SecurityGroups: List[str] = ...,
            TagSpecifications: List["LaunchTemplate.TagSpecification"] = ...,
            UserData: str = ...
        ): ...
    class LaunchTemplateElasticInferenceAccelerator:
        def __init__(self, *, Count: int = ..., Type: str = ...): ...
    class LicenseSpecification:
        def __init__(self, *, LicenseConfigurationArn: str = ...): ...
    class MetadataOptions:
        def __init__(
            self,
            *,
            HttpEndpoint: str = ...,
            HttpPutResponseHopLimit: int = ...,
            HttpTokens: str = ...
        ): ...
    class Monitoring:
        def __init__(self, *, Enabled: bool = ...): ...
    class NetworkInterface:
        def __init__(
            self,
            *,
            AssociatePublicIpAddress: bool = ...,
            DeleteOnTermination: bool = ...,
            Description: str = ...,
            DeviceIndex: int = ...,
            Groups: List[str] = ...,
            InterfaceType: str = ...,
            Ipv6AddressCount: int = ...,
            Ipv6Addresses: List["LaunchTemplate.Ipv6Add"] = ...,
            NetworkInterfaceId: str = ...,
            PrivateIpAddress: str = ...,
            PrivateIpAddresses: List["LaunchTemplate.PrivateIpAdd"] = ...,
            SecondaryPrivateIpAddressCount: int = ...,
            SubnetId: str = ...
        ): ...
    class Placement:
        def __init__(
            self,
            *,
            Affinity: str = ...,
            AvailabilityZone: str = ...,
            GroupName: str = ...,
            HostId: str = ...,
            HostResourceGroupArn: str = ...,
            PartitionNumber: int = ...,
            SpreadDomain: str = ...,
            Tenancy: str = ...
        ): ...
    class PrivateIpAdd:
        def __init__(self, *, Primary: bool = ..., PrivateIpAddress: str = ...): ...
    class SpotOptions:
        def __init__(
            self,
            *,
            BlockDurationMinutes: int = ...,
            InstanceInterruptionBehavior: str = ...,
            MaxPrice: str = ...,
            SpotInstanceType: str = ...,
            ValidUntil: str = ...
        ): ...
    class TagSpecification:
        def __init__(self, *, ResourceType: str = ..., Tags: List["Tag"] = ...): ...

class LocalGatewayRoute:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroute.html"""

    State: Final[str]

    Type: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DestinationCidrBlock: str,
        LocalGatewayRouteTableId: str,
        LocalGatewayVirtualInterfaceGroupId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class LocalGatewayRouteTableVPCAssociation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetablevpcassociation.html"""

    LocalGatewayId: Final[str]

    LocalGatewayRouteTableVpcAssociationId: Final[str]

    State: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        LocalGatewayRouteTableId: str,
        VpcId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: "LocalGatewayRouteTableVPCAssociation.Tags" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Tags:
        def __init__(self, *, Tags: List["Tag"] = ...): ...

class NatGateway:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-natgateway.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        AllocationId: str,
        SubnetId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class NetworkAcl:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        VpcId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class NetworkAclEntry:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        NetworkAclId: str,
        Protocol: int,
        RuleAction: str,
        RuleNumber: int,
        CidrBlock: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Egress: bool = ...,
        Icmp: "NetworkAclEntry.Icmp" = ...,
        Ipv6CidrBlock: str = ...,
        PortRange: "NetworkAclEntry.PortRange" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Icmp:
        def __init__(self, *, Code: int = ..., Type: int = ...): ...
    class PortRange:
        def __init__(self, *, From: int = ..., To: int = ...): ...

class NetworkInterface:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface.html"""

    PrimaryPrivateIpAddress: Final[str]

    SecondaryPrivateIpAddresses: Final[List[str]]

    Ref: Final[str]
    def __init__(
        self,
        *,
        SubnetId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        GroupSet: List[str] = ...,
        InterfaceType: str = ...,
        Ipv6AddressCount: int = ...,
        Ipv6Addresses: "NetworkInterface.InstanceIpv6Address" = ...,
        PrivateIpAddress: str = ...,
        PrivateIpAddresses: List[
            "NetworkInterface.PrivateIpAddressSpecification"
        ] = ...,
        SecondaryPrivateIpAddressCount: int = ...,
        SourceDestCheck: bool = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class InstanceIpv6Address:
        def __init__(self, *, Ipv6Address: str): ...
    class PrivateIpAddressSpecification:
        def __init__(self, *, Primary: bool, PrivateIpAddress: str): ...

class NetworkInterfaceAttachment:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-interface-attachment.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeviceIndex: str,
        InstanceId: str,
        NetworkInterfaceId: str,
        DeleteOnTermination: bool = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class NetworkInterfacePermission:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkinterfacepermission.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        AwsAccountId: str,
        NetworkInterfaceId: str,
        Permission: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class PlacementGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-placementgroup.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Strategy: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Route:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        RouteTableId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DestinationCidrBlock: str = ...,
        DestinationIpv6CidrBlock: str = ...,
        EgressOnlyInternetGatewayId: str = ...,
        GatewayId: str = ...,
        InstanceId: str = ...,
        NatGatewayId: str = ...,
        NetworkInterfaceId: str = ...,
        TransitGatewayId: str = ...,
        UpdateReplacePolicy: str = ...,
        VpcPeeringConnectionId: str = ...
    ): ...

class RouteTable:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-route-table.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        VpcId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class SecurityGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html"""

    GroupId: Final[str]

    VpcId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        GroupDescription: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        GroupName: str = ...,
        SecurityGroupEgress: List["SecurityGroup.Egress"] = ...,
        SecurityGroupIngress: List["SecurityGroup.Ingress"] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        VpcId: str = ...
    ): ...
    class Egress:
        def __init__(
            self,
            *,
            IpProtocol: str,
            CidrIp: str = ...,
            CidrIpv6: str = ...,
            Description: str = ...,
            DestinationPrefixListId: str = ...,
            DestinationSecurityGroupId: str = ...,
            FromPort: int = ...,
            ToPort: int = ...
        ): ...
    class Ingress:
        def __init__(
            self,
            *,
            IpProtocol: str,
            CidrIp: str = ...,
            CidrIpv6: str = ...,
            Description: str = ...,
            FromPort: int = ...,
            SourcePrefixListId: str = ...,
            SourceSecurityGroupId: str = ...,
            SourceSecurityGroupName: str = ...,
            SourceSecurityGroupOwnerId: str = ...,
            ToPort: int = ...
        ): ...

class SecurityGroupEgress:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-security-group-egress.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        GroupId: str,
        IpProtocol: str,
        CidrIp: str = ...,
        CidrIpv6: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        DestinationPrefixListId: str = ...,
        DestinationSecurityGroupId: str = ...,
        FromPort: int = ...,
        ToPort: int = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class SecurityGroupIngress:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group-ingress.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        IpProtocol: str,
        CidrIp: str = ...,
        CidrIpv6: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        FromPort: int = ...,
        GroupId: str = ...,
        GroupName: str = ...,
        SourcePrefixListId: str = ...,
        SourceSecurityGroupId: str = ...,
        SourceSecurityGroupName: str = ...,
        SourceSecurityGroupOwnerId: str = ...,
        ToPort: int = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class SpotFleet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-spotfleet.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        SpotFleetRequestConfigData: "SpotFleet.SpotFleetRequestConfigData",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class BlockDeviceMapping:
        def __init__(
            self,
            *,
            DeviceName: str,
            Ebs: "SpotFleet.EbsBlockDevice" = ...,
            NoDevice: str = ...,
            VirtualName: str = ...
        ): ...
    class ClassicLoadBalancer:
        def __init__(self, *, Name: str): ...
    class ClassicLoadBalancersConfig:
        def __init__(
            self, *, ClassicLoadBalancers: List["SpotFleet.ClassicLoadBalancer"]
        ): ...
    class EbsBlockDevice:
        def __init__(
            self,
            *,
            DeleteOnTermination: bool = ...,
            Encrypted: bool = ...,
            Iops: int = ...,
            SnapshotId: str = ...,
            VolumeSize: int = ...,
            VolumeType: str = ...
        ): ...
    class FleetLaunchTemplateSpecification:
        def __init__(
            self,
            *,
            Version: str,
            LaunchTemplateId: str = ...,
            LaunchTemplateName: str = ...
        ): ...
    class GroupIdentifier:
        def __init__(self, *, GroupId: str): ...
    class IamInstanceProfileSpecification:
        def __init__(self, *, Arn: str = ...): ...
    class InstanceIpv6Address:
        def __init__(self, *, Ipv6Address: str): ...
    class InstanceNetworkInterfaceSpecification:
        def __init__(
            self,
            *,
            AssociatePublicIpAddress: bool = ...,
            DeleteOnTermination: bool = ...,
            Description: str = ...,
            DeviceIndex: int = ...,
            Groups: List[str] = ...,
            Ipv6AddressCount: int = ...,
            Ipv6Addresses: List["SpotFleet.InstanceIpv6Address"] = ...,
            NetworkInterfaceId: str = ...,
            PrivateIpAddresses: List["SpotFleet.PrivateIpAddressSpecification"] = ...,
            SecondaryPrivateIpAddressCount: int = ...,
            SubnetId: str = ...
        ): ...
    class LaunchTemplateConfig:
        def __init__(
            self,
            *,
            LaunchTemplateSpecification: "SpotFleet.FleetLaunchTemplateSpecification" = ...,
            Overrides: List["SpotFleet.LaunchTemplateOverrides"] = ...
        ): ...
    class LaunchTemplateOverrides:
        def __init__(
            self,
            *,
            AvailabilityZone: str = ...,
            InstanceType: str = ...,
            SpotPrice: str = ...,
            SubnetId: str = ...,
            WeightedCapacity: float = ...
        ): ...
    class LoadBalancersConfig:
        def __init__(
            self,
            *,
            ClassicLoadBalancersConfig: "SpotFleet.ClassicLoadBalancersConfig" = ...,
            TargetGroupsConfig: "SpotFleet.TargetGroupsConfig" = ...
        ): ...
    class PrivateIpAddressSpecification:
        def __init__(self, *, PrivateIpAddress: str, Primary: bool = ...): ...
    class SpotFleetLaunchSpecification:
        def __init__(
            self,
            *,
            ImageId: str,
            InstanceType: str,
            BlockDeviceMappings: List["SpotFleet.BlockDeviceMapping"] = ...,
            EbsOptimized: bool = ...,
            IamInstanceProfile: "SpotFleet.IamInstanceProfileSpecification" = ...,
            KernelId: str = ...,
            KeyName: str = ...,
            Monitoring: "SpotFleet.SpotFleetMonitoring" = ...,
            NetworkInterfaces: List[
                "SpotFleet.InstanceNetworkInterfaceSpecification"
            ] = ...,
            Placement: "SpotFleet.SpotPlacement" = ...,
            RamdiskId: str = ...,
            SecurityGroups: List["SpotFleet.GroupIdentifier"] = ...,
            SpotPrice: str = ...,
            SubnetId: str = ...,
            TagSpecifications: List["SpotFleet.SpotFleetTagSpecification"] = ...,
            UserData: str = ...,
            WeightedCapacity: float = ...
        ): ...
    class SpotFleetMonitoring:
        def __init__(self, *, Enabled: bool = ...): ...
    class SpotFleetRequestConfigData:
        def __init__(
            self,
            *,
            IamFleetRole: str,
            TargetCapacity: int,
            AllocationStrategy: str = ...,
            ExcessCapacityTerminationPolicy: str = ...,
            InstanceInterruptionBehavior: str = ...,
            LaunchSpecifications: List["SpotFleet.SpotFleetLaunchSpecification"] = ...,
            LaunchTemplateConfigs: List["SpotFleet.LaunchTemplateConfig"] = ...,
            LoadBalancersConfig: "SpotFleet.LoadBalancersConfig" = ...,
            ReplaceUnhealthyInstances: bool = ...,
            SpotPrice: str = ...,
            TerminateInstancesWithExpiration: bool = ...,
            Type: str = ...,
            ValidFrom: str = ...,
            ValidUntil: str = ...
        ): ...
    class SpotFleetTagSpecification:
        def __init__(self, *, ResourceType: str = ..., Tags: List["Tag"] = ...): ...
    class SpotPlacement:
        def __init__(
            self,
            *,
            AvailabilityZone: str = ...,
            GroupName: str = ...,
            Tenancy: str = ...
        ): ...
    class TargetGroup:
        def __init__(self, *, Arn: str): ...
    class TargetGroupsConfig:
        def __init__(self, *, TargetGroups: List["SpotFleet.TargetGroup"]): ...

class Subnet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet.html"""

    AvailabilityZone: Final[str]

    Ipv6CidrBlocks: Final[List[str]]

    NetworkAclAssociationId: Final[str]

    VpcId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        CidrBlock: str,
        VpcId: str,
        AssignIpv6AddressOnCreation: bool = ...,
        AvailabilityZone: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Ipv6CidrBlock: str = ...,
        MapPublicIpOnLaunch: bool = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class SubnetCidrBlock:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnetcidrblock.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Ipv6CidrBlock: str,
        SubnetId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class SubnetNetworkAclAssociation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet-network-acl-assoc.html"""

    AssociationId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        NetworkAclId: str,
        SubnetId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class SubnetRouteTableAssociation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-subnet-route-table-assoc.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        RouteTableId: str,
        SubnetId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class TrafficMirrorFilter:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilter.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        NetworkServices: List[str] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class TrafficMirrorFilterRule:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorfilterrule.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DestinationCidrBlock: str,
        RuleAction: str,
        RuleNumber: int,
        SourceCidrBlock: str,
        TrafficDirection: str,
        TrafficMirrorFilterId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        DestinationPortRange: "TrafficMirrorFilterRule.TrafficMirrorPortRange" = ...,
        Protocol: int = ...,
        SourcePortRange: "TrafficMirrorFilterRule.TrafficMirrorPortRange" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class TrafficMirrorPortRange:
        def __init__(self, *, FromPort: int, ToPort: int): ...

class TrafficMirrorSession:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrorsession.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        NetworkInterfaceId: str,
        SessionNumber: int,
        TrafficMirrorFilterId: str,
        TrafficMirrorTargetId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        PacketLength: int = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        VirtualNetworkId: int = ...
    ): ...

class TrafficMirrorTarget:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-trafficmirrortarget.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        NetworkInterfaceId: str = ...,
        NetworkLoadBalancerArn: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class TransitGateway:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgateway.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        AmazonSideAsn: int = ...,
        AutoAcceptSharedAttachments: str = ...,
        DefaultRouteTableAssociation: str = ...,
        DefaultRouteTablePropagation: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        DnsSupport: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        VpnEcmpSupport: str = ...
    ): ...

class TransitGatewayAttachment:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayattachment.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        SubnetIds: List[str],
        TransitGatewayId: str,
        VpcId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class TransitGatewayRoute:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroute.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        TransitGatewayRouteTableId: str,
        Blackhole: bool = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DestinationCidrBlock: str = ...,
        TransitGatewayAttachmentId: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class TransitGatewayRouteTable:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetable.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        TransitGatewayId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class TransitGatewayRouteTableAssociation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetableassociation.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        TransitGatewayAttachmentId: str,
        TransitGatewayRouteTableId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class TransitGatewayRouteTablePropagation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-transitgatewayroutetablepropagation.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        TransitGatewayAttachmentId: str,
        TransitGatewayRouteTableId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class VPC:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html"""

    CidrBlock: Final[str]

    CidrBlockAssociations: Final[List[str]]

    DefaultNetworkAcl: Final[str]

    DefaultSecurityGroup: Final[str]

    Ipv6CidrBlocks: Final[List[str]]

    Ref: Final[str]
    def __init__(
        self,
        *,
        CidrBlock: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EnableDnsHostnames: bool = ...,
        EnableDnsSupport: bool = ...,
        InstanceTenancy: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class VPCCidrBlock:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpccidrblock.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        VpcId: str,
        AmazonProvidedIpv6CidrBlock: bool = ...,
        CidrBlock: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class VPCDHCPOptionsAssociation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc-dhcp-options-assoc.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DhcpOptionsId: str,
        VpcId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class VPCEndpoint:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html"""

    CreationTimestamp: Final[str]

    DnsEntries: Final[List[str]]

    NetworkInterfaceIds: Final[List[str]]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ServiceName: str,
        VpcId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        PolicyDocument: Any = ...,
        PrivateDnsEnabled: bool = ...,
        RouteTableIds: List[str] = ...,
        SecurityGroupIds: List[str] = ...,
        SubnetIds: List[str] = ...,
        UpdateReplacePolicy: str = ...,
        VpcEndpointType: str = ...
    ): ...

class VPCEndpointConnectionNotification:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointconnectionnotification.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ConnectionEvents: List[str],
        ConnectionNotificationArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ServiceId: str = ...,
        UpdateReplacePolicy: str = ...,
        VPCEndpointId: str = ...
    ): ...

class VPCEndpointService:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservice.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        NetworkLoadBalancerArns: List[str],
        AcceptanceRequired: bool = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class VPCEndpointServicePermissions:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpointservicepermissions.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ServiceId: str,
        AllowedPrincipals: List[str] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class VPCGatewayAttachment:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc-gateway-attachment.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        VpcId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        InternetGatewayId: str = ...,
        UpdateReplacePolicy: str = ...,
        VpnGatewayId: str = ...
    ): ...

class VPCPeeringConnection:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcpeeringconnection.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        PeerVpcId: str,
        VpcId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        PeerOwnerId: str = ...,
        PeerRegion: str = ...,
        PeerRoleArn: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class VPNConnection:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        CustomerGatewayId: str,
        Type: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        StaticRoutesOnly: bool = ...,
        Tags: List["Tag"] = ...,
        TransitGatewayId: str = ...,
        UpdateReplacePolicy: str = ...,
        VpnGatewayId: str = ...,
        VpnTunnelOptionsSpecifications: List[
            "VPNConnection.VpnTunnelOptionsSpecification"
        ] = ...
    ): ...
    class VpnTunnelOptionsSpecification:
        def __init__(self, *, PreSharedKey: str = ..., TunnelInsideCidr: str = ...): ...

class VPNConnectionRoute:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-connection-route.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DestinationCidrBlock: str,
        VpnConnectionId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class VPNGateway:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-gateway.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Type: str,
        AmazonSideAsn: int = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class VPNGatewayRoutePropagation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpn-gatewayrouteprop.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        RouteTableIds: List[str],
        VpnGatewayId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Volume:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volume.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        AvailabilityZone: str,
        AutoEnableIO: bool = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Encrypted: bool = ...,
        Iops: int = ...,
        KmsKeyId: str = ...,
        MultiAttachEnabled: bool = ...,
        Size: int = ...,
        SnapshotId: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        VolumeType: str = ...
    ): ...

class VolumeAttachment:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-ebs-volumeattachment.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Device: str,
        InstanceId: str,
        VolumeId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
