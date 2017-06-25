# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/mark_tutorial_complete_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import tutorial_state_pb2 as pogoprotos_dot_enums_dot_tutorial__state__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/mark_tutorial_complete_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\nLpogoprotos/networking/requests/messages/mark_tutorial_complete_message.proto\x12\'pogoprotos.networking.requests.messages\x1a%pogoprotos/enums/tutorial_state.proto\"\x9b\x01\n\x1bMarkTutorialCompleteMessage\x12<\n\x13tutorials_completed\x18\x01 \x03(\x0e\x32\x1f.pogoprotos.enums.TutorialState\x12\x1d\n\x15send_marketing_emails\x18\x02 \x01(\x08\x12\x1f\n\x17send_push_notifications\x18\x03 \x01(\x08\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_tutorial__state__pb2.DESCRIPTOR,])




_MARKTUTORIALCOMPLETEMESSAGE = _descriptor.Descriptor(
  name='MarkTutorialCompleteMessage',
  full_name='pogoprotos.networking.requests.messages.MarkTutorialCompleteMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tutorials_completed', full_name='pogoprotos.networking.requests.messages.MarkTutorialCompleteMessage.tutorials_completed', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='send_marketing_emails', full_name='pogoprotos.networking.requests.messages.MarkTutorialCompleteMessage.send_marketing_emails', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='send_push_notifications', full_name='pogoprotos.networking.requests.messages.MarkTutorialCompleteMessage.send_push_notifications', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=161,
  serialized_end=316,
)

_MARKTUTORIALCOMPLETEMESSAGE.fields_by_name['tutorials_completed'].enum_type = pogoprotos_dot_enums_dot_tutorial__state__pb2._TUTORIALSTATE
DESCRIPTOR.message_types_by_name['MarkTutorialCompleteMessage'] = _MARKTUTORIALCOMPLETEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MarkTutorialCompleteMessage = _reflection.GeneratedProtocolMessageType('MarkTutorialCompleteMessage', (_message.Message,), dict(
  DESCRIPTOR = _MARKTUTORIALCOMPLETEMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.mark_tutorial_complete_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.MarkTutorialCompleteMessage)
  ))
_sym_db.RegisterMessage(MarkTutorialCompleteMessage)


# @@protoc_insertion_point(module_scope)