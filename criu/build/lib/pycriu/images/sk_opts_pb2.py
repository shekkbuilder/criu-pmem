# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sk-opts.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sk-opts.proto',
  package='',
  serialized_pb=_b('\n\rsk-opts.proto\"\xe2\x02\n\rsk_opts_entry\x12\x11\n\tso_sndbuf\x18\x01 \x02(\r\x12\x11\n\tso_rcvbuf\x18\x02 \x02(\r\x12\x16\n\x0eso_snd_tmo_sec\x18\x03 \x02(\x04\x12\x17\n\x0fso_snd_tmo_usec\x18\x04 \x02(\x04\x12\x16\n\x0eso_rcv_tmo_sec\x18\x05 \x02(\x04\x12\x17\n\x0fso_rcv_tmo_usec\x18\x06 \x02(\x04\x12\x11\n\treuseaddr\x18\x07 \x01(\x08\x12\x13\n\x0bso_priority\x18\x08 \x01(\r\x12\x13\n\x0bso_rcvlowat\x18\t \x01(\r\x12\x0f\n\x07so_mark\x18\n \x01(\r\x12\x13\n\x0bso_passcred\x18\x0b \x01(\x08\x12\x12\n\nso_passsec\x18\x0c \x01(\x08\x12\x14\n\x0cso_dontroute\x18\r \x01(\x08\x12\x13\n\x0bso_no_check\x18\x0e \x01(\x08\x12\x14\n\x0cso_bound_dev\x18\x0f \x01(\t\x12\x11\n\tso_filter\x18\x10 \x03(\x06*6\n\x0bsk_shutdown\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04READ\x10\x01\x12\t\n\x05WRITE\x10\x02\x12\x08\n\x04\x42OTH\x10\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_SK_SHUTDOWN = _descriptor.EnumDescriptor(
  name='sk_shutdown',
  full_name='sk_shutdown',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRITE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOTH', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=374,
  serialized_end=428,
)
_sym_db.RegisterEnumDescriptor(_SK_SHUTDOWN)

sk_shutdown = enum_type_wrapper.EnumTypeWrapper(_SK_SHUTDOWN)
NONE = 0
READ = 1
WRITE = 2
BOTH = 3



_SK_OPTS_ENTRY = _descriptor.Descriptor(
  name='sk_opts_entry',
  full_name='sk_opts_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='so_sndbuf', full_name='sk_opts_entry.so_sndbuf', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='so_rcvbuf', full_name='sk_opts_entry.so_rcvbuf', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='so_snd_tmo_sec', full_name='sk_opts_entry.so_snd_tmo_sec', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='so_snd_tmo_usec', full_name='sk_opts_entry.so_snd_tmo_usec', index=3,
      number=4, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='so_rcv_tmo_sec', full_name='sk_opts_entry.so_rcv_tmo_sec', index=4,
      number=5, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='so_rcv_tmo_usec', full_name='sk_opts_entry.so_rcv_tmo_usec', index=5,
      number=6, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reuseaddr', full_name='sk_opts_entry.reuseaddr', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='so_priority', full_name='sk_opts_entry.so_priority', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='so_rcvlowat', full_name='sk_opts_entry.so_rcvlowat', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='so_mark', full_name='sk_opts_entry.so_mark', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='so_passcred', full_name='sk_opts_entry.so_passcred', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='so_passsec', full_name='sk_opts_entry.so_passsec', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='so_dontroute', full_name='sk_opts_entry.so_dontroute', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='so_no_check', full_name='sk_opts_entry.so_no_check', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='so_bound_dev', full_name='sk_opts_entry.so_bound_dev', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='so_filter', full_name='sk_opts_entry.so_filter', index=15,
      number=16, type=6, cpp_type=4, label=3,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=372,
)

DESCRIPTOR.message_types_by_name['sk_opts_entry'] = _SK_OPTS_ENTRY
DESCRIPTOR.enum_types_by_name['sk_shutdown'] = _SK_SHUTDOWN

sk_opts_entry = _reflection.GeneratedProtocolMessageType('sk_opts_entry', (_message.Message,), dict(
  DESCRIPTOR = _SK_OPTS_ENTRY,
  __module__ = 'sk_opts_pb2'
  # @@protoc_insertion_point(class_scope:sk_opts_entry)
  ))
_sym_db.RegisterMessage(sk_opts_entry)


# @@protoc_insertion_point(module_scope)
