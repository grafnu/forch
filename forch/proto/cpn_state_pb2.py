# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: forch/proto/cpn_state.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from forch.proto import cpn_config_pb2 as forch_dot_proto_dot_cpn__config__pb2
from forch.proto import shared_constants_pb2 as forch_dot_proto_dot_shared__constants__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='forch/proto/cpn_state.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x1b\x66orch/proto/cpn_state.proto\x1a\x1c\x66orch/proto/cpn_config.proto\x1a\"forch/proto/shared_constants.proto\"\xbd\x05\n\x08\x43pnState\x12*\n\tcpn_nodes\x18\x01 \x03(\x0b\x32\x17.CpnState.CpnNodesEntry\x12\x1f\n\tcpn_state\x18\x02 \x01(\x0e\x32\x0c.State.State\x12\x18\n\x10\x63pn_state_detail\x18\x03 \x01(\t\x12\x1e\n\x16\x63pn_state_change_count\x18\x04 \x01(\x05\x12\x1d\n\x15\x63pn_state_last_update\x18\x05 \x01(\t\x12\x1d\n\x15\x63pn_state_last_change\x18\x06 \x01(\t\x12\x18\n\x10system_state_url\x18\x07 \x01(\t\x1a\x42\n\rCpnNodesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.CpnState.CpnNode:\x02\x38\x01\x1a\xc9\x01\n\x07\x43pnNode\x12\"\n\nattributes\x18\x01 \x01(\x0b\x32\x0e.CpnAttributes\x12\x1b\n\x05state\x18\x02 \x01(\x0e\x32\x0c.State.State\x12+\n\x0cping_results\x18\x03 \x01(\x0b\x32\x15.CpnState.PingResults\x12\x1a\n\x12state_change_count\x18\x04 \x01(\x05\x12\x19\n\x11state_last_update\x18\x05 \x01(\t\x12\x19\n\x11state_last_change\x18\x06 \x01(\t\x1a\x81\x01\n\x0bPingResults\x12\x13\n\x0btransmitted\x18\x01 \x01(\x05\x12\x10\n\x08received\x18\x02 \x01(\x05\x12\x17\n\x0floss_percentage\x18\x03 \x01(\x05\x12\x0f\n\x07time_ms\x18\x04 \x01(\x05\x12!\n\x06rtt_ms\x18\x05 \x01(\x0b\x32\x11.CpnState.RttInfo\x1a>\n\x07RttInfo\x12\x0b\n\x03min\x18\x01 \x01(\x02\x12\x0b\n\x03\x61vg\x18\x02 \x01(\x02\x12\x0b\n\x03max\x18\x03 \x01(\x02\x12\x0c\n\x04mdev\x18\x04 \x01(\x02\x62\x06proto3'
  ,
  dependencies=[forch_dot_proto_dot_cpn__config__pb2.DESCRIPTOR,forch_dot_proto_dot_shared__constants__pb2.DESCRIPTOR,])




_CPNSTATE_CPNNODESENTRY = _descriptor.Descriptor(
  name='CpnNodesEntry',
  full_name='CpnState.CpnNodesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='CpnState.CpnNodesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='CpnState.CpnNodesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=333,
  serialized_end=399,
)

_CPNSTATE_CPNNODE = _descriptor.Descriptor(
  name='CpnNode',
  full_name='CpnState.CpnNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attributes', full_name='CpnState.CpnNode.attributes', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='CpnState.CpnNode.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ping_results', full_name='CpnState.CpnNode.ping_results', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state_change_count', full_name='CpnState.CpnNode.state_change_count', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state_last_update', full_name='CpnState.CpnNode.state_last_update', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state_last_change', full_name='CpnState.CpnNode.state_last_change', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=402,
  serialized_end=603,
)

_CPNSTATE_PINGRESULTS = _descriptor.Descriptor(
  name='PingResults',
  full_name='CpnState.PingResults',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transmitted', full_name='CpnState.PingResults.transmitted', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='received', full_name='CpnState.PingResults.received', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loss_percentage', full_name='CpnState.PingResults.loss_percentage', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_ms', full_name='CpnState.PingResults.time_ms', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rtt_ms', full_name='CpnState.PingResults.rtt_ms', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=606,
  serialized_end=735,
)

_CPNSTATE_RTTINFO = _descriptor.Descriptor(
  name='RttInfo',
  full_name='CpnState.RttInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='CpnState.RttInfo.min', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avg', full_name='CpnState.RttInfo.avg', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='CpnState.RttInfo.max', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mdev', full_name='CpnState.RttInfo.mdev', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=737,
  serialized_end=799,
)

