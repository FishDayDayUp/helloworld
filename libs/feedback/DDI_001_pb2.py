# Generated by the protocol buffer compiler.  DO NOT EDIT!
import sys

sys.path.append('/opt/trend/ddei/lib64/protobuf-2.4.1-py2.6.egg/')

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='DDI_001.proto',
  package='',
  serialized_pb='\n\rDDI_001.proto\"\xbc\x03\n\x0f\x44\x44IFeedBackInfo\x12\x1a\n\x12\x44\x65tected_file_sha1\x18\x01 \x01(\x0c\x12\x1a\n\x12\x44\x65tected_file_type\x18\x02 \x01(\r\x12\x1d\n\x15\x44\x65tected_file_subtype\x18\x03 \x01(\r\x12\x1a\n\x12\x44\x65tected_file_size\x18\x04 \x01(\x03\x12\x16\n\x0e\x44\x65tection_name\x18\x05 \x02(\t\x12\x10\n\x08\x44\x65tector\x18\x06 \x02(\t\x12\x19\n\x11\x41rchive_file_sha1\x18\x07 \x01(\x0c\x12\x19\n\x11\x41rchive_file_type\x18\x08 \x01(\r\x12\x1c\n\x14\x41rchive_file_subtype\x18\t \x01(\r\x12\x19\n\x11\x41rchive_file_size\x18\n \x01(\x03\x12\x1c\n\x14\x41ttachment_file_sha1\x18\x0b \x01(\x0c\x12\x1c\n\x14\x41ttachment_file_type\x18\x0c \x01(\r\x12\x1f\n\x17\x41ttachment_file_subtype\x18\r \x01(\r\x12\x1c\n\x14\x41ttachment_file_size\x18\x0e \x01(\x03\x12\x0b\n\x03URL\x18\x0f \x01(\t\x12\x15\n\rprotocol_type\x18\x10 \x02(\r')




_DDIFEEDBACKINFO = descriptor.Descriptor(
  name='DDIFeedBackInfo',
  full_name='DDIFeedBackInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='Detected_file_sha1', full_name='DDIFeedBackInfo.Detected_file_sha1', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='Detected_file_type', full_name='DDIFeedBackInfo.Detected_file_type', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='Detected_file_subtype', full_name='DDIFeedBackInfo.Detected_file_subtype', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='Detected_file_size', full_name='DDIFeedBackInfo.Detected_file_size', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='Detection_name', full_name='DDIFeedBackInfo.Detection_name', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='Detector', full_name='DDIFeedBackInfo.Detector', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='Archive_file_sha1', full_name='DDIFeedBackInfo.Archive_file_sha1', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='Archive_file_type', full_name='DDIFeedBackInfo.Archive_file_type', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='Archive_file_subtype', full_name='DDIFeedBackInfo.Archive_file_subtype', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='Archive_file_size', full_name='DDIFeedBackInfo.Archive_file_size', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='Attachment_file_sha1', full_name='DDIFeedBackInfo.Attachment_file_sha1', index=10,
      number=11, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='Attachment_file_type', full_name='DDIFeedBackInfo.Attachment_file_type', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='Attachment_file_subtype', full_name='DDIFeedBackInfo.Attachment_file_subtype', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='Attachment_file_size', full_name='DDIFeedBackInfo.Attachment_file_size', index=13,
      number=14, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='URL', full_name='DDIFeedBackInfo.URL', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='protocol_type', full_name='DDIFeedBackInfo.protocol_type', index=15,
      number=16, type=13, cpp_type=3, label=2,
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
  serialized_start=18,
  serialized_end=462,
)

DESCRIPTOR.message_types_by_name['DDIFeedBackInfo'] = _DDIFEEDBACKINFO

class DDIFeedBackInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DDIFEEDBACKINFO
  
  # @@protoc_insertion_point(class_scope:DDIFeedBackInfo)

# @@protoc_insertion_point(module_scope)
