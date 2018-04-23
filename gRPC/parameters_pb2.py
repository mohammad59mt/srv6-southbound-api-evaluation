# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: parameters.proto

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
  name='parameters.proto',
  package='parameters',
  syntax='proto3',
  serialized_pb=_b('\n\x10parameters.proto\x12\nparameters\"X\n\x11\x41\x64\x64SrRouteRequest\x12\x0e\n\x06prefix\x18\x01 \x01(\t\x12\x11\n\tencapmode\x18\x02 \x01(\t\x12\x10\n\x08segments\x18\x03 \x01(\t\x12\x0e\n\x06\x64\x65vice\x18\x04 \x01(\t\"\"\n\x0f\x41\x64\x64SrRouteReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"0\n\x0eRmRouteRequest\x12\x0e\n\x06prefix\x18\x01 \x01(\t\x12\x0e\n\x06\x64\x65vice\x18\x02 \x01(\t\"\x1f\n\x0cRmRouteReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x12\n\x10ListRouteRequest\"!\n\x0eListRouteReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"1\n\x12\x43hangeRouteRequest\x12\x0e\n\x06prefix\x18\x01 \x01(\t\x12\x0b\n\x03via\x18\x02 \x01(\t\"#\n\x10\x43hangeRouteReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"H\n\x14\x43hangeSrRouteRequest\x12\x0e\n\x06prefix\x18\x01 \x01(\t\x12\x10\n\x08segments\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x65vice\x18\x03 \x01(\t\"%\n\x12\x43hangeSrRouteReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\xad\x04\n\x0eSegmentRouting\x12J\n\nAddSrRoute\x12\x1d.parameters.AddSrRouteRequest\x1a\x1b.parameters.AddSrRouteReply\"\x00\x12\x45\n\x0bRemoveRoute\x12\x1a.parameters.RmRouteRequest\x1a\x18.parameters.RmRouteReply\"\x00\x12G\n\tListRoute\x12\x1c.parameters.ListRouteRequest\x1a\x1a.parameters.ListRouteReply\"\x00\x12M\n\x0b\x43hangeRoute\x12\x1e.parameters.ChangeRouteRequest\x1a\x1c.parameters.ChangeRouteReply\"\x00\x12S\n\rChangeSrRoute\x12 .parameters.ChangeSrRouteRequest\x1a\x1e.parameters.ChangeSrRouteReply\"\x00\x12O\n\x0f\x42unchAddSrRoute\x12\x1d.parameters.AddSrRouteRequest\x1a\x1b.parameters.AddSrRouteReply\"\x00\x12J\n\x10\x42unchRemoveRoute\x12\x1a.parameters.RmRouteRequest\x1a\x18.parameters.RmRouteReply\"\x00\x42\x02P\x01\x62\x06proto3')
)




_ADDSRROUTEREQUEST = _descriptor.Descriptor(
  name='AddSrRouteRequest',
  full_name='parameters.AddSrRouteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prefix', full_name='parameters.AddSrRouteRequest.prefix', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encapmode', full_name='parameters.AddSrRouteRequest.encapmode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='segments', full_name='parameters.AddSrRouteRequest.segments', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device', full_name='parameters.AddSrRouteRequest.device', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=32,
  serialized_end=120,
)


_ADDSRROUTEREPLY = _descriptor.Descriptor(
  name='AddSrRouteReply',
  full_name='parameters.AddSrRouteReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='parameters.AddSrRouteReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=122,
  serialized_end=156,
)


_RMROUTEREQUEST = _descriptor.Descriptor(
  name='RmRouteRequest',
  full_name='parameters.RmRouteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prefix', full_name='parameters.RmRouteRequest.prefix', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device', full_name='parameters.RmRouteRequest.device', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=158,
  serialized_end=206,
)


_RMROUTEREPLY = _descriptor.Descriptor(
  name='RmRouteReply',
  full_name='parameters.RmRouteReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='parameters.RmRouteReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=208,
  serialized_end=239,
)


_LISTROUTEREQUEST = _descriptor.Descriptor(
  name='ListRouteRequest',
  full_name='parameters.ListRouteRequest',
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=241,
  serialized_end=259,
)


