from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReduceRequest(_message.Message):
    __slots__ = ("audio", "rate")
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    audio: bytes
    rate: int
    def __init__(self, audio: _Optional[bytes] = ..., rate: _Optional[int] = ...) -> None: ...

class ReduceReply(_message.Message):
    __slots__ = ("audio",)
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    audio: bytes
    def __init__(self, audio: _Optional[bytes] = ...) -> None: ...
