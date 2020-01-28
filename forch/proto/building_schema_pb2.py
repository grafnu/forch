# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: forch/proto/building_schema.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='forch/proto/building_schema.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!forch/proto/building_schema.proto\"\x93\x05\n\x0e\x42uildingSchema\x12\x30\n\tmac_addrs\x18\x01 \x03(\x0b\x32\x1d.BuildingSchema.MacAddrsEntry\x1aK\n\rMacAddrsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.BuildingSchema.DeviceInfo:\x02\x38\x01\x1a\xbb\x01\n\nDeviceInfo\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05group\x18\x02 \x01(\t\x12@\n\x0b\x63ontrollers\x18\x03 \x03(\x0b\x32+.BuildingSchema.DeviceInfo.ControllersEntry\x1aN\n\x10\x43ontrollersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.BuildingSchema.Controller:\x02\x38\x01\x1a\x9a\x01\n\nController\x12>\n\ncontrolees\x18\x01 \x03(\x0b\x32*.BuildingSchema.Controller.ControleesEntry\x1aL\n\x0f\x43ontroleesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.BuildingSchema.Controlee:\x02\x38\x01\x1a\x96\x01\n\tControlee\x12:\n\tmac_addrs\x18\x01 \x03(\x0b\x32\'.BuildingSchema.Controlee.MacAddrsEntry\x1aM\n\rMacAddrsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.BuildingSchema.DeviceTarget:\x02\x38\x01\x1a\x0e\n\x0c\x44\x65viceTargetb\x06proto3')
)




_BUILDINGSCHEMA_MACADDRSENTRY = _descriptor.Descriptor(
  name='MacAddrsEntry',
  full_name='BuildingSchema.MacAddrsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='BuildingSchema.MacAddrsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='BuildingSchema.MacAddrsEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=181,
)

_BUILDINGSCHEMA_DEVICEINFO_CONTROLLERSENTRY = _descriptor.Descriptor(
  name='ControllersEntry',
  full_name='BuildingSchema.DeviceInfo.ControllersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='BuildingSchema.DeviceInfo.ControllersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='BuildingSchema.DeviceInfo.ControllersEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=293,
  serialized_end=371,
)

_BUILDINGSCHEMA_DEVICEINFO = _descriptor.Descriptor(
  name='DeviceInfo',
  full_name='BuildingSchema.DeviceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='BuildingSchema.DeviceInfo.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group', full_name='BuildingSchema.DeviceInfo.group', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='controllers', full_name='BuildingSchema.DeviceInfo.controllers', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BUILDINGSCHEMA_DEVICEINFO_CONTROLLERSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=184,
  serialized_end=371,
)

_BUILDINGSCHEMA_CONTROLLER_CONTROLEESENTRY = _descriptor.Descriptor(
  name='ControleesEntry',
  full_name='BuildingSchema.Controller.ControleesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='BuildingSchema.Controller.ControleesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='BuildingSchema.Controller.ControleesEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=452,
  serialized_end=528,
)

_BUILDINGSCHEMA_CONTROLLER = _descriptor.Descriptor(
  name='Controller',
  full_name='BuildingSchema.Controller',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='controlees', full_name='BuildingSchema.Controller.controlees', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BUILDINGSCHEMA_CONTROLLER_CONTROLEESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=374,
  serialized_end=528,
)

_BUILDINGSCHEMA_CONTROLEE_MACADDRSENTRY = _descriptor.Descriptor(
  name='MacAddrsEntry',
  full_name='BuildingSchema.Controlee.MacAddrsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='BuildingSchema.Controlee.MacAddrsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='BuildingSchema.Controlee.MacAddrsEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=604,
  serialized_end=681,
)

_BUILDINGSCHEMA_CONTROLEE = _descriptor.Descriptor(
  name='Controlee',
  full_name='BuildingSchema.Controlee',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mac_addrs', full_name='BuildingSchema.Controlee.mac_addrs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BUILDINGSCHEMA_CONTROLEE_MACADDRSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=531,
  serialized_end=681,
)

