from hashlib import _Hash
from typing import Callable, Optional

from .context import Context


def validate_secret(secret: bytes) -> bool: ...


def verify_signature(
    signature: bytes,
    message: bytes,
    public_key: bytes,
    hasher: Optional[Callable[[bytes], _Hash]] = ...,
    context: Context = ...,
) -> bool: ...