_LISTROUTEREPLY = _descriptor.Descriptor(
  name='ListRouteReply',
  full_name='parameters.ListRouteReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='parameters.ListRouteReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=261,
  serialized_end=294,
)


_CHANGEROUTEREQUEST = _descriptor.Descriptor(
  name='ChangeRouteRequest',
  full_name='parameters.ChangeRouteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prefix', full_name='parameters.ChangeRouteRequest.prefix', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='via', full_name='parameters.ChangeRouteRequest.via', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=296,
  serialized_end=345,
)


_CHANGEROUTEREPLY = _descriptor.Descriptor(
  name='ChangeRouteReply',
  full_name='parameters.ChangeRouteReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='parameters.ChangeRouteReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=347,
  serialized_end=382,
)


_CHANGESRROUTEREQUEST = _descriptor.Descriptor(
  name='ChangeSrRouteRequest',
  full_name='parameters.ChangeSrRouteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prefix', full_name='parameters.ChangeSrRouteRequest.prefix', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='segments', full_name='parameters.ChangeSrRouteRequest.segments', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device', full_name='parameters.ChangeSrRouteRequest.device', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=384,
  serialized_end=456,
)


_CHANGESRROUTEREPLY = _descriptor.Descriptor(
  name='ChangeSrRouteReply',
  full_name='parameters.ChangeSrRouteReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='parameters.ChangeSrRouteReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=458,
  serialized_end=495,
)

DESCRIPTOR.message_types_by_name['AddSrRouteRequest'] = _ADDSRROUTEREQUEST
DESCRIPTOR.message_types_by_name['AddSrRouteReply'] = _ADDSRROUTEREPLY
DESCRIPTOR.message_types_by_name['RmRouteRequest'] = _RMROUTEREQUEST
DESCRIPTOR.message_types_by_name['RmRouteReply'] = _RMROUTEREPLY
DESCRIPTOR.message_types_by_name['ListRouteRequest'] = _LISTROUTEREQUEST
DESCRIPTOR.message_types_by_name['ListRouteReply'] = _LISTROUTEREPLY
DESCRIPTOR.message_types_by_name['ChangeRouteRequest'] = _CHANGEROUTEREQUEST
DESCRIPTOR.message_types_by_name['ChangeRouteReply'] = _CHANGEROUTEREPLY
DESCRIPTOR.message_types_by_name['ChangeSrRouteRequest'] = _CHANGESRROUTEREQUEST
DESCRIPTOR.message_types_by_name['ChangeSrRouteReply'] = _CHANGESRROUTEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddSrRouteRequest = _reflection.GeneratedProtocolMessageType('AddSrRouteRequest', (_message.Message,), dict(
  DESCRIPTOR = _ADDSRROUTEREQUEST,
  __module__ = 'parameters_pb2'
  # @@protoc_insertion_point(class_scope:parameters.AddSrRouteRequest)
  ))
_sym_db.RegisterMessage(AddSrRouteRequest)

AddSrRouteReply = _reflection.GeneratedProtocolMessageType('AddSrRouteReply', (_message.Message,), dict(
  DESCRIPTOR = _ADDSRROUTEREPLY,
  __module__ = 'parameters_pb2'
  # @@protoc_insertion_point(class_scope:parameters.AddSrRouteReply)
  ))
_sym_db.RegisterMessage(AddSrRouteReply)

RmRouteRequest = _reflection.GeneratedProtocolMessageType('RmRouteRequest', (_message.Message,), dict(
  DESCRIPTOR = _RMROUTEREQUEST,
  __module__ = 'parameters_pb2'
  # @@protoc_insertion_point(class_scope:parameters.RmRouteRequest)
  ))
_sym_db.RegisterMessage(RmRouteRequest)

RmRouteReply = _reflection.GeneratedProtocolMessageType('RmRouteReply', (_message.Message,), dict(
  DESCRIPTOR = _RMROUTEREPLY,
  __module__ = 'parameters_pb2'
  # @@protoc_insertion_point(class_scope:parameters.RmRouteReply)
  ))
_sym_db.RegisterMessage(RmRouteReply)