_CPNSTATE = _descriptor.Descriptor(
  name='CpnState',
  full_name='CpnState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cpn_nodes', full_name='CpnState.cpn_nodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpn_state', full_name='CpnState.cpn_state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpn_state_detail', full_name='CpnState.cpn_state_detail', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpn_state_change_count', full_name='CpnState.cpn_state_change_count', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpn_state_last_update', full_name='CpnState.cpn_state_last_update', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpn_state_last_change', full_name='CpnState.cpn_state_last_change', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='system_state_url', full_name='CpnState.system_state_url', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CPNSTATE_CPNNODESENTRY, _CPNSTATE_CPNNODE, _CPNSTATE_PINGRESULTS, _CPNSTATE_RTTINFO, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=799,
)

_CPNSTATE_CPNNODESENTRY.fields_by_name['value'].message_type = _CPNSTATE_CPNNODE
_CPNSTATE_CPNNODESENTRY.containing_type = _CPNSTATE
_CPNSTATE_CPNNODE.fields_by_name['attributes'].message_type = forch_dot_proto_dot_cpn__config__pb2._CPNATTRIBUTES
_CPNSTATE_CPNNODE.fields_by_name['state'].enum_type = forch_dot_proto_dot_shared__constants__pb2._STATE_STATE
_CPNSTATE_CPNNODE.fields_by_name['ping_results'].message_type = _CPNSTATE_PINGRESULTS
_CPNSTATE_CPNNODE.containing_type = _CPNSTATE
_CPNSTATE_PINGRESULTS.fields_by_name['rtt_ms'].message_type = _CPNSTATE_RTTINFO
_CPNSTATE_PINGRESULTS.containing_type = _CPNSTATE
_CPNSTATE_RTTINFO.containing_type = _CPNSTATE
_CPNSTATE.fields_by_name['cpn_nodes'].message_type = _CPNSTATE_CPNNODESENTRY
_CPNSTATE.fields_by_name['cpn_state'].enum_type = forch_dot_proto_dot_shared__constants__pb2._STATE_STATE
DESCRIPTOR.message_types_by_name['CpnState'] = _CPNSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CpnState = _reflection.GeneratedProtocolMessageType('CpnState', (_message.Message,), {

  'CpnNodesEntry' : _reflection.GeneratedProtocolMessageType('CpnNodesEntry', (_message.Message,), {
    'DESCRIPTOR' : _CPNSTATE_CPNNODESENTRY,
    '__module__' : 'forch.proto.cpn_state_pb2'
    # @@protoc_insertion_point(class_scope:CpnState.CpnNodesEntry)
    })
  ,

  'CpnNode' : _reflection.GeneratedProtocolMessageType('CpnNode', (_message.Message,), {
    'DESCRIPTOR' : _CPNSTATE_CPNNODE,
    '__module__' : 'forch.proto.cpn_state_pb2'
    # @@protoc_insertion_point(class_scope:CpnState.CpnNode)
    })
  ,

  'PingResults' : _reflection.GeneratedProtocolMessageType('PingResults', (_message.Message,), {
    'DESCRIPTOR' : _CPNSTATE_PINGRESULTS,
    '__module__' : 'forch.proto.cpn_state_pb2'
    # @@protoc_insertion_point(class_scope:CpnState.PingResults)
    })
  ,

  'RttInfo' : _reflection.GeneratedProtocolMessageType('RttInfo', (_message.Message,), {
    'DESCRIPTOR' : _CPNSTATE_RTTINFO,
    '__module__' : 'forch.proto.cpn_state_pb2'
    # @@protoc_insertion_point(class_scope:CpnState.RttInfo)
    })
  ,
  'DESCRIPTOR' : _CPNSTATE,
  '__module__' : 'forch.proto.cpn_state_pb2'
  # @@protoc_insertion_point(class_scope:CpnState)
  })
_sym_db.RegisterMessage(CpnState)
_sym_db.RegisterMessage(CpnState.CpnNodesEntry)
_sym_db.RegisterMessage(CpnState.CpnNode)
_sym_db.RegisterMessage(CpnState.PingResults)
_sym_db.RegisterMessage(CpnState.RttInfo)


_CPNSTATE_CPNNODESENTRY._options = None
# @@protoc_insertion_point(module_scope)
