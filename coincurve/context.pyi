from typing import Optional


class Context:

    def __init__(
        self,
        seed: Optional[bytes] = ...,
        flag: int = ...,
    ) -> None: ...

    def reseed(self, seed: Optional[bytes] = ...) -> None: ...


GLOBAL_CONTEXT: Context
