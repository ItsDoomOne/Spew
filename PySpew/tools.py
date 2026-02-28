import base64
from utils import fancyexit
import sys
from pathlib import Path

path = sys.argv[1:]
print(path)
path_object = Path(path)
if path_object.parent.exists():
    with open(path_object, "rb") as f:
        debugprint(f"{path} Parent is real")
        encoded = base64.b64(f)
        print(encoded)
else:
    fancyexit(f"{path} Parent does not exist; halting.")