_BUILDINGSCHEMA_DEVICETARGET = _descriptor.Descriptor(
  name='DeviceTarget',
  full_name='BuildingSchema.DeviceTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=683,
  serialized_end=697,
)

_BUILDINGSCHEMA = _descriptor.Descriptor(
  name='BuildingSchema',
  full_name='BuildingSchema',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mac_addrs', full_name='BuildingSchema.mac_addrs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BUILDINGSCHEMA_MACADDRSENTRY, _BUILDINGSCHEMA_DEVICEINFO, _BUILDINGSCHEMA_CONTROLLER, _BUILDINGSCHEMA_CONTROLEE, _BUILDINGSCHEMA_DEVICETARGET, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=697,
)

_BUILDINGSCHEMA_MACADDRSENTRY.fields_by_name['value'].message_type = _BUILDINGSCHEMA_DEVICEINFO
_BUILDINGSCHEMA_MACADDRSENTRY.containing_type = _BUILDINGSCHEMA
_BUILDINGSCHEMA_DEVICEINFO_CONTROLLERSENTRY.fields_by_name['value'].message_type = _BUILDINGSCHEMA_CONTROLLER
_BUILDINGSCHEMA_DEVICEINFO_CONTROLLERSENTRY.containing_type = _BUILDINGSCHEMA_DEVICEINFO
_BUILDINGSCHEMA_DEVICEINFO.fields_by_name['controllers'].message_type = _BUILDINGSCHEMA_DEVICEINFO_CONTROLLERSENTRY
_BUILDINGSCHEMA_DEVICEINFO.containing_type = _BUILDINGSCHEMA
_BUILDINGSCHEMA_CONTROLLER_CONTROLEESENTRY.fields_by_name['value'].message_type = _BUILDINGSCHEMA_CONTROLEE
_BUILDINGSCHEMA_CONTROLLER_CONTROLEESENTRY.containing_type = _BUILDINGSCHEMA_CONTROLLER
_BUILDINGSCHEMA_CONTROLLER.fields_by_name['controlees'].message_type = _BUILDINGSCHEMA_CONTROLLER_CONTROLEESENTRY
_BUILDINGSCHEMA_CONTROLLER.containing_type = _BUILDINGSCHEMA
_BUILDINGSCHEMA_CONTROLEE_MACADDRSENTRY.fields_by_name['value'].message_type = _BUILDINGSCHEMA_DEVICETARGET
_BUILDINGSCHEMA_CONTROLEE_MACADDRSENTRY.containing_type = _BUILDINGSCHEMA_CONTROLEE
_BUILDINGSCHEMA_CONTROLEE.fields_by_name['mac_addrs'].message_type = _BUILDINGSCHEMA_CONTROLEE_MACADDRSENTRY
_BUILDINGSCHEMA_CONTROLEE.containing_type = _BUILDINGSCHEMA
_BUILDINGSCHEMA_DEVICETARGET.containing_type = _BUILDINGSCHEMA
_BUILDINGSCHEMA.fields_by_name['mac_addrs'].message_type = _BUILDINGSCHEMA_MACADDRSENTRY
DESCRIPTOR.message_types_by_name['BuildingSchema'] = _BUILDINGSCHEMA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuildingSchema = _reflection.GeneratedProtocolMessageType('BuildingSchema', (_message.Message,), dict(

  MacAddrsEntry = _reflection.GeneratedProtocolMessageType('MacAddrsEntry', (_message.Message,), dict(
    DESCRIPTOR = _BUILDINGSCHEMA_MACADDRSENTRY,
    __module__ = 'forch.proto.building_schema_pb2'
    # @@protoc_insertion_point(class_scope:BuildingSchema.MacAddrsEntry)
    ))
  ,

  DeviceInfo = _reflection.GeneratedProtocolMessageType('DeviceInfo', (_message.Message,), dict(

    ControllersEntry = _reflection.GeneratedProtocolMessageType('ControllersEntry', (_message.Message,), dict(
      DESCRIPTOR = _BUILDINGSCHEMA_DEVICEINFO_CONTROLLERSENTRY,
      __module__ = 'forch.proto.building_schema_pb2'
      # @@protoc_insertion_point(class_scope:BuildingSchema.DeviceInfo.ControllersEntry)
      ))
    ,
    DESCRIPTOR = _BUILDINGSCHEMA_DEVICEINFO,
    __module__ = 'forch.proto.building_schema_pb2'
    # @@protoc_insertion_point(class_scope:BuildingSchema.DeviceInfo)
    ))
  ,

  Controller = _reflection.GeneratedProtocolMessageType('Controller', (_message.Message,), dict(

    ControleesEntry = _reflection.GeneratedProtocolMessageType('ControleesEntry', (_message.Message,), dict(
      DESCRIPTOR = _BUILDINGSCHEMA_CONTROLLER_CONTROLEESENTRY,
      __module__ = 'forch.proto.building_schema_pb2'
      # @@protoc_insertion_point(class_scope:BuildingSchema.Controller.ControleesEntry)
      ))
    ,
    DESCRIPTOR = _BUILDINGSCHEMA_CONTROLLER,
    __module__ = 'forch.proto.building_schema_pb2'
    # @@protoc_insertion_point(class_scope:BuildingSchema.Controller)
    ))
  ,

  Controlee = _reflection.GeneratedProtocolMessageType('Controlee', (_message.Message,), dict(

    MacAddrsEntry = _reflection.GeneratedProtocolMessageType('MacAddrsEntry', (_message.Message,), dict(
      DESCRIPTOR = _BUILDINGSCHEMA_CONTROLEE_MACADDRSENTRY,
      __module__ = 'forch.proto.building_schema_pb2'
      # @@protoc_insertion_point(class_scope:BuildingSchema.Controlee.MacAddrsEntry)
      ))
    ,
    DESCRIPTOR = _BUILDINGSCHEMA_CONTROLEE,
    __module__ = 'forch.proto.building_schema_pb2'
    # @@protoc_insertion_point(class_scope:BuildingSchema.Controlee)
    ))
  ,

  DeviceTarget = _reflection.GeneratedProtocolMessageType('DeviceTarget', (_message.Message,), dict(
    DESCRIPTOR = _BUILDINGSCHEMA_DEVICETARGET,
    __module__ = 'forch.proto.building_schema_pb2'
    # @@protoc_insertion_point(class_scope:BuildingSchema.DeviceTarget)
    ))
  ,
  DESCRIPTOR = _BUILDINGSCHEMA,
  __module__ = 'forch.proto.building_schema_pb2'
  # @@protoc_insertion_point(class_scope:BuildingSchema)
  ))
_sym_db.RegisterMessage(BuildingSchema)
_sym_db.RegisterMessage(BuildingSchema.MacAddrsEntry)
_sym_db.RegisterMessage(BuildingSchema.DeviceInfo)
_sym_db.RegisterMessage(BuildingSchema.DeviceInfo.ControllersEntry)
_sym_db.RegisterMessage(BuildingSchema.Controller)
_sym_db.RegisterMessage(BuildingSchema.Controller.ControleesEntry)
_sym_db.RegisterMessage(BuildingSchema.Controlee)
_sym_db.RegisterMessage(BuildingSchema.Controlee.MacAddrsEntry)
_sym_db.RegisterMessage(BuildingSchema.DeviceTarget)


_BUILDINGSCHEMA_MACADDRSENTRY._options = None
_BUILDINGSCHEMA_DEVICEINFO_CONTROLLERSENTRY._options = None
_BUILDINGSCHEMA_CONTROLLER_CONTROLEESENTRY._options = None
_BUILDINGSCHEMA_CONTROLEE_MACADDRSENTRY._options = None
# @@protoc_insertion_point(module_scope)
