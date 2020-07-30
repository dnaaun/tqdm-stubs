from tqdm.utils import ObjectWrapper
from typing import Any, Optional

class DummyTqdmFile(ObjectWrapper):
    def write(self, x: Any, nolock: bool = ...) -> None: ...

def tenumerate(iterable: Any, start: int = ..., total: Optional[Any] = ..., tqdm_class: Any = ..., **tqdm_kwargs: Any): ...

tzip: Any
tmap: Any
