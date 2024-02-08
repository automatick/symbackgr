import ctypes as ct
from typing import Any

libc: ct.CDLL = ct.CDLL("libc.so.6")


def read(file_descriptor, size):
    buffer = ct.create_string_buffer(size)
    bytes_read = libc.read(file_descriptor, buffer, size)
    if bytes_read == -1:
        raise OSError(f"read error: {ct.get_errno()}")
    return bytes(buffer[:bytes_read])


def write(text: Any) -> None:
    encoded_text: bytes = str(text).encode()
    libc.write(0, encoded_text, len(encoded_text))


class Timespec(ct.Structure):
    _fields_ = [("tv_sec", ct.c_long),
                ("tv_nsec", ct.c_long)]


def nanosleep(requested_time):
    req = Timespec()
    req.tv_sec = ct.c_long(requested_time // 1000000000)
    req.tv_nsec = ct.c_long(requested_time % 1000000000)
    rem = Timespec()
    result = libc.nanosleep(ct.byref(req), ct.byref(rem))
    if result != 0:
        raise OSError("nanosleep failed")
    return rem.tv_sec * 1000000000 + rem.tv_nsec
