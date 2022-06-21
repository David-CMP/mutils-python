#TODO: Finish writing docstrings


def str2bin(x: str) -> str:
    """The binary form of the string's data"""
    return bin(int.from_bytes(x.encode(), "big")).removeprefix("0b")


def str2int(x: str) -> int:
    """An integer representation of the string's data"""
    return int.from_bytes(x.encode(), "big")


def str2hex(x: str) -> str:
    """The hexadecimal form of the string's data"""
    return x.encode(errors="ignore").replace(b"\x00", b"").hex()


def str2bytes(x: str) -> bytes:
    """Similar to x.encode()"""
    return x.encode(errors="ignore").replace(b"\x00", b"")


def bin2str(x: str) -> str:
    """The binary data as a utf-8 string"""
    int_ = int(x, 2)
    return int_.to_bytes(
        int_.bit_length(), "big"
    ).decode(errors="ignore").replace("\x00", "")

def bin2int(x: str) -> int:
    """Same as `int(x, 2)`"""
    return int(x, 2)

def bin2hex(x: str) -> str:
    """The hexadecimal representation of the binary value. Similar to
    `hex(bin2int(x))`"""
    int_ = int(x, 2)
    return int_.to_bytes(int_.bit_length(), "big").replace(b"\x00", 
                                                           b"").hex()

def bin2bytes(x: str) -> bytes:
    """The binary value encoded with utf-8"""
    int_ = int(x, 2)
    return int_.to_bytes(int_.bit_length(), "big").replace(b"\x00", b"")


def int2str(x: int) -> str:
    """The integer value as a utf-8 string"""
    return x.to_bytes(
        x.bit_length(), "big"
    ).decode(errors="ignore").replace("\x00", "")


def int2bin(x: int) -> str:
    """Similar to `bin(x)` but without the prefix"""
    return bin(x).removeprefix("0b")


def int2hex(x: int) -> str:
    """The hexadecimal representation of the integer value. Similar to
    `hex(int(x))`"""
    return x.to_bytes(x.bit_length(), "big").replace(b"\x00", b"").hex()


def int2bytes(x: int) -> bytes:
    """The integer value as bytes"""
    return x.to_bytes(x.bit_length(), "big").replace(b"\x00", b"")


def hex2str(x: str) -> str:
    return bytes.fromhex(x).decode(errors="ignore").replace(b"\x00", b"")


def hex2bin(x: str) -> str:
    return bin(int(x, 16)).removeprefix("0b")


def hex2int(x: str) -> int:
    return int(x, 16)


def hex2bytes(x: str) -> bytes:
    return bytes.fromhex(x).replace(b"\x00", b"")


def bytes2str(x: bytes) -> str:
    return x.decode(errors="ignore").replace("\x00", "")


def bytes2bin(x: bytes) -> str:
    return bin(int.from_bytes(x, "big")).removeprefix("0b")


def bytes2int(x: bytes) -> int:
    return int.from_bytes(x, "big")


def bytes2hex(x: bytes) -> str:
    return x.hex()
