# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: forch/proto/path_node.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='forch/proto/path_node.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1b\x66orch/proto/path_node.proto\"3\n\x08PathNode\x12\x0e\n\x06switch\x18\x01 \x01(\t\x12\n\n\x02in\x18\x02 \x01(\x05\x12\x0b\n\x03out\x18\x03 \x01(\x05\x62\x06proto3')
)




_PATHNODE = _descriptor.Descriptor(
  name='PathNode',
  full_name='PathNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='switch', full_name='PathNode.switch', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='in', full_name='PathNode.in', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='out', full_name='PathNode.out', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=31,
  serialized_end=82,
)

DESCRIPTOR.message_types_by_name['PathNode'] = _PATHNODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PathNode = _reflection.GeneratedProtocolMessageType('PathNode', (_message.Message,), dict(
  DESCRIPTOR = _PATHNODE,
  __module__ = 'forch.proto.path_node_pb2'
  # @@protoc_insertion_point(class_scope:PathNode)
  ))
_sym_db.RegisterMessage(PathNode)


# @@protoc_insertion_point(module_scope)
