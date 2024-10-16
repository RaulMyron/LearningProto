# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hello.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bhello.proto\" \n\x0cHelloMessage\x12\x10\n\x08greeting\x18\x01 \x02(\t28\n\x0cHelloService\x12(\n\x08SayHello\x12\r.HelloMessage\x1a\r.HelloMessage'
)




_HELLOMESSAGE = _descriptor.Descriptor(
  name='HelloMessage',
  full_name='HelloMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='greeting', full_name='HelloMessage.greeting', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=47,
)

DESCRIPTOR.message_types_by_name['HelloMessage'] = _HELLOMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloMessage = _reflection.GeneratedProtocolMessageType('HelloMessage', (_message.Message,), {
  'DESCRIPTOR' : _HELLOMESSAGE,
  '__module__' : 'hello_pb2'
  # @@protoc_insertion_point(class_scope:HelloMessage)
  })
_sym_db.RegisterMessage(HelloMessage)



_HELLOSERVICE = _descriptor.ServiceDescriptor(
  name='HelloService',
  full_name='HelloService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=49,
  serialized_end=105,
  methods=[
  _descriptor.MethodDescriptor(
    name='SayHello',
    full_name='HelloService.SayHello',
    index=0,
    containing_service=None,
    input_type=_HELLOMESSAGE,
    output_type=_HELLOMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_HELLOSERVICE)

DESCRIPTOR.services_by_name['HelloService'] = _HELLOSERVICE

# @@protoc_insertion_point(module_scope)