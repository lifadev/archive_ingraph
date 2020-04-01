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

import base64
import hashlib
import io
from dataclasses import dataclass
from pathlib import Path
from typing import Any, ClassVar, Mapping, Optional, Sequence, Set, Tuple, cast

import networkx as nx
from ruamel.yaml import YAML, Representer, ScalarNode

from . import core


def encode_cfn(graph: nx.Graph) -> Tuple[str, Mapping[str, Path]]:
    template: Any = dict(AWSTemplateFormatVersion="2010-09-09")

    assets: Set[core.Asset] = set()
    for node in graph:
        assets.update(node.assets)
    if assets:
        template["Parameters"] = dict(
            AssetsS3Bucket=dict(Type="String"), AssetsS3Prefix=dict(Type="String"),
        )

    if params := core.getparameters(graph):
        template.setdefault("Parameters", {}).update(
            {_getidn(k): _getparam(v) for k, v in params.items()}
        )

    nodes = [node for node in graph if isinstance(node.resource, core.NativeResource)]
    if not nodes:
        raise TypeError("at least one AWS resource must be provided")
    resources = template["Resources"] = cast(Any, {})
    for node in nodes:
        resource = resources[_getnidn(node)] = dict(Type=node.resource._ig_kind)
        if props := _t(node.resource._ig_data):
            resource["Properties"] = props
        if deps := node.resource._ig_deps:
            resource["DependsOn"] = [_getnidn(d._ig_node) for d in deps]

    if outputs := core.getoutputs(graph):
        template["Outputs"] = {_getidn(k): _getoutput(v) for k, v in outputs.items()}

    yaml = YAML()
    for t in (
        MultilineStr,
        GetAtt,
        Join,
        Ref,
        RefValue,
        Select,
        Split,
        Sub,
        CIDR,
    ):
        yaml.register_class(t)

    stream = io.BytesIO()
    YAML().dump(template, stream)

    return (
        stream.getvalue().decode("utf-8"),
        {asset._ig_hash: asset._ig_path for asset in assets},
    )


def _getnidn(node: core.Node) -> str:
    data = cast(core.NativeResource, node.resource)
    pre = "-".join([name for name in node.lineage] + [data._ig_kind])
    dig = hashlib.sha1(pre.encode("utf-8")).digest()[:5]
    idn = base64.b32encode(dig).decode("utf-8").upper()
    name = "".join([name.title().replace("_", "") for name in node.lineage[1:]])
    return (name + idn)[-255:]


def _getidn(orig: str) -> str:
    return orig.title().replace("_", "")


def _getaidn(orig: str) -> str:
    return orig.rstrip("_").replace("_", ".")


def _getparam(info: core.Parameter) -> Any:
    typ: str
    if isinstance(info, core.String):
        typ = "String"
    elif isinstance(info, core.Number):
        typ = "Number"
    elif isinstance(info, core.LISTS[core.String]):
        typ = "CommaDelimitedList"
    elif isinstance(info, core.LISTS[core.Number]):
        typ = "List<Number>"
    res = dict(Type=typ)
    defl = info._ig_default
    if defl is None:
        return res
    defl = defl._ig_value if isinstance(defl, core.ManagedList) else [defl]
    defl = [v._ig_value for v in defl]
    if len(defl) > 1:
        defl = [v if isinstance(v, str) else str(v) for v in defl]
        res.update(Default=",".join(defl))
    else:
        res.update(Default=defl[0])
    return res


def _getoutput(value: Any) -> Any:
    return dict(Value=_t(value))


