# toolbox-py




```python
# 在 Python 3.10 中才能使用 TypeAlias 和类型联合运算符|。

# from lis.py
import math
import operator as op
from collections import ChainMap
from itertools import chain
from typing import Any, TypeAlias, NoReturn

Symbol: TypeAlias = str
Atom: TypeAlias = float | int | Symbol
Expression: TypeAlias = Atom | list
```