ListRouteRequest = _reflection.GeneratedProtocolMessageType('ListRouteRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTROUTEREQUEST,
  __module__ = 'parameters_pb2'
  # @@protoc_insertion_point(class_scope:parameters.ListRouteRequest)
  ))
_sym_db.RegisterMessage(ListRouteRequest)

ListRouteReply = _reflection.GeneratedProtocolMessageType('ListRouteReply', (_message.Message,), dict(
  DESCRIPTOR = _LISTROUTEREPLY,
  __module__ = 'parameters_pb2'
  # @@protoc_insertion_point(class_scope:parameters.ListRouteReply)
  ))
_sym_db.RegisterMessage(ListRouteReply)

ChangeRouteRequest = _reflection.GeneratedProtocolMessageType('ChangeRouteRequest', (_message.Message,), dict(
  DESCRIPTOR = _CHANGEROUTEREQUEST,
  __module__ = 'parameters_pb2'
  # @@protoc_insertion_point(class_scope:parameters.ChangeRouteRequest)
  ))
_sym_db.RegisterMessage(ChangeRouteRequest)

ChangeRouteReply = _reflection.GeneratedProtocolMessageType('ChangeRouteReply', (_message.Message,), dict(
  DESCRIPTOR = _CHANGEROUTEREPLY,
  __module__ = 'parameters_pb2'
  # @@protoc_insertion_point(class_scope:parameters.ChangeRouteReply)
  ))
_sym_db.RegisterMessage(ChangeRouteReply)

ChangeSrRouteRequest = _reflection.GeneratedProtocolMessageType('ChangeSrRouteRequest', (_message.Message,), dict(
  DESCRIPTOR = _CHANGESRROUTEREQUEST,
  __module__ = 'parameters_pb2'
  # @@protoc_insertion_point(class_scope:parameters.ChangeSrRouteRequest)
  ))
_sym_db.RegisterMessage(ChangeSrRouteRequest)

ChangeSrRouteReply = _reflection.GeneratedProtocolMessageType('ChangeSrRouteReply', (_message.Message,), dict(
  DESCRIPTOR = _CHANGESRROUTEREPLY,
  __module__ = 'parameters_pb2'
  # @@protoc_insertion_point(class_scope:parameters.ChangeSrRouteReply)
  ))
_sym_db.RegisterMessage(ChangeSrRouteReply)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('P\001'))

_SEGMENTROUTING = _descriptor.ServiceDescriptor(
  name='SegmentRouting',
  full_name='parameters.SegmentRouting',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=498,
  serialized_end=1055,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddSrRoute',
    full_name='parameters.SegmentRouting.AddSrRoute',
    index=0,
    containing_service=None,
    input_type=_ADDSRROUTEREQUEST,
    output_type=_ADDSRROUTEREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveRoute',
    full_name='parameters.SegmentRouting.RemoveRoute',
    index=1,
    containing_service=None,
    input_type=_RMROUTEREQUEST,
    output_type=_RMROUTEREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListRoute',
    full_name='parameters.SegmentRouting.ListRoute',
    index=2,
    containing_service=None,
    input_type=_LISTROUTEREQUEST,
    output_type=_LISTROUTEREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ChangeRoute',
    full_name='parameters.SegmentRouting.ChangeRoute',
    index=3,
    containing_service=None,
    input_type=_CHANGEROUTEREQUEST,
    output_type=_CHANGEROUTEREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ChangeSrRoute',
    full_name='parameters.SegmentRouting.ChangeSrRoute',
    index=4,
    containing_service=None,
    input_type=_CHANGESRROUTEREQUEST,
    output_type=_CHANGESRROUTEREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='BunchAddSrRoute',
    full_name='parameters.SegmentRouting.BunchAddSrRoute',
    index=5,
    containing_service=None,
    input_type=_ADDSRROUTEREQUEST,
    output_type=_ADDSRROUTEREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='BunchRemoveRoute',
    full_name='parameters.SegmentRouting.BunchRemoveRoute',
    index=6,
    containing_service=None,
    input_type=_RMROUTEREQUEST,
    output_type=_RMROUTEREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SEGMENTROUTING)

DESCRIPTOR.services_by_name['SegmentRouting'] = _SEGMENTROUTING

# @@protoc_insertion_point(module_scope)
