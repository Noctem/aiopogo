# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/inventory/egg_incubators.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory import egg_incubator_pb2 as pogoprotos_dot_inventory_dot_egg__incubator__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/inventory/egg_incubators.proto',
  package='pogoprotos.inventory',
  syntax='proto3',
  serialized_pb=_b('\n)pogoprotos/inventory/egg_incubators.proto\x12\x14pogoprotos.inventory\x1a(pogoprotos/inventory/egg_incubator.proto\"J\n\rEggIncubators\x12\x39\n\regg_incubator\x18\x01 \x03(\x0b\x32\".pogoprotos.inventory.EggIncubatorb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_egg__incubator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EGGINCUBATORS = _descriptor.Descriptor(
  name='EggIncubators',
  full_name='pogoprotos.inventory.EggIncubators',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='egg_incubator', full_name='pogoprotos.inventory.EggIncubators.egg_incubator', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=183,
)

_EGGINCUBATORS.fields_by_name['egg_incubator'].message_type = pogoprotos_dot_inventory_dot_egg__incubator__pb2._EGGINCUBATOR
DESCRIPTOR.message_types_by_name['EggIncubators'] = _EGGINCUBATORS

EggIncubators = _reflection.GeneratedProtocolMessageType('EggIncubators', (_message.Message,), dict(
  DESCRIPTOR = _EGGINCUBATORS,
  __module__ = 'pogoprotos.inventory.egg_incubators_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.inventory.EggIncubators)
  ))
_sym_db.RegisterMessage(EggIncubators)


# @@protoc_insertion_point(module_scope)