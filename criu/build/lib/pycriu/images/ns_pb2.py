# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ns.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ns.proto',
  package='',
  serialized_pb=_b('\n\x08ns.proto\"K\n\rns_file_entry\x12\n\n\x02id\x18\x01 \x02(\r\x12\r\n\x05ns_id\x18\x02 \x02(\r\x12\x10\n\x08ns_cflag\x18\x03 \x02(\r\x12\r\n\x05\x66lags\x18\x04 \x02(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_NS_FILE_ENTRY = _descriptor.Descriptor(
  name='ns_file_entry',
  full_name='ns_file_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ns_file_entry.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ns_id', full_name='ns_file_entry.ns_id', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ns_cflag', full_name='ns_file_entry.ns_cflag', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flags', full_name='ns_file_entry.flags', index=3,
      number=4, type=13, cpp_type=3, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=12,
  serialized_end=87,
)

DESCRIPTOR.message_types_by_name['ns_file_entry'] = _NS_FILE_ENTRY

ns_file_entry = _reflection.GeneratedProtocolMessageType('ns_file_entry', (_message.Message,), dict(
  DESCRIPTOR = _NS_FILE_ENTRY,
  __module__ = 'ns_pb2'
  # @@protoc_insertion_point(class_scope:ns_file_entry)
  ))
_sym_db.RegisterMessage(ns_file_entry)


# @@protoc_insertion_point(module_scope)
