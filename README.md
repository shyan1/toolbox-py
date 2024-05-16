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

# lis.py：负责解析的主要函数
def parse(program: str) -> Expression:
    "从字符串中读取Scheme表达式。"
    return read_from_tokens(tokenize(program))

def tokenize(s: str) -> list[str]:
    "把字符串转换成词法单元列表。"
    return s.replace('(', ' ( ').replace(')', ' ) ').split()

def read_from_tokens(tokens: list[str]) -> Expression:
    "从一系列词法单元中读取表达式。"
    # 排版需要，省略了很多解析代码
```
