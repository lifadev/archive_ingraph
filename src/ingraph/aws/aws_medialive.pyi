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

_NAMESPACE = "AWS::MediaLive"

class Channel:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-channel.html"""

    Arn: Final[str]

    Inputs: Final[List[str]]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ChannelClass: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Destinations: List["Channel.OutputDestination"] = ...,
        EncoderSettings: Any = ...,
        InputAttachments: List["Channel.InputAttachment"] = ...,
        InputSpecification: "Channel.InputSpecification" = ...,
        LogLevel: str = ...,
        Name: str = ...,
        RoleArn: str = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AribSourceSettings:
        def __init__(self) -> None: ...
    class AudioLanguageSelection:
        def __init__(
            self, *, LanguageCode: str = ..., LanguageSelectionPolicy: str = ...
        ): ...
    class AudioPidSelection:
        def __init__(self, *, Pid: int = ...): ...
    class AudioSelector:
        def __init__(
            self,
            *,
            Name: str = ...,
            SelectorSettings: "Channel.AudioSelectorSettings" = ...
        ): ...
    class AudioSelectorSettings:
        def __init__(
            self,
            *,
            AudioLanguageSelection: "Channel.AudioLanguageSelection" = ...,
            AudioPidSelection: "Channel.AudioPidSelection" = ...
        ): ...
    class CaptionSelector:
        def __init__(
            self,
            *,
            LanguageCode: str = ...,
            Name: str = ...,
            SelectorSettings: "Channel.CaptionSelectorSettings" = ...
        ): ...
    class CaptionSelectorSettings:
        def __init__(
            self,
            *,
            AribSourceSettings: "Channel.AribSourceSettings" = ...,
            DvbSubSourceSettings: "Channel.DvbSubSourceSettings" = ...,
            EmbeddedSourceSettings: "Channel.EmbeddedSourceSettings" = ...,
            Scte20SourceSettings: "Channel.Scte20SourceSettings" = ...,
            Scte27SourceSettings: "Channel.Scte27SourceSettings" = ...,
            TeletextSourceSettings: "Channel.TeletextSourceSettings" = ...
        ): ...
    class DvbSubSourceSettings:
        def __init__(self, *, Pid: int = ...): ...
    class EmbeddedSourceSettings:
        def __init__(
            self,
            *,
            Convert608To708: str = ...,
            Scte20Detection: str = ...,
            Source608ChannelNumber: int = ...,
            Source608TrackNumber: int = ...
        ): ...
    class HlsInputSettings:
        def __init__(
            self,
            *,
            Bandwidth: int = ...,
            BufferSegments: int = ...,
            Retries: int = ...,
            RetryInterval: int = ...
        ): ...
    class InputAttachment:
        def __init__(
            self,
            *,
            InputAttachmentName: str = ...,
            InputId: str = ...,
            InputSettings: "Channel.InputSettings" = ...
        ): ...
    class InputSettings:
        def __init__(
            self,
            *,
            AudioSelectors: List["Channel.AudioSelector"] = ...,
            CaptionSelectors: List["Channel.CaptionSelector"] = ...,
            DeblockFilter: str = ...,
            DenoiseFilter: str = ...,
            FilterStrength: int = ...,
            InputFilter: str = ...,
            NetworkInputSettings: "Channel.NetworkInputSettings" = ...,
            SourceEndBehavior: str = ...,
            VideoSelector: "Channel.VideoSelector" = ...
        ): ...
    class InputSpecification:
        def __init__(
            self, *, Codec: str = ..., MaximumBitrate: str = ..., Resolution: str = ...
        ): ...
    class MediaPackageOutputDestinationSettings:
        def __init__(self, *, ChannelId: str = ...): ...
    class MultiplexProgramChannelDestinationSettings:
        def __init__(self, *, MultiplexId: str = ..., ProgramName: str = ...): ...
    class NetworkInputSettings:
        def __init__(
            self,
            *,
            HlsInputSettings: "Channel.HlsInputSettings" = ...,
            ServerValidation: str = ...
        ): ...
    class OutputDestination:
        def __init__(
            self,
            *,
            Id: str = ...,
            MediaPackageSettings: List[
                "Channel.MediaPackageOutputDestinationSettings"
            ] = ...,
            MultiplexSettings: "Channel.MultiplexProgramChannelDestinationSettings" = ...,
            Settings: List["Channel.OutputDestinationSettings"] = ...
        ): ...
    class OutputDestinationSettings:
        def __init__(
            self,
            *,
            PasswordParam: str = ...,
            StreamName: str = ...,
            Url: str = ...,
            Username: str = ...
        ): ...
    class Scte20SourceSettings:
        def __init__(
            self, *, Convert608To708: str = ..., Source608ChannelNumber: int = ...
        ): ...
    class Scte27SourceSettings:
        def __init__(self, *, Pid: int = ...): ...
    class TeletextSourceSettings:
        def __init__(self, *, PageNumber: str = ...): ...
    class VideoSelector:
        def __init__(
            self,
            *,
            ColorSpace: str = ...,
            ColorSpaceUsage: str = ...,
            SelectorSettings: "Channel.VideoSelectorSettings" = ...
        ): ...
    class VideoSelectorPid:
        def __init__(self, *, Pid: int = ...): ...
    class VideoSelectorProgramId:
        def __init__(self, *, ProgramId: int = ...): ...
    class VideoSelectorSettings:
        def __init__(
            self,
            *,
            VideoSelectorPid: "Channel.VideoSelectorPid" = ...,
            VideoSelectorProgramId: "Channel.VideoSelectorProgramId" = ...
        ): ...

class Input:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-input.html"""

    Destinations: Final[List[str]]

    Arn: Final[str]

    Sources: Final[List[str]]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Destinations: List["Input.InputDestinationRequest"] = ...,
        InputSecurityGroups: List[str] = ...,
        MediaConnectFlows: List["Input.MediaConnectFlowRequest"] = ...,
        Name: str = ...,
        RoleArn: str = ...,
        Sources: List["Input.InputSourceRequest"] = ...,
        Tags: Any = ...,
        Type: str = ...,
        UpdateReplacePolicy: str = ...,
        Vpc: "Input.InputVpcRequest" = ...
    ): ...
    class InputDestinationRequest:
        def __init__(self, *, StreamName: str = ...): ...
    class InputSourceRequest:
        def __init__(
            self, *, PasswordParam: str = ..., Url: str = ..., Username: str = ...
        ): ...
    class InputVpcRequest:
        def __init__(
            self, *, SecurityGroupIds: List[str] = ..., SubnetIds: List[str] = ...
        ): ...
    class MediaConnectFlowRequest:
        def __init__(self, *, FlowArn: str = ...): ...

class InputSecurityGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-inputsecuritygroup.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...,
        WhitelistRules: List["InputSecurityGroup.InputWhitelistRuleCidr"] = ...
    ): ...
    class InputWhitelistRuleCidr:
        def __init__(self, *, Cidr: str = ...): ...
