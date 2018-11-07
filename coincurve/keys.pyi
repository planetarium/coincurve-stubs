from hashlib import _Hash
from typing import Callable, Optional, Tuple

from .context import Context


# typedef int (*secp256k1_nonce_function)(
#     unsigned char *nonce32,
#     const unsigned char *msg32,
#     const unsigned char *key32,
#     const unsigned char *algo16,
#     void *data,
#     unsigned int attempt
# );
secp256k1_nonce_function = Callable[
    [bytes, bytes, bytes, bytes, bytes, int],
    int
]

class PrivateKey(object):

    context: Context
    public_key: 'PublicKey'
    secret: bytes

    def __init__(
        self,
        secret: Optional[bytes] = None,
        context: Context = ...,
    ) -> None: ...

    def sign(
        self,
        message: bytes,
        hasher: Optional[Callable[[bytes], _Hash]] = ...,
        custom_nonce: Optional[Tuple[secp256k1_nonce_function, bytes]] = ...,
    ) -> bytes: ...

    def sign_recoverable(
        self,
        message: bytes,
        hasher: Optional[Callable[[bytes], _Hash]] = ...,
    ) -> bytes: ...

    def ecdh(self, public_key: bytes) -> bytes: ...
    def add(self, scalar: bytes, update: bool = ...) -> 'PrivateKey': ...
    def multiply(self, scalar: bytes, update: bool = ...) -> 'PrivateKey': ...
    def to_hex(self) -> str: ...
    def to_int(self) -> int: ...
    def to_pem(self) -> bytes: ...
    def to_der(self) -> bytes: ...

    @classmethod
    def from_hex(cls, hexed: str, context: Context = ...) -> 'PrivateKey': ...

    @classmethod
    def from_int(cls, num: int, context: Context = ...) -> 'PrivateKey': ...

    @classmethod
    def from_pem(cls, pem: bytes, context: Context = ...) -> 'PrivateKey': ...

    @classmethod
    def from_der(cls, der: bytes, context: Context = ...) -> 'PrivateKey': ...

    def __eq__(self, other: 'PrivateKey') -> bool: ...


class PublicKey(object):

    context: Context

    def __init__(self, data: bytes, context: Context = ...) -> None: ...

    @classmethod
    def from_secret(
        cls,
        secret: bytes,
        context: Context = ...,
    ) -> 'PublicKey': ...

    @classmethod
    def from_valid_secret(
        cls,
        secret: bytes,
        context: Context = ...,
    ) -> 'PublicKey': ...

    @classmethod
    def from_point(
        cls,
        x: int,
        y: int,
        context: Context = ...,
    ) -> 'PublicKey': ...

    @classmethod
    def from_signature_and_message(
        cls,
        serialized_sig: bytes,
        message: bytes,
        hasher: Optional[Callable[[bytes], _Hash]] = ...,
        context: Context = ...,
    ) -> 'PublicKey': ...

    @classmethod
    def combine_keys(
        cls,
        public_keys: Sequence['PublicKey'],
        context: Context = ...,
    ) -> 'PublicKey': ...

    def format(self, compressed: bool = ...) -> bytes: ...
    def point(self) -> Tuple[int, int]: ...

    def verify(
        self,
        signature: bytes,
        message: bytes,
        hasher: Optional[Callable[[bytes], _Hash]] = ...,
    ): ...

    def add(self, scalar: bytes, update: bool = ...) -> 'PublicKey': ...
    def multiply(self, scalar: bytes, update: bool = ...) -> 'PublicKey': ...

    def combine(
        self,
        public_keys: Sequence['PublicKey'],
        update: bool = ...,
    ) -> 'PublicKey': ...

    def __eq__(self, other: 'PublicKey') -> bool: ...
