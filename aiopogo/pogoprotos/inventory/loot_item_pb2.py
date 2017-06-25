# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/inventory/loot_item.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory.item import item_id_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__id__pb2
from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/inventory/loot_item.proto',
  package='pogoprotos.inventory',
  syntax='proto3',
  serialized_pb=_b('\n$pogoprotos/inventory/loot_item.proto\x12\x14pogoprotos.inventory\x1a\'pogoprotos/inventory/item/item_id.proto\x1a!pogoprotos/enums/pokemon_id.proto\"\xa2\x01\n\x08LootItem\x12/\n\x04item\x18\x01 \x01(\x0e\x32!.pogoprotos.inventory.item.ItemId\x12\x10\n\x08stardust\x18\x02 \x01(\x08\x12\x10\n\x08pokecoin\x18\x03 \x01(\x08\x12\x32\n\rpokemon_candy\x18\x04 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\r\n\x05\x63ount\x18\x05 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_item_dot_item__id__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,])




_LOOTITEM = _descriptor.Descriptor(
  name='LootItem',
  full_name='pogoprotos.inventory.LootItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='pogoprotos.inventory.LootItem.item', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stardust', full_name='pogoprotos.inventory.LootItem.stardust', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokecoin', full_name='pogoprotos.inventory.LootItem.pokecoin', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_candy', full_name='pogoprotos.inventory.LootItem.pokemon_candy', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='pogoprotos.inventory.LootItem.count', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=139,
  serialized_end=301,
)

_LOOTITEM.fields_by_name['item'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
_LOOTITEM.fields_by_name['pokemon_candy'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
DESCRIPTOR.message_types_by_name['LootItem'] = _LOOTITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LootItem = _reflection.GeneratedProtocolMessageType('LootItem', (_message.Message,), dict(
  DESCRIPTOR = _LOOTITEM,
  __module__ = 'pogoprotos.inventory.loot_item_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.inventory.LootItem)
  ))
_sym_db.RegisterMessage(LootItem)


# @@protoc_insertion_point(module_scope)