def _t(value: Any) -> Any:

    if isinstance(value, core.CIDR):
        return CIDR(value)
    if isinstance(value, core.Base64Encoded):
        return {"Fn::Base64": _t(value._ig_target)}
    if isinstance(value, core.AccountID):
        return RefValue("AWS::AccountId")
    if isinstance(value, core.AvailabilityZones):
        return {"Fn::GetAZs": ""}
    if isinstance(value, core.NotificationARNs):
        return RefValue("AWS::NotificationARNs")
    if isinstance(value, core.Partition):
        return RefValue("AWS::Partition")
    if isinstance(value, core.Region):
        return RefValue("AWS::Region")
    if isinstance(value, core.StackID):
        return RefValue("AWS::StackId")
    if isinstance(value, core.StackName):
        return RefValue("AWS::StackName")
    if isinstance(value, core.URLSuffix):
        return RefValue("AWS::URLSuffix")
    if isinstance(value, core.Parameter):
        return RefValue(_getidn(value._ig_name), style=None)
    if isinstance(value, core.Join):
        return Join(value)
    if isinstance(value, core.Ref):
        return Ref(value)
    if isinstance(value, core.Select):
        return Select(value)
    if isinstance(value, core.Split):
        return Split(value)
    if isinstance(value, core.Sub):
        return Sub(value)
    if isinstance(value, core.AssetBucket):
        return RefValue("AssetsS3Bucket")
    if isinstance(value, core.AssetKey):
        value = core.String(f"${{AssetsS3Prefix}}{value._ig_asset._ig_hash}")
        return Sub(core.Sub(value, core.Map({})))
    if isinstance(value, core.AssetURI):
        value = core.String(
            f"s3://${{AssetsS3Bucket}}/${{AssetsS3Prefix}}"
            f"{value._ig_asset._ig_hash}"
        )
        return Sub(core.Sub(value, core.Map({})))
    if isinstance(value, core.AssetURL):
        value = core.String(
            f"https://${{AssetsS3Bucket}}.s3.amazonaws.com/${{AssetsS3Prefix}}"
            f"{value._ig_asset._ig_hash}"
        )
        return Sub(core.Sub(value, core.Map({})))
    if isinstance(value, core.Property):
        return _t(value._ig_data)
    if isinstance(value, core.Attribute):
        return GetAtt(value)
    if isinstance(
        value,
        (
            core.Boolean,
            core.Number,
            core.String,
            core.ManagedList,
            core.FreeList,
            core.Map,
        ),
    ):
        return _t(value._ig_value)
    if isinstance(value, dict):
        return {_t(k): _t(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_t(v) for v in value]
    if isinstance(value, str) and "\n" in value:
        return MultilineStr(value)
    return value


@dataclass
class MultilineStr:
    tag: ClassVar[str] = "tag:yaml.org,2002:str"
    v: str

    @classmethod
    def to_yaml(cls, r: Representer, n: "MultilineStr") -> Any:
        return r.represent_scalar(cls.tag, n.v, style="|")


@dataclass
class GetAtt:
    tag: ClassVar[str] = "!GetAtt"
    v: core.Attribute

    @classmethod
    def to_yaml(cls, r: Representer, n: "GetAtt") -> Any:
        return r.represent_scalar(
            cls.tag, f"{_getnidn(n.v._ig_node)}.{_getaidn(n.v._ig_name)}",
        )


@dataclass
class Join:
    tag: ClassVar[str] = "!Join"
    v: core.Join

    @classmethod
    def to_yaml(cls, r: Representer, n: "Join") -> Any:
        return r.represent_sequence(cls.tag, _t([n.v._ig_separator, n.v._ig_items]),)


@dataclass
class Ref:
    tag: ClassVar[str] = "!Ref"
    v: core.Ref

    @classmethod
    def to_yaml(cls, r: Representer, n: "Ref") -> Any:
        return r.represent_scalar(cls.tag, _getnidn(n.v._ig_node))


@dataclass
class RefValue:
    tag: ClassVar[str] = "!Ref"
    v: str
    style: Optional[str] = "'"

    @classmethod
    def to_yaml(cls, r: Representer, n: "RefValue") -> Any:
        return r.represent_scalar(cls.tag, n.v, style=n.style)


@dataclass
class Select:
    tag: ClassVar[str] = "!Select"
    v: core.Select

    @classmethod
    def to_yaml(cls, r: Representer, n: "Select") -> Any:
        return r.represent_sequence(cls.tag, _t([n.v._ig_index, n.v._ig_items]),)


@dataclass
class Split:
    tag: ClassVar[str] = "!Split"
    v: core.Split

    @classmethod
    def to_yaml(cls, r: Representer, n: "Split") -> Any:
        return r.represent_sequence(cls.tag, _t([n.v._ig_separator, n.v._ig_target]),)


@dataclass
class Sub:
    tag: ClassVar[str] = "!Sub"
    v: core.Sub

    @classmethod
    def to_yaml(cls, r: Representer, n: "Sub") -> Any:
        fmt = n.v._ig_format._ig_value
        kwargs = {}
        for k, v in n.v._ig_kwargs._ig_value.items():
            old = new = f"${{{k._ig_value}}}"
            if isinstance(v, core.Parameter):
                new = f"${{{_getidn(v._ig_name)}}}"
            elif isinstance(v, core.Ref):
                new = f"${{{_getnidn(v._ig_node)}}}"
            elif isinstance(v, core.Attribute):
                new = f"${{{_getnidn(v._ig_node)}.{_getaidn(v._ig_name)}}}"
            elif isinstance(getattr(v, "_ig_value", None), (str, int, float)):
                new = f"{v._ig_value}"
            else:
                kwargs[k] = v
            fmt = fmt.replace(old, new)
        if not kwargs:
            return r.represent_scalar(cls.tag, _t(fmt))
        return r.represent_sequence(cls.tag, _t([fmt, kwargs]))


@dataclass
class CIDR:
    tag: ClassVar[str] = "!Cidr"
    v: core.CIDR

    @classmethod
    def to_yaml(cls, r: Representer, n: "CIDR") -> Any:
        return r.represent_sequence(
            cls.tag, _t([n.v._ig_block, n.v._ig_count, n.v._ig_bits])
        )
