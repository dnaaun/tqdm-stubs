import sys
import os

try:
    get_ipython = sys.modules["IPython"].get_ipython
    if "IPKernelApp" not in get_ipython().config:
        raise ImportError("console")
    if "VSCODE_PID" in os.environ:
        raise ImportError("vscode")
except Exception:
    from .std import tqdm, trange
else:
    from .notebook import tqdm, trange

__all__ = ["tqdm", "trange"]
